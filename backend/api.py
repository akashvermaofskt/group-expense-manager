from models import Base, UserInfo
from flask import Flask, jsonify, request, abort, g
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_cors import CORS

auth = HTTPBasicAuth()

engine = create_engine('sqlite:///foo.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__) # Flask object created
CORS(app) # CORS (Cross-Origin Resource Sharing) is a standard for accessing web resources on different domains.

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

@app.route('/api/login/', methods=["GET"])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})

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
    
@app.route("/api/resource/", methods=["GET"])
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.name })

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
