import sqlite3

from config import Config
from app import db
from app import app
from flask import g


def get_db(database_path):

    if 'db' not in g:
        g.db = sqlite3.connect(
            database_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def init_db( sql_file_path , database_path): 
    db = get_db(database_path)
 
    with app.open_resource( sql_file_path, mode='r') as file:
        db.cursor().executescript(file.read())
