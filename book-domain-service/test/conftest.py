import pytest
from config import Config_Test
from app import create_app, db
from app.book import Book

@pytest.fixture()
def client():

    app = create_app(Config_Test)
    client = app.test_client()

    app_context = app.app_context()
    app_context.push()

    yield client
    
    app_context.pop()

@pytest.fixture()
def init_test_database():
    db.create_all()

    book_title = 'Test book'
    test_book = Book(title = book_title)
    db.session.add(test_book)
    db.session.commit()
    
    yield db

    db.drop_all()
