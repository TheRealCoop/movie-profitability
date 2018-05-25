import json
from flask import url_for


HEADERS = {'Content-Type': 'application/json'}


def test_get_genres(client):
    response = get(client, 'api.genres')
    assert response.status_code == 200
    assert not response.json['success']


def test_get_actors(client):
    response = get(client, 'api.actors')
    assert response.status_code == 200
    assert response.json['success']


def test_get_directors(client):
    response = get(client, 'api.directors')
    assert response.status_code == 200
    assert response.json['success'] == 'opah'


def get(client, endpoint, **kwargs):
    return client.get(url_for(endpoint, **kwargs))
