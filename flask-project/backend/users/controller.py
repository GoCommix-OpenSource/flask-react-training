from flask import Blueprint, jsonify, request
from .models import User

# 1. instansiate a blueprint (blueprint)
user_blueprint = Blueprint('user',__name__,template_folder='templates',url_prefix="/api")

# 2. create routes using blueprint instance (blueprint)
@user_blueprint.route('/user/', methods=['GET'])
def user():
    users = User.objects()
    return jsonify(users)

@user_blueprint.route('/user/signup/', methods=['POST'])
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
        
        user.set_password(data['password'])
        user.save()
        response["data"]=user
        response["error"]=False
        response["message"]="User Created"
    except Exception as e:
        if "duplicate" in str(e):
            response["data"]=None
            response["message"]="Try different username"

    return jsonify(response)