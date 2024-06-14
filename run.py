"""I do not know if this file will be used or not. If yes, in what ? """

from tracker import create_app
from tracker.dbmodels import db

app = create_app()
  # Update database
with app.app_context(): 
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)