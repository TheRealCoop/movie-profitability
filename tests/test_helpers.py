import json

import pandas as pd

from app import helpers as hp


def test_get_movie_df():
    df = hp.get_movie_df()
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 1 and df.shape[1] > 1


def test_compute_profit():
    headers = ['col1', 'gross', 'budget']
    rows = [['a', 10, 5], ['b', 10, 1], ['c', 0, 0]]
    df = _create_df(headers, rows)

    result = hp.compute_profit(df)
    assert result['profit'][0] == 5
    assert result['profit'][1] == 9
    assert result['profit'][2] == 0


def test_groupby():
    df = _create_df(['col1', 'profit'], [['a', 10], ['a', 10], ['c', 0]])

    result = hp.groupby(df, 'col1')
    assert result['profit'][0] == 20
    assert result['profit'][1] == 0


def test_desc_num_to_list():
    headers = ['col1', 'col2', 'profit']
    rows = [['a', 'x', 10], ['a', 'y', 100], ['c', 'z', 0]]
    df = _create_df(headers, rows)

    assert hp.desc_num_to_list(df, 'col2', 2) == ['y', 'x']


def test_combine_columns():
    headers = hp.ACTOR_COLUMNS + ['profit']
    rows = [['a', 'b', 'c', 10], ['d', 'e', 'f', 100]]
    df = _create_df(headers, rows)

    result = hp.combine_columns(df, 'new_actors')
    assert result['new_actors'].tolist() == ['a', 'd', 'b', 'e', 'c', 'f']
    assert result['profit'].tolist() == [10, 100, 10, 100, 10, 100]


def test_split_column():
    headers = ['col1', 'profit']
    rows = [['a|b', 10], ['c|d', 100]]
    df = _create_df(headers, rows)

    result = hp.split_column(df, 'col1', 'new_col_name')
    assert result['new_col_name'].tolist() == ['a', 'b', 'c', 'd']
    assert result['profit'].tolist() == [10, 10, 100, 100]


def _create_df(headers, rows):
    return pd.DataFrame(data=rows, columns=headers)
