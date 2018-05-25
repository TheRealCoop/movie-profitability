from os import environ

from pytest import fixture

from app import DB_ENGINE, create_app


@fixture()
def app():
    environ['FLASK_ENV'] = 'test'
    return create_app()
