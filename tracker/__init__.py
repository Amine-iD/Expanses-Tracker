from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tracker import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes.bp)
    return app
app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db' 
db = SQLAlchemy(app)