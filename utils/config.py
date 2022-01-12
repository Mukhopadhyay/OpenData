OPEN_GOV_URLS: str = 'https://s3.amazonaws.com/bsp-ocsit-prod-east-appdata/datagov/wordpress/2019/09/opendatasites91819.csv'

# Files and directories
DATA_DIR: str = 'data'
NLP_DATASETS: str = 'nlp-datasets.json'
AUDIO_DATASETS: str = 'audio-datasets.json'
IMAGE_DATASETS: str = 'image-datasets.json'
OPEN_GOV_WEBSITES: str = 'open-gov-websites.csv'
OPEN_DATA_WEBSITES: str = 'opendata-websites.json'
OPEN_GOV_ADDITIONAL: str = 'open-gov-additional.json'

# Expected files
EXPECTED_FILES = (
    NLP_DATASETS,
    AUDIO_DATASETS,
    IMAGE_DATASETS,
    OPEN_GOV_WEBSITES,
    OPEN_DATA_WEBSITES,
    OPEN_GOV_ADDITIONAL
)

README_TEMPLATE: str = '''
<div align='center'>
    <h1>Open Data ❤️</h1>
</div>

<div align='center'>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](https://forthebadge.com)

</div>
<br/><br/>

<div align='center'>
<div style="width: 500px">

> **Open Data** is the idea that some data should be freely available
> to everyone to use and republish as they wish, without restrictions
> from copyright, patents or other mechanisms of control.
> <cite>[Wikipedia](https://en.wikipedia.org/wiki/Open_data)</cite>

</div>
</div>

<br/>

## Index
- [Index](#index)
- [OpenData Websites](#opendata-websites)
- [Image Datasets](#image-datasets)
- [NLP Datasets](#nlp-datasets)
- [Audio Datasets](#audio-datasets)
- [Open Government Sites](#open-government-sites)

---
'''