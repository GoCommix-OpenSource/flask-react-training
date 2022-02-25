from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# 3. Register blue print with app instance (blue print)
def create_user_module(app, **kwargs):
    from .controller import user_blueprint
    app.register_blueprint(user_blueprint)
    