from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user
from flask_security import login_required
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.secret_key = ';ajsgkasjgas;galsjg'

login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)


@login_manager.user_loader
def get_user(ident):
    return User.query.get(int(ident))


@app.route("/",  methods=['get', 'post'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            email=request.form['email'],
            password=request.form['password']).first()
        if user is None:
            flash('Неправильные логин или пароль')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('users'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users=users)
