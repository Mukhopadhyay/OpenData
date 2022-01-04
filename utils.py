import json
import pandas as pd

OPEN_GOV_URLS = 'https://s3.amazonaws.com/bsp-ocsit-prod-east-appdata/datagov/wordpress/2019/09/opendatasites91819.csv'

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

def create_gov_markdown_table(df: pd.DataFrame) -> str:
    for _, row in df.iterrows():
        if row.URL.find('.') == -1:
            continue
        try:
            string = f"|**{row.Name.strip()}**|{row.Type}|[{row.URL.split('//')[1].split('/')[0]}]({row.URL})|"
        except Exception:
            string = f"|**{row.Name.strip()}**|{row.Type}|[{row.URL}]({row.URL.split('/')[0]})|"
        finally:
            print(string)


def create_audio_markdown_table() -> str:
    with open('data/audio-datasets.json', 'r') as file:
        audio = json.load(file)
    
    audio = sorted(audio, key=lambda x: x['name'])
    
    for row in audio:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            print(string)

def create_image_markdown_table() -> str:
    with open('data/image-datasets.json', 'r') as file:
        image = json.load(file)
        
    image = sorted(image, key=lambda x: x['name'])
        
    for row in image:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            print(string)

def create_nlp_markdown_table() -> str:
    with open('data/nlp-datasets.json', 'r') as file:
        nlp = json.load(file)
        
    nlp = sorted(nlp, key=lambda x: x['name'])
    
    for row in nlp:
        try:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url'].split('//')[1].split('/')[0]}]({row['url']})|"
        except Exception:
            string = f"|**{row['name'].strip()}**|{row['desc']}|[{row['url']}]({row['url'].split('/')[0]})|"
        finally:
            print(string)



df = process_open_gov_df(
    fetch_open_gov_csv(
        OPEN_GOV_URLS
    )
).reset_index(drop=True)


# create_markdown_table(df)
create_audio_markdown_table()
