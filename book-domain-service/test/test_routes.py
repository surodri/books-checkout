import os
import tempfile
import pytest

from app import app
from app import routes
from app.db import init_db

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        test_data_file_path = os.path.join(root_dir(), 'test_books_data.sql')
        test_database_path = os.path.join(root_dir(), 'schema.db')

        init_db(test_data_file_path, test_database_path)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_checkout_book_returns_200_given_book_exist(client):

    response = client.get('/1/checkout/')
    assert response.status_code == 200
