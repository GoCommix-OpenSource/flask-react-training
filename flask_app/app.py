from re import L
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

# config = {
#     'DEBUG':TRUE,
#     'MONGODB_SETTINGS':{
#         'db': 'project1',
#         'host': '192.168.1.35',
#         'port': 12345
#     }
# }

# CONFIG
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_mongo',
    'host': '127.0.0.1',
    'port': 27017
}
app.config['DEBUG']=True
db = MongoEngine(app)


# Models
'''
# Types of Document that we can to create models -
1. db.Document 
2. db.EmbeddedDocument
3. db.DynamicDocument
4. db.DynamicEmbeddedDocument
'''


class Movie(db.Document):
    '''## movie model that contains title and stars'''
    title = db.StringField()
    stars = db.DecimalField()

class Imdb(db.EmbededDocument):
    pass

class Director(db.DynamicDocument):
    pass

class Cast(db.DynamicEmbededDocument):
    pass    

# Routes

@app.route('/') # route (endpoints)
def hello():
    movies = Movie.objects()
    return jsonify(movies)


@app.route('/<first_name>') # route (endpoints)
def greet(first_name):
    return jsonify(first_name=first_name)



