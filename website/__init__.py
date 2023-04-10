from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "notebook_database.db"

# defining flask app
def create_app():
    # initialising flask
    app = Flask(__name__)

    # for encrypting and securing cookies and session data                        
    app.config['SECRET_KEY']  = 'hojoborolo'

    #  database initialising 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()




    return app

        
