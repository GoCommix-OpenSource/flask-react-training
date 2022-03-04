from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
def create_module(app, **kwargs):
    bcrypt.init_app(app)
    from .controllers import user_blueprint
    app.register_blueprint(user_blueprint)