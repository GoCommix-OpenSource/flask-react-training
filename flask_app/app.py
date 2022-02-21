
from flask import Flask, jsonify, request
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
[
    {
        "USERNAME":"USERNAME"
        "PASSWORD":"SKADFJHKWF"
    },
    {
        "USERNAME":"USERNAME2"
        "PASSWORD":"SKADFJHKWF"
    },
    
    
]
'''

class Imdb(db.EmbeddedDocument):
    imdb_id = db.StringField() # It is good practice to create a separate  id for embedded Document 
    rating = db.DecimalField()
    votes = db.IntField()
'''
{
    "_id":{"$oid":"6210c348d95b0dd4cf8a8a72"},
    "title":"movie2",
    "year":2022,
    "rated":"3.5",
    "director":"director2",
    "actors":["actor1","actor2"]
    "imdb":{
        "imdb_id":"",
        "rating":"",
        "votes":""
    }
}
'''
class Movie(db.Document):
    '''## movie model that contains title and stars'''
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField(default="0")
    director = db.StringField()
    actors = db.ListField()
    imdb = db.EmbeddedDocumentField(Imdb)

    def __str__(self):
        return self.title




# Routes CRUD - Create Read Update Delete

@app.route('/') # route (endpoints)
def hello():
    return "Hello world"

@app.route('/movie/')
def get_all_movies():
    # movies = Movie.filter(title="movie2") # get movies with filter
    movies = Movie.objects() # get all the movies
    print(movies)
    # movies = movies.filter(title="movie1") # there is another way
    # movies = movies.filter(title__icontains="movie") # there is another way also check the link https://docs.mongoengine.org/guide/querying.html for more filter options
    return jsonify(movies)

@app.route('/movie/<id>/')
def get_all_movie_with_id(id):
    '''
        access instance using its ID(UNIQUE)
    '''
    movie = Movie.objects.get(id=id)
    return jsonify(movie)

@app.route('/movie/create/')
def create_movie():
    '''
        add object in the document
    '''
    movie = Movie(
        title="Movie1",
        year=2021,
        rated="3.5",
        director="director",
        actors=["actor1", "actor2"]
    )
    
    # movie=Movie(title="Movie1") # creating a new object/instance
    # movie.year = 2022
    # movie.rated="3.5"
    director_name = "director2"
    movie.director=director_name
    movie.actors=["actor1", "actor2"]
    movie.save()
    return jsonify(movie)

@app.route('/movie/create_/', methods=["GET", "POST"])
def create_movie_2():
    print(request)
    print(request.method)
    print(request.host)
    
    # get the data using any of the allowed requests
    print(request.args, "args")
    print(request.get_json(), "get json")
    print(request.from_values(), "from values")
    print(request.values)
    
    data = request.get_json()
    # logic for data validation
    # print(data['title'],data['year']) way to access data 
    movie = Movie(**data)
    # more logics here ..
    
    
    # print(movie.title)
    # print(movie.year)
    movie.save()
    
    return jsonify(movie)



@app.route('/movie/change/<id>/')
def update_movie(id):
    # ORM  Object Relational Mapper
    movie = Movie.objects.get(id=id)  # retriving any one object
    movie.title = "new movie title"
    movie.save() # save the changes of object
    return jsonify(movie)

@app.route('/movie/delete/<id>/')
def delete_movie(id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return f"object with id {id} deleted successful "

@app.route('/imdb/add/<id>/')
def imdb(id):
    movie = Movie.objects.get(id=id)
    movie.imdb = Imdb(imdb_id="23847y2i8yh23", rating=2.4, votes=6)
    movie.save()
    return jsonify(movie) 
    


@app.route('/<first_name>/') # route (endpoints)
def greet(first_name):
    return jsonify(first_name=first_name)



