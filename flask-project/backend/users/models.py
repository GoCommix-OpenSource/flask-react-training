from .. import mongo as db
from . import bcrypt
# user = User.objects.first()
# user.password = "sdfklsjdf"  // wrong
# user.set_pasword("sdfklsjdf")    // right

class User(db.Document):
    username = db.StringField(required =True, unique=True)
    password = db.StringField(required =True)
    def set_password(self, password):
        # encrypts password and saves in database
        self.password = bcrypt.generate_password_hash(password)
        
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password, password)
    