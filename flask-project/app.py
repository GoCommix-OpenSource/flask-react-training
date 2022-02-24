from distutils.debug import DEBUG
import os
from backend import create_app
env = os.environ.get('WEBAPP_ENV','dev')

app = create_app(f'config.{env.capitalize()}Conf')

if __name__ =="__main__":
    app.run()
