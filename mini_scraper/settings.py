BOT_NAME = "mini_scraper"

SPIDER_MODULES = ["mini_scraper.spiders"]
NEWSPIDER_MODULE = "mini_scraper.spiders"

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 4
DOWNLOAD_DELAY = 0.5
LOG_LEVEL = "INFO"

# Activamos nuestro pipeline
ITEM_PIPELINES = {
    "mini_scraper.pipelines.JsonWriterPipeline": 1,
}

# Scrapy + Playwright
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# Opcional: esperar a que se renderice JS
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
}

# Reducir bloqueos
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 1
