from tracker import app 
from tracker import db 
from tracker import  bcrypte 
from tracker import  login_manager
from datetime import datetime
from flask_login import UserMixin 
# from sqlalchemy import 
# -------------------This is essential for flask-login to work properly
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model ,UserMixin):
    id = db.Column(db.Integer() , primary_key = True)# it was called user_id, but load_user() calls the id attribute from the User class, and not the  user_id attribute
    user_name = db.Column(db.String(length = 20) , nullable = False , unique = True)
    email = db.Column(db.String() , nullable = False , unique = True)
    password = db.Column(db.String(length = 100) , nullable = False )
    balances = db.relationship('Balance', backref = 'owner' , lazy = True) # different balances for diffrent months
    # WE Will need to hash the password for security reasons

    # Getter
    @property
    def get_password(self):
        return self.get_password
    # Setter
    @get_password.setter
    def get_password(self , plain_text_password):
        self.password =  bcrypte.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self , attempted_password):
        return bcrypte.check_password_hash(self.password ,attempted_password) # returns True if they are equal



class Category(db.Model):
    category_id = db.Column(db.Integer() , primary_key = True)
    category_name = db.Column(db.String() , nullable = False , unique = True)
    items = db.relationship('Item' , backref = 'item-category' , lazy = True)

class Balance(db.Model):
    id = db.Column(db.Integer() , primary_key = True)
    amount = db.Column(db.Integer() , nullable = True)
    period = db.Column(db.String(length = 30) , nullable = False , unique = True) 
    user_id = db.Column(db.Integer() , db.ForeignKey('user.id'))

class Item(db.Model):
    item_id = db.Column(db.Integer() , primary_key = True)
    item_name = db.Column(db.String(length = 50) , nullable = False , unique = True)
    item_category = db.Column(db.String() , db.ForeignKey('category.category_id'))
    amount = db.Column(db.Integer)  

# This is how we converted the classes into db tables and connected them to the db file. but we needed to run this 
# file `dbmodels.py` seperately in order to do so.
with app.app_context():
    db.create_all()
    db.session.commit()