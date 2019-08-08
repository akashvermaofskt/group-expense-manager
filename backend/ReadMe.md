This repo contains all APIs used in this project.

## How to set up the project environemnt

* [Clone](https://github.com/akashvermaofskt/group-expense-manager.git) this repo in your local machine.
* [Install](https://blog.ruanbekker.com/blog/2018/11/27/python-flask-tutorial-series-create-a-hello-world-app-p1/) python3. 
* cd ⁨`group-expense-manager/backend`
* setup [virtual environment](https://blog.ruanbekker.com/blog/2018/12/09/python-flask-tutorial-series-setup-a-python-virtual-environment-p2/) in it.
* Install all required packages mentioned in `requirement.txt`.


## How to run the backend
    
* Open terminal then `cd group-expense-manager/backend` 
* Run command `python3 api.py` in your terminal this will create the database name `version1.db` in the backend folder which contains all the required tables.
![Database](https://user-images.githubusercontent.com/21224753/62530443-20e7a780-b85e-11e9-9978-b6fd4ffd9b38.png)


## How to hit APIs

#### To signup new user i.e `POST`

* Hit following API http://0.0.0.0:5000/api/signup/ in postman then write in this format in the body. 
```
{
    "User": {
        "Name": "Mohit Rai",
        "Email": "cenation092@gmail.com",
        "Password": "1234567890"
    }
}
```

* This will return a JSON file of the signup user details(which is initially not verified) in this format.

```
{
    "login_details": {
        "email": "cenation092@gmail.com",
        "name": "Mohit Rai",
        "status": "Not Verified"
    }
}
```
![Post](https://user-images.githubusercontent.com/21224753/62530271-d82fee80-b85d-11e9-9f9a-3ed7834a0b1a.png)

#### To login the existing user i.e `GET`

* Hit following API http://0.0.0.0:5000/api/login/ in postman then write the email id and password in the Authorization. 
* This will return a JSON file which contains the unique token for that user with limited expiry time.

![GET](https://user-images.githubusercontent.com/21224753/62531011-30b3bb80-b85f-11e9-9842-7ef6e1948eb8.png)

#### After getting the token use that token as username whenever user provide any service under Authorization

![Token](https://user-images.githubusercontent.com/21224753/62531248-af105d80-b85f-11e9-8675-69e3865fb120.png)

#### To create New group for existing user i.e `POST`

* Hit following API http://0.0.0.0:5000/api/create_group/ in postman then write in this format in the body. 
```
{
    "Group": {
        "Name": "Test Group"
    }
}
```

* This will return a JSON file of group details in this format.

```
{
    "Group Details": {
        "name": "Test Group",
        "owner": "cenation092@gmail.com",
        "status": "Active"
    }
}
```

#### To add new member in the existing group i.e `POST`

* Hit following API http://0.0.0.0:5000/api/add_user_to_group/ in postman then write in this format in the body. 
```
{
    "Group": {
        "Group_Name": "Test Group",
        "New_Person_Email": "akashvermaofskt@gmail.com"
    }
}
```

* This will return a JSON file of group mapping details in this format.

```
{
    "Group Mapping Details": {
        "Group": 1,
        "User": 2
    }
}
```

#### To add new friend for an existing user i.e `POST`

* Hit following API http://0.0.0.0:5000/api/add_friend/ in postman then write in this format in the body. 
```
{
    "Friend_Details": {
        "Friend_Email": "akashvermaofskt@gmail.com"
    }
}
```

* This will return a JSON file of friend mapping details in this format.

```
{
    "Friend Mapping Details": {
        "Friend_id": 2,
        "User_id": 1
    }
}
```

#### To get the details of an existing user i.e `GET`

* Hit following API http://0.0.0.0:5000/api/details/ in postman with the token in the authentication.


* This will return a JSON file of friend mapping details in this format.

```
{
  	"User Details": {
    	"Email": "cenation092@gmail.com",
    	"Member Since": "Thu, 08 Aug 2019 00:07:17 GMT",
    	"Name": "Mohit Rai",
    	"Stauts": "Not Verified"
  	}
}
```

#### To retrive all friends of an existing user i.e `GET`

* Hit following API http://0.0.0.0:5000/api/all_friends/ in postman with the token in the authentication.


* This will return a JSON file of friend mapping details in this format.

```
{
  	"All_Friend_Name": [ "Akash Verma", "Friend2", "Friend3" ]
}
```

#### To retrive all active groups of an existing user i.e `GET`

* Hit following API http://0.0.0.0:5000/api/active_group/ in postman with the token in the authentication.


* This will return a JSON file of friend mapping details in this format.

```
{
    "Active Groups": [
        {
            "Id": 3,
            "Name": "Test Group"
        },
        {
            "Id": 4,
            "Name": "Test Group"
        },
        {
            "Id": 5,
            "Name": "Test Group 2"
        }
    ]
}
```

#### To retrive all active groups of an existing user i.e `GET`

* Hit following API http://0.0.0.0:5000/api/deactive_group/ in postman with the token in the authentication.


* This will return a JSON file of friend mapping details in this format.

```
{
    "Deactive Groups": [
        {
            "Id": 3,
            "Name": "Test Group"
        },
        {
            "Id": 4,
            "Name": "Test Group"
        }
    ]
}
```

#### To retrive group details i.e `GET`

* Hit following API http://0.0.0.0:5000/api/group_details/ in postman then write in this format in the body. 
```
{
    "Group": {
        "Id": 1
    }
}
```

* This will return a JSON file of friend mapping details in this format.

```
{
 	"Group Details": {
    	"Created By": "Mohit Rai",
    	"Created On": "Wed, 07 Aug 2019 22:46:11 GMT",
    	"Members Name": [ "Mohit Rai", "Akash Verma" ],
    	"Name": "Pta Ni",
    	"Status": "Active"
  	}
}
```