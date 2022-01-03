import os
import utils
import pytest
import pandas as pd

expected_files = (
    'audio-datasets.json',
    'image-datasets.json',
    'nlp-datasets.json',
    'open-government.json',
    'opendata-websites.json'
)

def test_data_files() -> None:
    data_dir_contents = os.listdir('data')
    for datafile in expected_files:
        assert datafile in data_dir_contents

def test_fetch_open_gov_csv() -> None:
    url = utils.OPEN_GOV_URLS
    assert isinstance(url, str)
    assert url.endswith('.csv')
    assert isinstance(utils.fetch_open_gov_csv(url), pd.DataFrame)

def test_process_open_gov_df() -> None:
    
    df = utils.process_open_gov_df(
        utils.fetch_open_gov_csv(utils.OPEN_GOV_URLS)
    )
    for col in ('Name', 'URL', 'Type'):
        assert col in df.columns
    for type in  df.Type.unique():
        assert type in ('International Regional', 'International Country', 'US City or County', 'US State', 'Other State Related')
