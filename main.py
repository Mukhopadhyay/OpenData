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
    with open('TEST.md', 'w', encoding='utf-8') as file:
        file.write(config.README_TEMPLATE)
    
    with open('TEST.md', 'a') as file:
        file.write(utils.get_markdown_header('Open Websites'))
        file.write(utils.create_openweb_markdown_table())
    
    with open('TEST.md', 'a') as file:
        file.write(utils.get_markdown_header('NLP Datasets'))
        file.write(utils.create_nlp_markdown_table())
    
    with open('TEST.md', 'a') as file:
        file.write(utils.get_markdown_header('Image Datasets'))
        file.write(utils.create_image_markdown_table())
    
    with open('TEST.md', 'a') as file:
        file.write(utils.get_markdown_header('AUDIO Datasets'))
        file.write(utils.create_audio_markdown_table())
        
    with open('TEST.md', 'a', encoding='utf-8') as file:
        file.write(utils.get_markdown_header('Open GOV'))
        file.write(utils.create_open_gov_markdown_table())
