import pytest

def test_checkout(client, app):
    assert client.get('/1/update').status_code == 200
