from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from config_test import Config_Test

db = SQLAlchemy()

def create_app(config_object=None):
    
    app = Flask(__name__)
    app.config.from_object(config_object)

    from .routes import checkout_blueprint
    app.register_blueprint(checkout_blueprint)

    db.init_app(app)

    return app
