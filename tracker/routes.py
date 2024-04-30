from flask import Blueprint , render_template , redirect , url_for ,flash
from tracker.forms import Register
# from tracker.dbmodels import User

bp = Blueprint('pages' , __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/register',methods = ['GET' , 'POST'])
def register():
    from tracker.dbmodels import User
    from tracker import app , db
    form = Register() # This allows us to make conditions upon the redirected template 
    if form.validate_on_submit():
        user_to_create = User(
            user_name = form.user_name.data,
            email = form.email.data,
            get_password = form.password1.data)
        with app.app_context():
            db.session.add(user_to_create)
            db.session.commit()
        return redirect(url_for("pages.home"))
    # We need to check if the user entered the data in the correct way as it was mentioned in the validators
    if form.errors:
        for err in form.errors.values():
            flash(f'There was an error with creating the user :{err}' ,'danger')
    # We need to check if the email or the username entered is unique 
        # And this was done in the forms.py inside the login form class

    return render_template('register.html' , form = form)
