from sqlalchemy import Column,Integer,String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import datetime

Base = declarative_base()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))

class UserInfo(Base):
    __tablename__ = "UserData"
    #attributes for userdata table
    id = Column(Integer, primary_key = True )
    name = Column( String(100), nullable = False )
    email = Column( String(120), unique = True )
    password_hash = Column( String(100), nullable = False )
    status = Column( String(10), nullable = False ) #for verify email
    phone_number = Column(Integer,nullable = True)
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)  

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600000):
    	s = Serializer(secret_key, expires_in = expiration)
    	return s.dumps({'email': self.email }) 

    @staticmethod
    def verify_auth_token(token):
    	s = Serializer(secret_key)
    	try:
    		data = s.loads(token)
    	except SignatureExpired:
    		#Valid Token, but expired
    		return None
    	except BadSignature:
    		#Invalid Token
    		return None
    	email = data['email']
    	return email

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.status = "Not Verified"

    def toJSON(self):
        return { "login_details" : {
                "email" : self.email,
                "name" : self.name,
                "status" : self.status
            }
        }

class GroupInfo(Base):
    __tablename__ = "GroupData"
    #attributes for userdata table
    id = Column(Integer, primary_key = True )
    name = Column( String(100), nullable = False, primary_key = True )
    owner = Column( String(120), nullable = False, primary_key = True )
    status = Column( String(10), nullable = False ) #active or not
    created_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)  

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.status = "Active"

    def toJSON(self):
        return { "Group Details" : {
                "owner" : self.owner,
                "name" : self.name,
                "status" : self.status
            }
        }

class GroupMapping(Base):
    __tablename__ = "GroupMapping"
    #attributes for userdata table
    id = Column(Integer, primary_key = True )
    user_id = Column( Integer, nullable = False)
    group_id = Column( Integer, nullable = False )
    spent = Column( Integer, nullable = False )
    paid = Column( Integer, nullable = False )
    created_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)  

    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id
        self.spent = 0
        self.paid = 0
    
    def toJSON(self):
        return { "Group Mapping Details" : {
                "Group" : self.group_id,
                "User" : self.user_id
            }
        }

class FriendMapping(Base):
    __tablename__ = "Friends"
    #attributes for userdata table
    user_id = Column( Integer, nullable = False, primary_key = True)
    friend_id = Column( Integer, nullable = False, primary_key = True)
    created_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)  

    def __init__(self, user_id, friend_id):
        self.user_id = user_id
        self.friend_id = friend_id
    
    def toJSON(self):
        return { "Friend Mapping Details" : {
                "User_id" : self.user_id,
                "Friend_id" : self.friend_id
            }
        }

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///version1.db')

Base.metadata.create_all(engine)
