import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")
parsed = urlparse(TARGET_URL)
DOMAIN = parsed.netloc

BOT_NAME = "mini_scraper"

SPIDER_MODULES = ["mini_scraper.spiders"]
NEWSPIDER_MODULE = "mini_scraper.spiders"

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 16

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
}

ITEM_PIPELINES = {
    "mini_scraper.pipelines.SaveFilePipeline": 300,
}

DATA_FOLDER = f"data/site-{DOMAIN}"

ALLOWED_DOMAIN = DOMAIN
TARGET_URL = TARGET_URL
