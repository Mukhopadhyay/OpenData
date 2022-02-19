import os
import json
import pytest
import asyncio
import aiohttp
import warnings
from os import path
import pandas as pd
import utils.utils as utils
import utils.config as config

warnings.filterwarnings('ignore')

@pytest.mark.files
def test_data_files() -> None:
    data_dir_contents = os.listdir('data')
    for datafile in config.EXPECTED_FILES:
        assert datafile in data_dir_contents


@pytest.mark.files
def test_data_file_integrity(files) -> None:
    for file, ext in files:
        if ext == 'json':
            with open(path.join('data', file), 'r') as f:
                assert isinstance(json.load(f), list)
        elif ext == 'csv':
            assert isinstance(pd.read_csv(path.join('data', file)), pd.DataFrame)


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
    """
    For now considering the followng status code
    
    200: The HTTP 200 OK success status response code indicates that the request has succeeded
    403: The HTTP 403 Forbidden response status code indicates that the server understands the request but refuses to authorize it.
    """
    async with session.get(url) as response:
        assert response.status in [200, 403]
        result = await response.text(), response.status, url
        return result


async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result


async def call_urls(urls: list, verbose: str):
    async with aiohttp.ClientSession() as session:
        results = await fetch_all(session, urls)
        print(verbose)
        for _, code, url in results:
            print(f'\t\t{url} ({code})')


@pytest.mark.urls
@pytest.mark.xfail
def test_audio_urls():
    with open(path.join(config.DATA_DIR, config.AUDIO_DATASETS), 'r') as file:
        content = json.load(file)
        urls = [_['url'] for _ in content]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_urls(urls, f'\n\t{"*"*40}\n\t AUDIO URLS\n\t{"*"*40}'))


@pytest.mark.urls
@pytest.mark.xfail
def test_image_urls():
    with open(path.join(config.DATA_DIR, config.IMAGE_DATASETS), 'r') as file:
        content = json.load(file)
        urls = [_['url'] for _ in content]
        
    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_urls(urls, f'\n\t{"*"*40}\n\t IMAGE URLS\n\t{"*"*40}'))


@pytest.mark.urls
@pytest.mark.xfail
def test_nlp_urls():
    with open(path.join(config.DATA_DIR, config.NLP_DATASETS), 'r') as file:
        content = json.load(file)
        urls = [_['url'] for _ in content]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_urls(urls, f'\n\t{"*"*40}\n\t NLP URLS\n\t{"*"*40}'))


@pytest.mark.urls
@pytest.mark.xfail
def test_open_gov_additional_urls():
    with open(path.join(config.DATA_DIR, config.OPEN_GOV_ADDITIONAL), 'r') as file:
        content = json.load(file)
        urls = [_['url'] for _ in content]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_urls(urls, f'\n\t{"*"*40}\n\t OPEN-GOV ADDITIONAL URLS\n\t{"*"*40}'))


@pytest.mark.urls
@pytest.mark.xfail
def test_opendata_web_urls():
    with open(path.join(config.DATA_DIR, config.OPEN_DATA_WEBSITES), 'r') as file:
        content = json.load(file)
        urls = [_['url'] for _ in content]
        
    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_urls(urls, f'\n\t{"*"*40}\n\t OPENDATA-WEB URLS\n\t{"*"*40}'))

