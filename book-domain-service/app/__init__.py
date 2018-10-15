from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, Config_Test

db = SQLAlchemy()

def create_app(config_objectname=None):
    
    app = Flask(__name__)
    app.config.from_object(config_objectname)
    db.init_app(app)

    return app
