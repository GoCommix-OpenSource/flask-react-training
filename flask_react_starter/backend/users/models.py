from .. import mongo
from . import bcrypt
'''
primary_key=None
db_field=None,
required=False,
default=None,
unique=False,
unique_with=None,
choices=None
'''
class User(mongo.Document):
    username = mongo.StringField(required=True, unique=True)
    password = mongo.DynamicField(required=True)
    def set_password(self, password):
        self.password= bcrypt.generate_password_hash(password)
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

