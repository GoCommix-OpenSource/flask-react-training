from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
# {
#     "name":"xyz",
#     "course":"mca",
#     ...
#     ...
# }
'''
class Student(db.Model):
    name=
    roll=
    dob=
    course=

name|roll| dob course
    |    |
    
    
student = [   
{
    "id":"34"
    "name":"abc",
    "roll": "1"
    ..
    ..
},
{
    "id":"435"
  "name":"xyz",
  "roll":"2",
  ...
  ...  
},
]
''' 


app = Flask(__name__)


app.config.from_pyfile('mongo.cfg')
db = MongoEngine(app)



@app.route('/') # route (endpoints)
def hello():
    return "hello world"


@app.route('/<first_name>') # route (endpoints)
def greet(first_name):
    return jsonify(first_name=first_name)



