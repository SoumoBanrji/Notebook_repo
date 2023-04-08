from flask import Blueprint

# defining blueprint for auth
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>this is login page</p>"

@auth.route('/logout')
def logout():
    return "<p>this is logout page</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>this is sign-up page</p>"

