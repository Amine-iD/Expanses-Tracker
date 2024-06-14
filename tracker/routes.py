from flask import Blueprint , render_template , redirect , url_for ,flash
from tracker.forms import Register , Login
from flask_login import login_user , logout_user , login_required
# from tracker.dbmodels import load_user --> This causes circular import ,so it is imported inside each route/function

bp = Blueprint('routes' , __name__)    
@bp.route('/')
@bp.route('/home')
def home():
    from tracker.dbmodels import load_user
    return render_template("home.html")

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/register',methods = ['GET' , 'POST'])
def register():
    from tracker.dbmodels import User
    from tracker import create_app , db
    app = create_app()
    form = Register() # This allows us to make conditions upon the redirected template 
    if form.validate_on_submit():
        user_to_create = User(
            user_name = form.user_name.data,
            email = form.email.data,
            get_password = form.password1.data)
        with app.app_context():
            db.session.add(user_to_create)
            db.session.commit()
            login_user(user_to_create)
        return redirect(url_for("routes.home"))
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
    from tracker import db , create_app
    app = create_app()
    form = Login()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user_name = form.user_name.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash("You are successfully logged in!",category='success')
            return redirect(url_for('routes.dashboard'))

        else:
            flash('Log in Error',category='danger')
        
        return redirect(url_for("routes.home"))    
    return render_template('login.html' , form = form )

@bp.route('/logout')
def logout():
    logout_user()
    flash("You are currently logged out")
    return render_template('home.html')

@bp.route('/add' , methods = ['GET' , 'POST'])
def add():
    from tracker.dbmodels import Category , Item
    from tracker.forms import AddCategory
    from tracker import create_app , db
    app = create_app()
    form = AddCategory()
    if form.validate_on_submit():
        created_category = Category(category_name = form.category_name.data)
        with app.app_context():
            db.session.add(created_category)
            db.session.commit()
            return redirect(url_for('routes.add'))
    if form.errors:
        for err in form.errors.values():
            flash(err)
    categories = [str(category) for category in  Category.query.all()]
    items =[str(item) for item in  Item.query.all()]
    
    return render_template('categories.html' , form = form , categories = categories , items = items)



