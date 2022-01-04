import utils
import config

if __name__ == '__main__':
    df = utils.process_open_gov_df(
        utils.fetch_open_gov_csv(
            config.OPEN_GOV_URLS
        )
    )
    print(df)
