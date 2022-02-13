import os
import json
import pytest
import asyncio
import aiohttp
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


###################################
# Testing the validity of the url # 
###################################

async def fetch(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        result = await response.text(), response.status, url
        return result

async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result

async def image_urls():
    with open(path.join(config.DATA_DIR, config.IMAGE_DATASETS), 'r') as file:
        content = json.load(file)
        urls = [_['url'] for _ in content]

    async with aiohttp.ClientSession() as session:
        results = await fetch_all(session, urls)
        print('\n\t', '*'*40, '\n\t Image URLS\n\t', '*'*40)
        for _, code, url in results:
            print(f'\t\t{url} ({code})')

def test_image_urls():
    asyncio.run(image_urls())
