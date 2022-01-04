import json
import config
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
    return final

# def create_gov_markdown_table(df: pd.DataFrame) -> str:
#     for _, row in df.iterrows():
#         if row.URL.find('.') == -1:
#             continue
#         try:
#             string = f"|**{row.Name.strip()}**|{row.Type}|[{row.URL.split('//')[1].split('/')[0]}]({row.URL})|"
#         except Exception:
#             string = f"|**{row.Name.strip()}**|{row.Type}|[{row.URL}]({row.URL.split('/')[0]})|"
#         finally:
#             print(string)


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

    return '\n'.join(strings)

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

    return '\n'.join(strings)

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

    return '\n'.join(strings)


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

    return '\n'.join(strings)
