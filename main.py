import os
import utils.utils as utils
import utils.config as config

if __name__ == '__main__':
    open_gov_path = os.path.join(config.DATA_DIR, config.OPEN_GOV_WEBSITES)
    if not os.path.exists(open_gov_path):
        df = utils.process_open_gov_df(
            utils.fetch_open_gov_csv(
                config.OPEN_GOV_URLS
            )
        )
        df.to_csv(open_gov_path, index=False)
    
    # Generate Markdown table here
    # ...
