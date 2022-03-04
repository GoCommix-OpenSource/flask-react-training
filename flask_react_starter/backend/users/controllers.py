from flask import Blueprint, jsonify, request
from .models import User
from .. import MyException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# 1. instansiate a blueprint (blueprint)
user_blueprint = Blueprint('users',__name__,template_folder='templates',url_prefix="/api")

# 2. create routes using blueprint instance (blueprint)
@user_blueprint.route('/users/', methods=['GET'])
def users():
    response= {
        "error":True,
        "data":"",
        "message":""
    }
    response["data"] = User.objects()
    return jsonify(response)

@user_blueprint.route('/users/<id>/', methods=['GET'])
@jwt_required()
def user(id):
    response= {
        "error":True,
        "data":"",
        "message":""
    }
    print("call hua")
    try:
        user_data = User.objects.get(id=id)
    except:
        response["message"] = "username does not exist" 
        user_data = None   
    if user_data is not None:
        request_user = get_jwt_identity()
        if user_data.username == request_user:
            response["data"] = User.objects.get(id=id)
            response["error"] = False
        else:
            response["message"] = "Request not allowed"
    return jsonify(response)

@user_blueprint.route('/signup/', methods=['POST'])
def signup():
    data = request.get_json()
    response= {
        "error":True,
        "data":"",
        "message":""
    }   
    try:
        user = User(username=data['username'])
        # password validation
        # 1. validate the password string (must contain a number , alphabets, and minimum of 6 digits)
        # 2. save the password
        # 3. if password is not valid(ease a exception"password is not valid") return appropriate message in response
        from re import match
        pattern=r"^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9]{6,}"
        
        matched = match(pattern, data['password'])
        if matched is None:
            raise MyException("password must contain a number ,an alphabet, and minimum of 6 charecters")
        
        user.set_password(data['password'])
        user.save()
        response["data"]=user
        response["error"]=False
        response["message"]="User Created"
    
    except MyException as e:
        response["data"] = None
        response["message"] = str(e)
        
    except Exception as e:
        if "duplicate" in str(e):
            response["data"]=None
            response["message"]="Try different username"
    
    return jsonify(response)

@user_blueprint.route('/login/',methods=['POST'])
def login():
    '''
# Input fields

```json
{
    "username": string,
    "password": string
}
```

# output
```json
{
    "error": boolean
    "message" : string
    "data"  : data
    "user": UserObject,
    "token": "access token"
}
```
'''
    data = request.get_json()
    response= {
        "error":True,
        "data":"",
        "message":""
    }
    username = data["username"]
    password = data["password"]
    
    try:
        # check if username is registered or not
        user = User.objects.get(username = username)
    except:
        user = None
    
    if user is not None:
        matched = user.check_password(password)    
        if matched:
            # generate token
            # send token as a response
            access_token = create_access_token(identity=username,)
            response["data"]={"user":user,"token":access_token}
            response['error']=False
            response['message']="User Logged in"
        else:
            response['message']="Invalid Credentials"
    else:
            response['message']="User Not found"
        
    print("login request received",username, password)
    return jsonify(response)