import os
from flask import render_template
from backend import create_app
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app(f'config.{env.capitalize()}Config')
@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
@app.route("/<path:path>")
def home(path):
    return render_template("home.html")
if __name__ == '__main__':
    app.run()