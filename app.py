"""  I do not know if this file will be used or not . If yes, in what ?   """
from flask import Flask
import tracker.pages as pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)