import os
import json
import pytest
import requests
from os import path
import pandas as pd
import utils.utils as utils
import utils.config as config

def test_data_files() -> None:
    data_dir_contents = os.listdir('data')
    for datafile in config.EXPECTED_FILES:
        assert datafile in data_dir_contents

def test_fetch_open_gov_csv() -> None:
    url = config.OPEN_GOV_URLS
    assert isinstance(url, str)
    assert url.endswith('.csv')
    assert isinstance(utils.fetch_open_gov_csv(url), pd.DataFrame)

def test_process_open_gov_df() -> None:
    url = config.OPEN_GOV_URLS
    df = utils.process_open_gov_df(
        utils.fetch_open_gov_csv(url)
    )
    for col in ('Name', 'URL', 'Type'):
        assert col in df.columns
    for type in  df.Type.unique():
        assert type in ('International Regional', 'International Country', 'US City or County', 'US State', 'Other State Related')

def test_create_audio_markdown_table() -> None:
    aud_md = utils.create_audio_markdown_table()
    assert isinstance(aud_md, str)

def test_image_audio_markdown_table() -> None:
    img_md = utils.create_image_markdown_table()
    assert isinstance(img_md, str)

def test_create_nlp_markdown_table() -> None:
    nlp_md = utils.create_nlp_markdown_table()
    assert isinstance(nlp_md, str)

def test_create_openweb_markdown_table() -> None:
    openweb_md = utils.create_openweb_markdown_table()
    assert isinstance(openweb_md, str)

def test_urls() -> None:
    # Testing nlp links
    with open(path.join(config.DATA_DIR, config.NLP_DATASETS), 'r') as file:
        nlp = json.load(file)
        for link in nlp:
            r = requests.get(link.get('url'))
            assert r.status_code == 200
        