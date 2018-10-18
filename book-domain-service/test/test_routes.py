import pytest

from .conftest import client, init_test_database

def test_checkout_returns_200_given_book_exist(client, init_test_database):
 
    response = client.put('/1/checkout')

    assert b'You checked out book id: 1, name: Test book' in response.data
    assert response.status_code == 200

def test_checkout_returns_404_given_book_not_exist(client, init_test_database):

    response = client.put('/400/checkout')

    assert b'I wish we had that book! Try another' in response.data
    assert response.status_code == 404

def test_addbook_returns_200_given_new_book(client, init_test_database):

    response = client.post('/addbook', json={ 'title': 'Test new book'})

    assert b'Test new book' in response.data
    assert response.status_code == 200

def test_addbook_returns_400_given_book_exists(client, init_test_database):

    client.post('/addbook', json={ 'title': 'Existing test book'})

    response = client.post('/addbook', json={ 'title': 'Existing test book'})

    assert b'This book already exists! Titles must be unique' in response.data
    assert response.status_code == 400
