import pytest

from .conftest import init_test_database
from app.book import Book

def test_to_json_returns_book_in_json_given_new_book():
    
    new_book = Book(title = 'Spanking new test book')

    assert new_book.to_json().get('title') == 'Spanking new test book'

def test_from_json_return_book():
    
    with pytest.raises(ValueError, match='Please provide a title'):
        Book.from_json({ } )
