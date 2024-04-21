from tracker import db 
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer() , primary_key = True)
    user_name = db.Column(db.String(length = 20) , nullable = False , unique = True)
    balances = db.relationship('Balance', backref = 'author' , lazy = True)

class Category(db.Model):
    category_id = db.Column(db.Integer() , primary_key = True)
    category_name = db.Column(db.String() , nullable = False , unique = True)

class Balance(db.Model):
    amount = db.Column(db.Integer() , nullable = True)
    period = db.Column(db.String(length = 30) , nullable = False , unique = True) 
    user_id = db.Column(db.Integer() , db.ForeignerKey('User.user_id')) 
