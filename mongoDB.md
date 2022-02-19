***MongoEngine provides several types of documents classes:***

#### . Document
#### . EmbeddedDocument
#### . DynamicDocument
#### . DynamicEmbeddedDocument


### 1. Document
This represents a document that has it's own collection in the database, it is created by
inheriting from `mongoengine.Document` or from our MongoEngine instance (`db.Document`)

### 2. EmbeddedDocument
This represents a document that doesn't have it's own collection in the database but is
embedded into another document, it is created by inheriting from `db.EmbeddedDocument` class
### 3. DynamicDocument
This is a document whose fields are added dynamically, taking advantage of the dynamic nature
of MongoDB.
Like the other document types, MongoEngine provides a class for `db.DynamicDocuments`:
### 4. DynamicEmbeddedDocument
This has all the properties of DynamicDocument and EmbeddedDocument, Like the other document types, MongoEngine provides a class for `db.DynamicEmbeddedDocuments`:
Also…..

***MongoEngine also provides additional classes that describe and validate the type of data a document's fields should take and optional modifiers to add more details or constraints to each field.***

#### Examples of fields are:
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






# Queries and mutation guide
1. https://docs.mongoengine.org/guide/document-instances.html
2. https://docs.mongoengine.org/guide/querying.html
3. https://flask.palletsprojects.com/en/2.0.x/patterns/mongoengine/


