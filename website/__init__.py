from flask import Flask

# defining flask app
def create_app():
    app = Flask(__name__)                          # initialising flask
    app.config['SECRET_KEY']  = 'hojoborolo'      # for encrypting and securing cookies and session data
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app