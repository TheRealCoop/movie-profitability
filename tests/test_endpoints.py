import json
from flask import url_for


HEADERS = {'Content-Type': 'application/json'}


def test_get_genres(client):
    response = get(client, 'api.genres')
    _assert_response(response)


def test_get_actors(client):
    response = get(client, 'api.actors')
    _assert_response(response)


def test_get_directors(client):
    response = get(client, 'api.directors')
    _assert_response(response)


def get(client, endpoint, **kwargs):
    return client.get(url_for(endpoint, **kwargs))


def _assert_response(response):
    result = response.json['result']
    assert response.status_code == 200
    assert len(set(result)) == 10
    assert isinstance(result, list)
