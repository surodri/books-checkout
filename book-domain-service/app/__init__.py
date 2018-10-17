from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from config_test import Config_Test

db = SQLAlchemy()

def create_app(config_object=None):
    
    app = Flask(__name__)
    app.config.from_object(config_object)
    config_object.init_app(app)

    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes import checkout_blueprint
    app.register_blueprint(checkout_blueprint)
    

    return app
