from flask import Blueprint , render_template , redirect , url_for ,flash
from tracker.forms import Register , Login
# from tracker.dbmodels import User
from flask_login import login_user

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
            flash(f'There was an error with creating the user :{err}' ,category='danger')
    # We need to check if the email or the username entered is unique 
        # And this was done in the forms.py inside the login form class

    return render_template('register.html' , form = form)
 
@bp.route('/login' , methods = ['GET', 'POST'])
def login():
    # These imports are here to avoid circular imports problem
    from tracker.dbmodels import User 
    from tracker import db , app
    form = Login()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user_name = form.user_name.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash("You are successfully logged in!",category='success')
            flash(attempted_user.password)
            return redirect(url_for('pages.home'))

        else:
            flash('Log in Error',category='danger')
        
        return redirect(url_for("pages.about"))    
    return render_template('login.html' , form = form)







"""
need to SOLVE THE USER() ID ATTRIBUTE (MEANING COLUMN) , AND FOR THAT I NEED TO SOLVE THE IMPORT TRACKER ISSUE !!
"""