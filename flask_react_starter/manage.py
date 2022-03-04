import os
from backend import mongo, create_app
from backend.users.models import User
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app(f'config.{env.capitalize()}Config')
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=mongo, User=User)