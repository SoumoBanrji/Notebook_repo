from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# defining blueprint for auth
auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>this is logout page</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('FirstName')
        last_name = request.form.get('LastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 6:
            flash('email must be greater than 5 charecters', category='error')
            pass
        elif len(first_name) < 2:
            flash('First name must be greater than 1 charecter', category='error')
            pass
        elif len(last_name) < 2 :
            flash('Last name must be greater than 1 charecter', category='error')
            pass
        elif password1 != password2:
            flash('Password do not match', category='error')
            pass
        elif len(password1) < 8:
            flash('Password must be atleast 8 charecters', category='error')
            pass
        else:
            new_user = User(first_name=first_name,last_name=last_name,email=email, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!',category='success')
            return redirect(url_for('views.home'))
            




    return render_template("sign_up.html")

