import pytest

from .conftest import client, init_test_database

def test_checkout_book_returns_200_given_book_exist(client, init_test_database):
 
    response = client.put('/1/checkout')

    assert b'You checked out book id: 1, name: Test title BLAH' in response.data
    assert response.status_code == 200

def test_addbook_returns_200_given_book_exists(client, init_test_database):

    response = client.post('/addbook', json={ 'title': 'Test new book'})

    assert b'Test new book' in  response.data

