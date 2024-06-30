import os
from flask import Flask , current_app
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
# from flask_migrate import Migrate
from tracker.routes import bp
from flask_bcrypt import Bcrypt as Bcr
from flask_login import LoginManager , login_user
from dotenv import load_dotenv


db = SQLAlchemy()
bcrypte = Bcr()
login_manager = LoginManager()

load_dotenv(rf'C:\Users\amine\to unpack\WebDev\Expanses-Tracker\.env')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    bcrypte.init_app(app)
    login_manager.init_app(app)
    app.config.from_prefixed_env()
    # app.config.from_prefixed_env('SQLALCHEMY')
    # os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app) 
    return app
"""
This is how To delete data from the database:
with app.app_context():
...     toDel = Category.query.filter_by(category_name = 'Test').first()
...     db.session.delete(toDel)
...     db.session.commit()
"""

