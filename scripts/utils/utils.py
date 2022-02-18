import json
import utils.config as config
import pandas as pd
from os import path

def fetch_open_gov_csv(url: str) -> pd.DataFrame:
    return pd.read_csv(url, encoding='unicode_escape')


def process_open_gov_df(df: pd.DataFrame) -> pd.DataFrame:
    cols = ['Name', 'URL', 'Type']
    row0 = df.columns
    # DF without the first entry
    df.columns = cols
    # DF of shape (1,3)
    x = pd.DataFrame(row0).T
    x.columns = cols
    # Final dataframe
    final = pd.concat([x, df])
    # acceptable types
    acceptable_types = [
        'International Regional',
        'International Country',
        'US City or County',
        'US State',
        'Other State Related'
    ]
    final = final[final.Type.isin(acceptable_types)]
    final.URL = final.URL.apply(lambda x: x.strip())
    final = final[~final.URL.str.contains(' ')]
    return final


def create_audio_markdown_table() -> str:
    with open(path.join(config.DATA_DIR, config.AUDIO_DATASETS), 'r') as file:
        audio = json.load(file)

    audio = sorted(audio, key=lambda x: x['name'])
    strings = []

    for row in audio:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            strings.append(string)

    string = '''
|Name|Description|URL|
|:---|:----------|:--|\n''' +  '\n'.join(strings)
    return string


def create_image_markdown_table() -> str:
    with open(path.join(config.DATA_DIR, config.IMAGE_DATASETS), 'r') as file:
        image = json.load(file)

    image = sorted(image, key=lambda x: x['name'])
    strings = []

    for row in image:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            strings.append(string)

    string = '''
|Name|Description|URL|
|:---|:----------|:--|\n''' +  '\n'.join(strings)
    return string


def create_nlp_markdown_table() -> str:
    with open(path.join(config.DATA_DIR, config.NLP_DATASETS), 'r') as file:
        nlp = json.load(file)

    nlp = sorted(nlp, key=lambda x: x['name'])
    strings = []

    for row in nlp:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            strings.append(string)

    string = '''
|Name|Description|URL|
|:---|:----------|:--|\n''' +  '\n'.join(strings)
    return string


def create_openweb_markdown_table() -> str:
    with open(path.join(config.DATA_DIR, config.OPEN_DATA_WEBSITES), 'r') as file:
        nlp = json.load(file)

    nlp = sorted(nlp, key=lambda x: x['name'])
    strings = []

    for row in nlp:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            strings.append(string)

    string = '''
|Name|Description|URL|
|:---|:----------|:--|\n''' +  '\n'.join(strings)
    return string


def create_open_gov_markdown_table() -> str:
    # Reading additional open gov data portals
    with open(path.join(config.DATA_DIR, config.OPEN_GOV_ADDITIONAL), 'r') as file:
        gov = json.load(file)
    
    gov_df = pd.read_csv(path.join(config.DATA_DIR, config.OPEN_GOV_WEBSITES))
    for _, row in gov_df.iterrows():
        gov.append(
            {
                'name': row.Name,
                'desc': row.Type,
                'url': row.URL
            }
        )
    gov = sorted(gov, key=lambda x: x['name'])
    
    strings = []
    for row in gov:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            strings.append(string)

        string = '''
|Name|Type|URL|
|:---|:---|:--|\n''' +  '\n'.join(strings)
    return string


def get_markdown_header(header: str) -> str:
    return f'''
<div align = 'center'>

## {header}

</div>
'''

