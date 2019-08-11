from models import Base, UserInfo, GroupInfo, GroupMapping, FriendMapping
from flask import Flask, jsonify, request, abort, g
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from SendVerification import verify
from sqlalchemy import create_engine
from flask_cors import CORS

auth = HTTPBasicAuth()

engine = create_engine('sqlite:///version1.db',connect_args={'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__) # Flask object created
CORS(app) # CORS (Cross-Origin Resource Sharing) is a standard for accessing web resources on different domains.

#to give access to authorized users
@auth.verify_password
def verify_password(email_or_token, password):
    #Try to see if it's a token first
    email = UserInfo.verify_auth_token(email_or_token)
    if email:
        user = session.query(UserInfo).filter_by(email = email).one()
    else:
        user = session.query(UserInfo).filter_by(email = email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    #session.close()
    g.user = user 
    return True

# Api for login that give the token
@app.route('/api/login/', methods=["GET"])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})

# Api for signup
@app.route("/api/signup/", methods=["POST"])
def create_user():
    data = request.json["User"]
    name = data["Name"]
    email = data["Email"]
    _password = data["Password"]
    # new user created
    new_user = UserInfo(name, email)
    new_user.hash_password(_password)
    try:
        session.add(new_user)
        session.commit()
        #session.close()
        return jsonify(new_user.toJSON()), 201
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500
    
# Api to create group by only authorized users
@app.route("/api/create_group/", methods=["POST"])
@auth.login_required
def create_group():
    data = request.json["Group"]
    name = data["Name"]
    owner = g.user.email
    new_group = GroupInfo(name, owner)
    try:
        session.add(new_group)
        session.commit()
        user = session.query(UserInfo).filter_by(email = owner).first()
        user_id = user.id
        group = session.query(GroupInfo).all()
        if group == None:
            group_id = 1
        else:
            group.reverse()
            group_id = group[0].id
        # add mapping of user with its group
        new_mapping = GroupMapping(user_id, group_id)
        session.add(new_mapping)
        session.commit()
        #session.close()
        return jsonify(new_group.toJSON()), 201
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

# Api to add user in existing group
@app.route("/api/add_user_to_group/", methods=["POST"])
@auth.login_required
def add_user_to_group():
    data = request.json["Group"]
    name = data["Group_Name"]
    email = data["New_Person_Email"]
    try:
        # retrive user_id
        user = session.query(UserInfo).filter_by(email = email).first()
        user_id = user.id
        # retrive group_id
        group = session.query(GroupInfo).filter_by(name = name).first()
        group_id = group.id
        new_mapping = GroupMapping(user_id, group_id)
        session.add(new_mapping)
        session.commit()
        #session.close()
        return jsonify(new_mapping.toJSON()), 201
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

# Api to add friend in existing user
@app.route("/api/add_friend/", methods=["POST"])
@auth.login_required
def add_friend():
    data = request.json["Friend_Details"]
    email = data["Friend_Email"]
    owner = g.user.email
    try:
        # retrive user_id
        user = session.query(UserInfo).filter_by(email = email).first()
        friend_id = user.id
        # retrive group_id
        user = session.query(UserInfo).filter_by(email = owner).first()
        user_id = user.id
        # one side mapping
        new_friend = FriendMapping(user_id, friend_id)
        session.add(new_friend)
        session.commit()
        #other side mapping
        user_id, friend_id = friend_id, user_id
        new_friend = FriendMapping(user_id, friend_id)
        session.add(new_friend)
        session.commit()
        #session.close()
        return jsonify(new_friend.toJSON()), 201
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

#Api for current user detail
@app.route("/api/details/", methods=["GET"])
@auth.login_required
def user_detail():
    user_email = g.user.email
    try:
        user = session.query(UserInfo).filter_by(email = user_email).first()
        email = user.email
        name = user.name
        status = user.status
        member_since = user.created_on
        #session.close()
        return { "User Details" : {
                "Email" : email,
                "Name" : name,
                "Member Since" : member_since,
                "Stauts" : status
            }
        }, 200
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

# Api to retrive all friends of current user
@app.route("/api/all_friends/", methods=["GET"])
@auth.login_required
def retrive_friends():
    user_email = g.user.email
    try:
        user_detail = session.query(UserInfo).filter_by(email = user_email).first()
        user_id = user_detail.id
        all_friends = session.query(FriendMapping).filter_by(user_id = user_id).all()
        friends_ids = []
        for i in all_friends:
            friend_id = i.friend_id
            print(friend_id)
            friends_ids.append(friend_id)
        friend_name = []
        for i in friends_ids:
            cur_friend_name = session.query(UserInfo).filter_by(id = i).first().name
            friend_name.append(cur_friend_name)
        #session.close()
        return {"All_Friend_Name" : friend_name }, 200
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

# Api to retrive all active groups of current user
@app.route("/api/active_group/", methods=["GET"])
@auth.login_required
def retrive_active_groups():
    user_email = g.user.email
    try:
        user_detail = session.query(UserInfo).filter_by(email = user_email).first()
        user_id = user_detail.id
        all_groups = session.query(GroupMapping).filter_by(user_id = user_id).all()
        group_ids = []
        for i in all_groups:
            group_id = i.group_id
            group_ids.append(group_id)
        info = []
        cnt = 1
        for i in group_ids:
            cur_group = session.query(GroupInfo).filter_by(id = i, status = "Active").first()
            cur_group_info = {}
            name = cur_group.name
            id = cur_group.id
            cur_group_info["Name"] = name
            cur_group_info["Id"] = id
            info.append(cur_group_info)
            cnt += 1
        #session.close()
        return {"Active Groups" : info }, 200   
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

# Api to retrive all deactive groups of current user
@app.route("/api/deactive_group/", methods=["GET"])
@auth.login_required
def retrive_deactive_groups():
    user_email = g.user.email
    try:
        user_detail = session.query(UserInfo).filter_by(email = user_email).first()
        user_id = user_detail.id
        all_groups = session.query(GroupMapping).filter_by(user_id = user_id).all()
        group_ids = []
        for i in all_groups:
            group_id = i.group_id
            group_ids.append(group_id)
        info = []
        cnt = 1
        for i in group_ids:
            cur_group = session.query(GroupInfo).filter_by(id = i, status = "Deactive").first()
            cur_group_info = {}
            name = cur_group.name
            id = cur_group.id
            cur_group_info["Name"] = name
            cur_group_info["Id"] = id
            info.append(cur_group_info)
            cnt += 1
        #session.close()
        return {
                "Deactive Groups" : info}, 200  
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

# Api to retrive details of a group
@app.route("/api/group_details/", methods=["GET"])
@auth.login_required
def retrive_group_details():
    data = request.json["Group"]
    id = data["Id"]
    try:
        Group = session.query(GroupInfo).filter_by(id = id).first()
        group_name = Group.name
        owner = Group.owner
        status = Group.status
        created_on = Group.created_on
        created_by = session.query(UserInfo).filter_by(email=owner).first().name
        members = session.query(GroupMapping).filter_by(group_id=id).all()
        member_ids = []
        for i in members:
            member_ids.append(i.user_id)
        member_names = []
        for i in member_ids:
            name = session.query(UserInfo).filter_by(id = i).first().name
            member_names.append(name)
        #session.close()
        return {
                "Group Details" : 
                    {
                        "Status" : status,
                        "Name" : group_name,
                        "Created By" : created_by,
                        "Created On" : created_on,
                        "Members Name" : member_names
                    }
                }, 200
    except:
        session.rollback()
        #session.close()
        return { "Error" : "Internal Server Error" }, 500

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
