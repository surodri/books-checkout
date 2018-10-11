import os
import tempfile
import pytest

from app import app
from app import routes
from app.db import init_db

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_checkout_book_returns_200_given_book_exist(client):

    response = client.get('/1/checkout/')
    assert response.status_code == 200
