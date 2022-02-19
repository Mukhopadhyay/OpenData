import pytest

@pytest.fixture
def files():
    return [
        ('nlp-datasets.json', 'json'),
        ('audio-datasets.json', 'json'),
        ('image-datasets.json', 'json'),
        ('open-gov-websites.csv', 'csv'),
        ('opendata-websites.json', 'json'),
        ('open-gov-additional.json', 'json')
    ]
