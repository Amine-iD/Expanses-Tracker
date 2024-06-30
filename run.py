"""I do not know if this file will be used or not. If yes, in what ? """

from tracker import create_app
from tracker.dbmodels import db

app = create_app()
  # Update database
    # db.session.close_all()

if __name__ == "__main__":
    with app.app_context(): 
      # db.drop_all()
      db.create_all()
      db.session.commit() 
    app.run(debug=True)