from flask import Flask , current_app
from flask_sqlalchemy import SQLAlchemy
from tracker.routes import bp
from flask_bcrypt import Bcrypt as Bcr

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app

app = create_app()
bcrypte = Bcr(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db' 
app.config['SECRET_KEY'] = 'b9212131a5fe1e1345346de59f1cab71c17941e23fb166dc52ba162a3ca78c2e'
db = SQLAlchemy(app)