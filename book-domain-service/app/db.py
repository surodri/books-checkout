import sqlite3

from config import Config
from app import db
from app import app
from flask import g

def init_db(): 
    db = get_db()
    
    with app.open_resource(Config.SQLALCHEMY_DB, mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()

def get_db():

    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row
    return g.db


