from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import LoginForm, SignupForm



from . import auth
from app.models import UserModel, UserData
from app.db import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = db.session.execute(f"SELECT * FROM users WHERE username = '{username}';").fetchone()

        if user_doc is not None:
            password_from_db = user_doc.password

            if check_password_hash(password_from_db, password):
                user_data = UserData(username, password, user_doc.usertype)
                user = UserModel(user_data)

                login_user(user)

                flash('Bienvenido de nuevo')

                redirect(url_for('hello'))
            else:
                flash('La informaición no coincide')
        else:
            flash('El usario no existe')

        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        usertype = signup_form.usertype.data

        user_doc = db.session.execute(f"SELECT * FROM users WHERE username = '{username}';").fetchone()

        if user_doc is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash, usertype)

            user = db.session.execute(f"INSERT INTO users (username, password, usertype) VALUES ('{username}', '{password_hash}', '{usertype}');")
            user = db.session.commit()

            user = UserModel(user_data)
    
            login_user(user)

            flash('Bienvenido!')

            return redirect(url_for('hello'))

        else:
            flash('El usario existe!')

    return render_template('signup.html', **context)


@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))
