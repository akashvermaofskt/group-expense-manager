from flask import Flask, request, jsonify
from models import db, UserInfo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from SendVerification import verify
import json
import os

app = Flask(__name__) # Flask object created
CORS(app) # CORS (Cross-Origin Resource Sharing) is a standard for accessing web resources on different domains.
bcrypt = Bcrypt(app) # to encrypt pasword

basedir = os.path.abspath(os.path.dirname(__file__)) # path of this file

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db.init_app(app)

@app.route("/api/signup/", methods=["POST"])
def create_user():
    data = request.json["User"]
    name = data["Name"]
    email = data["Email"]
    _password = data["Password"]
    _password = bcrypt.generate_password_hash(_password, 12)
    # new user created
    new_user = UserInfo(name, email, _password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.toJSON()), 201
    except:
        return { "Error" : "Internal Server Error" }, 500

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
