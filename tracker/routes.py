from flask import Blueprint , render_template
from tracker.forms import Register
from tracker.dbmodels import User

bp = Blueprint('pages' , __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/register')
def register():
    form = Register() # This allows us to make conditions upon the redirected template 
    user_to_create = User(
        user_name = form.user_name,
    ) 
    return render_template('register.html' , form = form)
