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
'''STUDENT
{
    "NAME":"SDFSD",
    "YEAR":3,
    "COURSE":{
      "ID":"FGD",
      "DURATION:"DFG"
      "SUBJECTS":"DFG"
      "DFGDFG":"SSDF" 
    }
     
}
'''

'''MOVIE
[
    {
      "TITLE":"movie1",
      "YEAR:"",
      "STARS":""
      ...
      ...
      ...  
    },
    {
      "TITLE":"movie2",
      "YEAR:"",
      "STARS":""
      ...
      ...
      ...  
    },
    ..
    ..
]
'''
'''USER
{
    "USERNAME":"USERNAME"
    "PASSWORD":"SKADFJHKWF"
}
'''

class Movie(db.Document):
    '''## movie model that contains title and stars'''
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField()
    director = db.StringField()
    actors = db.ListField()

# class Imdb(db.EmbededDocument):
#     pass  

# Routes

@app.route('/') # route (endpoints)
def hello():
    return "Hello world"

@app.route('/movie')
def get_all_movies():
    movies = Movie.objects()
    return jsonify(movies)

@app.route('/movie/create')
def create_movie():
    # movie = Movie(
    #     title="Movie1",
    #     year=2021,
    #     rated="3.5",
    #     director="director",
    #     actors=["actor1", "actor2"]
    # )
    
    movie=Movie(title="movie2")
    movie.year = 2022
    movie.rated="3.5"
    director_name = "director2"
    movie.director=director_name
    movie.actors=["actor1", "actor2"]
    movie.save()
    return jsonify(movie)


@app.route('/<first_name>') # route (endpoints)
def greet(first_name):
    return jsonify(first_name=first_name)



