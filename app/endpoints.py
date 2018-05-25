from flask import Blueprint

from app import helpers as hp


API = Blueprint('api', __name__, url_prefix='/api')


@API.route('/genres', methods=['GET'])
@hp.serialize
def genres():
    df = hp.compute_profit(hp.get_movie_df())
    df = hp.split_column(df, 'genres', 'genre')
    df = hp.groupby(df, 'genre')
    return hp.desc_num_to_list(df, 'genre', 10)


@API.route('/actors', methods=['GET'])
@hp.serialize
def actors():
    df = hp.compute_profit(hp.get_movie_df())
    df = hp.combine_columns(df, 'actor_name')
    df = hp.groupby(df, 'actor_name')
    return hp.desc_num_to_list(df, 'actor_name', 10)


@API.route('/directors', methods=['GET'])
@hp.serialize
def directors():
    df = hp.compute_profit(hp.get_movie_df())
    df = hp.groupby(df, 'director_name')
    return hp.desc_num_to_list(df, 'director_name', 10)
