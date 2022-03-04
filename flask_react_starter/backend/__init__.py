
from flask_mongoengine import MongoEngine
from flask import Flask, render_template
from flask_docs import  ApiDoc
from flask_jwt_extended import JWTManager

# --- for SQL use below ---
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# db = SQLAlchemy()
# migrate = Migrate()


# --- for NoSql ----
mongo = MongoEngine()

class MyException(BaseException):
    pass

def page_not_found(error):
    return render_template('404.html'), 404


def create_app(object_name):
    
    # from .users.controllers import users_blueprint
    app = Flask(__name__)
    jwt = JWTManager(app)
    app.config.from_object(object_name)
    # --- for SQL use below ---
    # db.init_app(app)
    # migrate.init_app(app, db)
    
    # ---for NoSql ----
    mongo.init_app(app)
    
    
    # register your blueprints here
    # app.register_blueprint(users_blueprint)
    
    # or you can call create_module for each module 
    from .users import create_module as register_user
    
    # register you modules here
    register_user(app)
    
    
    
    
    ApiDoc(
        app,
        title="Api Docs",
        version="0.0.1",
        description="A simple app API"

    )
    
    app.register_error_handler(404, page_not_found)
    # app.register_error_handler(200,home)
    
   

    # RESTful Api documents to be excluded
    app.config['RESTFUL_API_DOC_EXCLUDE'] = []
    return app