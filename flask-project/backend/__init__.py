# import required packages
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from .users import create_user_module
# create mongo instance
mongo = MongoEngine()
class MyException(BaseException):
    pass


def page_not_found(error):
    return render_template('404.html'),404

# create Flask app
def create_app(object_name):
    app = Flask(__name__) # initialize Flask app
    app.config.from_object(object_name)
    mongo.init_app(app) # initialize mongo engine
    app.register_error_handler(404,page_not_found)
    
    # 4. call the create module function
    create_user_module(app)
    return app