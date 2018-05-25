from os import environ

import pandas as pd
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DB_ENGINE = create_engine('sqlite:///movies.db')
MOVIE_CSV_FILE_NAME = 'movie_metadata.csv'


def create_app():
    '''Create application.'''
    app = Flask(__name__)
    import_db(app)
    load_blueprints(app)
    return app


def import_db(app):
    '''Imports .csv of movie metadata to database'''
    declarative_base().metadata.create_all(DB_ENGINE)
    dataframe = pd.read_csv(MOVIE_CSV_FILE_NAME)
    try:
        dataframe.to_sql(con=DB_ENGINE, name='movies', if_exists='fail')
    except ValueError:
        pass


def load_blueprints(app):
    from app.endpoints import API

    app.register_blueprint(API)
