"""  I do not know if this file will be used or not . If yes, in what ?   """

from tracker import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)