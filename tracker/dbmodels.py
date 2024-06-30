from tracker import create_app, db, bcrypte, login_manager
from datetime import datetime
from flask_login import UserMixin 
from datetime import datetime
# from sqlalchemy import 
# -------------------This is essential for flask-login to work properly

app = create_app()
with app.app_context():
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


class User(db.Model ,UserMixin):
    """I will try to implement the UserMixin properties manually without inheriting them"""
    id = db.Column(db.Integer() , primary_key = True)# it was called user_id, but load_user() calls the id attribute from the User class, and not the  user_id attribute
    user_name = db.Column(db.String(length = 20) , nullable = False , unique = False)
    email = db.Column(db.String() , nullable = False , unique = True)
    password = db.Column(db.String(length = 100) , nullable = False , unique = False )
    balances = db.relationship('Balance', backref = 'owner' , lazy = True) # different balances for diffrent months

    def __repr__(self) -> str:
        return self.user_name #This is what displays the real value of the class User , if it's not written , all we get is <User 1or2>
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

class Balance(db.Model):
    id = db.Column(db.Integer() , primary_key = True)
    amount = db.Column(db.Integer() , nullable = True)
    period = db.Column(db.String(length = 30) , nullable = False , unique = True) 
    user_id = db.Column(db.Integer() , db.ForeignKey('user.id'))

class Category(db.Model):
    category_id = db.Column(db.Integer() , primary_key = True)
    category_name = db.Column(db.String() , nullable = False , unique = True)
    items = db.relationship('Item' , backref = 'item-category' , lazy = True)
    def __repr__(self) -> str:
        return f'{self.category_name}'

class Item(db.Model):
    item_id = db.Column(db.Integer() , primary_key = True)
    item_name = db.Column(db.String(length = 50) , nullable = False , unique = True)
    item_category = db.Column(db.String() , db.ForeignKey('category.category_id'))
    amount = db.Column(db.Integer()) 
    created_at = db.Column(db.DateTime, default=datetime.now())

class Service(db.Model):
    __tablename__ = 'service'

    service_id = db.Column(db.Integer() , primary_key = True)
    service_name = db.Column(db.String() , nullable = False , unique = True)


# This is how we converted the classes into db tables and connected them to the db file. but we needed to run this 
# file `dbmodels.py` seperately in order to do so.
with app.app_context():
    db.create_all()
    db.session.commit()

# I will make items a little bit general , like sugars , veges, fruits etc...
# And I will add a description to each purchase/Xpanse to describe it specifically