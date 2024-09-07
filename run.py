"""
This is where to run the application
"""
from tracker import create_app
from tracker.dbmodels import db
from flask_migrate import Migrate

app = create_app()
  # Update database
migrate = Migrate(app , db)
    # db.session.close_all()
if __name__ == "__main__":
    # with app.app_context(): 
      # db.drop_all()         
      # db.create_all()                                
      # db.session.commit() 
    app.run(debug=True)
