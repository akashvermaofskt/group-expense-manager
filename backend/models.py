from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

class UserInfo(db.Model):
    __tablename__ = "UserData"
    #attributes for userdata table
    name = db.Column( db.String(100), nullable = False )
    email = db.Column( db.String(120), primary_key=True )
    _password = db.Column( db.String(100), nullable = False )
    status = db.Column( db.String(10), nullable = False ) #for verify email
    phone_number = db.Column(db.Integer,nullable = True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    

    def __init__(self, email, name, _password ):
        self.name = name
        self.email = email
        self._password = _password
        self.status = "Not Verified"

    def toJSON(self):
        return { "login_detail" : {
                "email" : self.email,
                "name" : self.name,
                "status" : self.status
            }
        }
