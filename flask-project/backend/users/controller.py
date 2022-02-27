from flask import Blueprint, jsonify, request
from .models import User
from .. import MyException
# 1. instansiate a blueprint (blueprint)
user_blueprint = Blueprint('user',__name__,template_folder='templates',url_prefix="/api")

# 2. create routes using blueprint instance (blueprint)
@user_blueprint.route('/users/', methods=['GET'])
def users():
    users = User.objects()
    return jsonify(users)

@user_blueprint.route('/users/<id>/', methods=['GET'])
def user(id):
    users = User.objects.get(id=id)
    return jsonify(users)

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
    data = request.get_json()
    response= {
        "error":True,
        "data":"",
        "message":""
    }
    username = data["username"]
    password = data["password"]
    
    try:
        user = User.objects.get(username = username)
    except:
        user = None
    
    if user is not None:
        matched = user.check_password(password)    
        if matched:
            # generate token
            # send token as a response
            token="token"
            response["data"]={"user":user,"token":token}
            response['error']=False
            response['message']="User Logged in"
        else:
            response['message']="Invalid username or password"
    return jsonify(response)