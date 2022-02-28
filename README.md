# Flask React training

## ***1. Flask installation, environment setup and more***
### virtual env managers
anaconda\
virtualenv\
poertry\
pipenv <-- we are using this

### ***create new virtualenv using pip env***
```python
pipenv install
```

### ***Activate virtual env***
```python
pipenv shell
```


### ***install package(s) in virtualenv***
```python
# using pip
pipenv shell
pip instll <package-name>
pip install -r requirements.txt
```
```python
# using pipenv
pipenv install <package_name>
```
Finally, if you want to use `Pipenv` to manage a project that currently uses a `requirements.txt` file, just navigate to the project’s directory and run `pipenv install`. Pipenv will detect the `requirements.txt` (or you can use the `-r` flag to point to it) and migrate all of the requirements into a `Pipfile`.
### ***export dependencies ito file***
```
pip freeze
pip freeze > requirements.txt
```
### ***deactivate virtualenv***
```
deactivate
```
### ***You can run application in virtual env without actually activating it***
```
pipenv run python flask_app/app.py
```

### ***Python decorators***
search online and learn about the concept

## ***Introduction to Git***
![alt text](https://github.com/GoCommix-OpenSource/flask-react-training/blob/main/git%20commands.png?raw=true)



## ***3. MongoDB with flask and flask_mongoengine***

***MongoEngine provides several types of documents classes:***

    1. Document
    2. EmbeddedDocument
    3. DynamicDocument
    4. DynamicEmbeddedDocument


### ***1. Document***
This represents a document that has it's own collection in the database, it is created by
inheriting from `mongoengine.Document` or from our MongoEngine instance (`db.Document`)

### ***2. EmbeddedDocument***
This represents a document that doesn't have it's own collection in the database but is
embedded into another document, it is created by inheriting from `db.EmbeddedDocument` class
### ***3. DynamicDocument***
This is a document whose fields are added dynamically, taking advantage of the dynamic nature
of MongoDB.
Like the other document types, MongoEngine provides a class for `db.DynamicDocuments`:
### ***4. DynamicEmbeddedDocument***
This has all the properties of DynamicDocument and EmbeddedDocument, Like the other document types, MongoEngine provides a class for `db.DynamicEmbeddedDocuments`:
Also…..

MongoEngine also provides additional classes that describe and validate the type of data a document's fields should take and optional modifiers to add more details or constraints to each field.

#### ***Examples of fields are:***
```python 
StringField() #for string values
IntField() #for int values
ListField() #for a list
FloatField() #for floating point values
ReferenceField() #for referencing other documents
EmbeddedDocumentField() #for embedded documents etc.
FileField() #for storing files (more on this later)

'''
example:
username=StringField()
'''
```
#### You can also apply modifiers in these fields, such as:
```python
-required
-default
-unique
-primary_key etc.
'''
example: 
StringField(required =True)
IntegerField(required =True, unique=True, primary_key=True)
'''
# By setting any of these to True, they'll be applied to that field specifically.
```







# Some Topics to Discover
1. Python Decorators
2. MVC project model (Model View Controller)
3. POSTMAN or any REST api test-client
4. gitignore
5. Packaging
6. flask blueprint
7. JWT

# Some important links
### Queries and mutation guide and examples
1. [flask-doc](https://docs.mongoengine.org/guide/document-instances.html)
2. [queries](https://docs.mongoengine.org/guide/querying.html)
3. [mongoengine](https://flask.palletsprojects.com/en/2.0.x/patterns/mongoengine/)
4. [status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

5. [flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/stable/)