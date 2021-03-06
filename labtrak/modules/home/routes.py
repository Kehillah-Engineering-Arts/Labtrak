from . import controllers
from flask import render_template, redirect, url_for, flash
from flask import session, request
from flask import Blueprint

import random

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('/')
def index():
    image = random.choice([
        'http://i.imgur.com/2DEhzOG.jpg',
        'http://i.imgur.com/GpZbMD7.jpg',
        'http://i.imgur.com/hBSjwrk.jpg'
    ])
    return render_template('home.html', session=session, image=image)


@home_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Register the user."""
    if session.get('user'):
        return redirect(url_for('home.index'))
    error = None
    if request.method == 'POST':
        error = controllers.signup(
            request.form['username'],
            request.form['email'],
            request.form['password'],
            request.form['password2'],
            request.form['firstname'],
            request.form['lastname']
        )
        if not error:
            flash('You were successfully registered and can login now')
            return redirect(url_for('home.login'))
    return render_template('register.html', error=error)



@home_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if session.get('user'):
        return redirect(url_for('home.index'))
    error = None
    if request.method == 'POST':
        user = controllers.authenticate_user(request.form['username'], request.form['password'])
        if user:
            flash('Welcome back, %s' % user['firstname'])
            session['user'] = user
            return redirect(url_for('home.index'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error, session=session)



@home_bp.route('/logout')
def logout(msg='You were logged out'):
    """Logs the user out."""
    flash(msg)
    session.clear()
    return redirect(url_for('home.index'))
