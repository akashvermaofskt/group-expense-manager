from models import Base, UserInfo, GroupInfo, GroupMapping, FriendMapping
from flask import Flask, jsonify, request, abort, g
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_cors import CORS

auth = HTTPBasicAuth()

engine = create_engine('sqlite:///version1.db')

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
        return jsonify(new_user.toJSON()), 201
    except:
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
        group = session.query(GroupInfo).filter_by(name = name).first()
        group_id = group.id
        # add mapping of user with its group
        new_mapping = GroupMapping(user_id, group_id)
        session.add(new_mapping)
        session.commit()
        return jsonify(new_group.toJSON()), 201
    except:
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
        return jsonify(new_mapping.toJSON()), 201
    except:
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
        new_friend = FriendMapping(user_id, friend_id)
        session.add(new_friend)
        session.commit()
        return jsonify(new_friend.toJSON()), 201
    except:
        return { "Error" : "Internal Server Error" }, 500

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
