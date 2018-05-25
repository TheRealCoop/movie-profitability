from decorator import decorator
from flask import jsonify
import pandas as pd

from app import DB_ENGINE


ACTOR_COLUMNS = ['actor_1_name', 'actor_2_name', 'actor_3_name']
MEASUREMENT = 'profit'


@decorator
def serialize(func, *args, **kwargs):
    '''Converts the result of the passed function's result to be nested
    within a `result` key in a new dictionary and JSONified.'''
    return jsonify({'result': func(*args, **kwargs)})


def get_movie_df():
    '''Retrieves the movie table in the database and returns as dataframe'''
    return pd.read_sql('SELECT * FROM movies', DB_ENGINE, index_col='index')


def compute_profit(dataframe):
    '''Takes dataframe and computes net profit by doing `gross` - `budget`.
    Returns as dataframe'''
    dataframe['profit'] = dataframe['gross'] - dataframe['budget']
    return dataframe


def groupby(dataframe, grouped_column):
    '''Takes a dataframe and sums the column MEASUREMENT in order to group
    the `grouped_column. Returns a dataframe'''
    return dataframe.groupby([grouped_column])[MEASUREMENT].sum()\
                    .to_frame()\
                    .reset_index()


def desc_num_to_list(dataframe, column, num):
    '''Sorts descending passed `dataframe` based on MEASUREMENT.
    Returns list of top `num` values in `column`.'''
    dataframe.sort_values(MEASUREMENT, ascending=False, inplace=True)
    return dataframe[column][:num].tolist()


def combine_columns(dataframe, new_col_name):
    '''Takes a `dataframe`, combines all the columns in ACTOR_COLUMNS into a
    `new_col_name` with the MEASUREMENT's original values'''
    new_df = pd.DataFrame([], columns=[new_col_name, MEASUREMENT])

    for col_name in ACTOR_COLUMNS:
        renamed_df = dataframe[[col_name, MEASUREMENT]]\
            .rename({col_name: new_col_name}, axis='columns')
        new_df = new_df.append(renamed_df, ignore_index=True)

    return new_df


def split_column(dataframe, column, new_column_name):
    '''Takes a `dataframe` along with a specific `column` that is to be split
    out by a pip. Returns dataframe with `new_column_name` replacing
    `column` with the values split out over multiple rows.'''
    new_df = dataframe[column].str.split('|').apply(pd.Series, 1).stack()
    new_df.index = new_df.index.droplevel(-1)
    new_df.name = new_column_name
    del dataframe[column]
    return dataframe.join(new_df)
