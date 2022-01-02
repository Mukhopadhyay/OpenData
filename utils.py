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

def create_markdown_table(df: pd.DataFrame) -> str:
    idx = 0
    for _, row in df.iterrows():
        if row.URL.find('.') == -1:
            continue
        try:
            string = f"|**{row.Name.strip()}**|{row.Type}|[{row.URL.split('//')[1].split('/')[0]}]({row.URL})|"
        except Exception:
            string = f"|**{row.Name.strip()}**|{row.Type}|[{row.URL}]({row.URL.split('/')[0]})|"
        finally:
            print(string)
            idx += 1
    
    print(f'\n\n{idx}')

df = process_open_gov_df(
    fetch_open_gov_csv(
        OPEN_GOV_URLS
    )
)
create_markdown_table(df)
