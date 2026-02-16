import os
import scrapy
from urllib.parse import urljoin, urlparse
from dotenv import load_dotenv
from mini_scraper.utils import rewrite_links

load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")

class FirstSpider(scrapy.Spider):
    name = "first_spider"

    def start_requests(self):
        yield scrapy.Request(
            TARGET_URL,
            meta={
                "playwright": True,
                "playwright_include_page": True,
            },
            callback=self.parse
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        await page.wait_for_load_state("networkidle")

        requests = []

        def handle_request(request):
            requests.append(request.url)

        page.on("request", handle_request)

        content = await page.content()

        html_bytes = content.encode("utf-8")

        yield {
            "url": response.url,
            "body": html_bytes
        }

        domain = urlparse(TARGET_URL).netloc

        links = response.css("a::attr(href)").getall()
        assets = (
            response.css("link::attr(href)").getall() +
            response.css("script::attr(src)").getall() +
            response.css("img::attr(src)").getall() +
            response.css("source::attr(src)").getall() +
            response.css("video::attr(src)").getall() +
            response.css("audio::attr(src)").getall()
        )

        all_urls = links + assets + requests

        seen = set()

        for url in all_urls:
            if not url:
                continue

            absolute_url = urljoin(response.url, url)
            parsed = urlparse(absolute_url)

            if parsed.netloc != domain:
                continue

            if absolute_url in seen:
                continue

            seen.add(absolute_url)

            yield scrapy.Request(
                absolute_url,
                callback=self.save_asset,
                dont_filter=True
            )

        await page.close()

    def save_asset(self, response):
        try:
            yield {
                "url": response.url,
                "body": response.body
            }
        except Exception as e:
            self.logger.error(f"Error saving asset: {e}")
