import os
from mini_scraper.utils import get_local_path

class SaveFilePipeline:

    def process_item(self, item, spider):
        try:
            url = item["url"]
            body = item["body"]
            base_folder = spider.settings.get("DATA_FOLDER")

            file_path = get_local_path(base_folder, url)

            with open(file_path, "wb") as f:
                f.write(body)

        except Exception as e:
            spider.logger.error(f"Error saving file: {e}")

        return item
