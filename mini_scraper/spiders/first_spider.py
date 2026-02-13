import scrapy
from urllib.parse import urlparse
import os


class FirstSpider(scrapy.Spider):
    name = "first"
    start_urls = ["https://quotes.toscrape.com/"]
    allowed_domains = ["quotes.toscrape.com"]

    visited = set()

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT": 30000,  # 30s
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={"playwright": True, "playwright_include_page": True},
                callback=self.parse
            )

    def get_base_dir(self):
        parsed = urlparse(self.start_urls[0])
        site_name = parsed.netloc.replace("www.", "")
        base_dir = os.path.join("data", f"site-{site_name}")
        os.makedirs(base_dir, exist_ok=True)
        return base_dir

    def save_file(self, url, content, folder, ext):
        base_dir = self.get_base_dir()
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        parsed = urlparse(url)
        filename = parsed.path.strip("/").replace("/", "_")
        if not filename:
            filename = "index"
        filepath = os.path.join(folder_path, f"{filename}.{ext}")
        with open(filepath, "wb") as f:
            f.write(content)

    async def parse(self, response):
        if response.url in self.visited:
            return
        self.visited.add(response.url)

        page = response.meta.get("playwright_page")
        if page:
            # Espera a que cargue JS y contenido dinámico
            await page.wait_for_load_state("networkidle")

        # HTML
        self.save_file(response.url, response.body, "html", "html")

        # CSS
        css_links = response.css("link::attr(href)").getall()
        for css in css_links:
            yield response.follow(
                css,
                meta={"folder": "css", "ext": "css", "playwright": True},
                callback=self.parse_asset
            )

        # JS
        js_links = response.css("script::attr(src)").getall()
        for js in js_links:
            yield response.follow(
                js,
                meta={"folder": "js", "ext": "js", "playwright": True},
                callback=self.parse_asset
            )

        # TS
        ts_links = response.css("script[type='module']::attr(src)").getall()
        for ts in ts_links:
            yield response.follow(
                ts,
                meta={"folder": "ts", "ext": "ts", "playwright": True},
                callback=self.parse_asset
            )

        # Imágenes
        img_links = response.css("img::attr(src)").getall()
        for img in img_links:
            ext = img.split(".")[-1] if "." in img else "img"
            yield response.follow(
                img,
                meta={"folder": "images", "ext": ext, "playwright": True},
                callback=self.parse_asset
            )

        # Seguir enlaces internos
        links = response.css("a::attr(href)").getall()
        for link in links:
            yield response.follow(
                link,
                meta={"playwright": True, "playwright_include_page": True},
                callback=self.parse
            )

        if page:
            await page.close()

    async def parse_asset(self, response):
        if response.url in self.visited:
            return
        self.visited.add(response.url)

        folder = response.meta.get("folder", "other")
        ext = response.meta.get("ext", "txt")

        page = response.meta.get("playwright_page")
        if page:
            await page.wait_for_load_state("networkidle")
        self.save_file(response.url, response.body, folder, ext)
        if page:
            await page.close()
