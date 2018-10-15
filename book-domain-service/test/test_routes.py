import pytest

from .conftest import client, init_test_database

def test_checkout_book_returns_200_given_book_exist(client, init_test_database):

    response = client.put('/1/checkout')
    assert response.data == "I wish we had that book! Try another"
    assert response.status_code == 200
