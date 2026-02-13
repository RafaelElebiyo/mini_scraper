🕷️ Mini Scraper (Scrapy + Playwright)

A small educational project for professional Web Scraping built with:

Python 3.10+

Scrapy

Playwright

Mirror-style crawler (downloads HTML, CSS, JS, images)

Automatic daily execution with cron

The scraper can:
````
✅ Render JavaScript (dynamic websites)
✅ Download full HTML
✅ Download CSS, JS, TS, and images
✅ Avoid duplicate URLs
✅ Save files in an organized folder structure
✅ Run automatically every day
````
📁 Project Structure
````
mini-scraper/
│
├── scrapy.cfg
├── requirements.txt
├── run.sh
├── .env
├── .gitignore
├── README.md
│
├── data/
│   └── site-example.com/
│        ├── html/
│        ├── css/
│        ├── js/
│        ├── ts/
│        └── images/
│
└── mini-scraper/
    ├── items.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        └── first_spider.py
````
🚀 Step-by-step Installation
1️⃣ Create virtual environment

Linux / macOS:
````
python3 -m venv venv
source venv/bin/activate
````

Windows:

```nv\Scripts\activate

2️⃣ Install Python dependencies
pip install -r requirements.txt

3️⃣ Install Playwright browsers
```
IMPORTANT (first time only):

`playwright install`


Linux (if system libraries are missing):

`playwright install-deps`

⚙️ Configuration
.env

Define the target URL:

START_URL=https://quotes.toscrape.com/


You can replace it with:
```
https://www.amazon.com/s?k=laptop
https://example.com
https://your-local-store.com
```

▶️ Run the scraper

Inside the virtual environment:

`scrapy crawl products`

📂 Output

The scraper automatically generates:

```
data/
 └── site-quotes.toscrape.com/
      ├── html/
      ├── css/
      ├── js/
      ├── ts/
      └── images/

```
Each resource is saved physically:

Example:
````
html/index.html
css/main.css
js/app.js
images/logo.png
````

👉 This creates an offline mirror of the website.

⏰ Automatic execution with CRON (Linux/Mac)

Edit crontab:

`crontab -e`


Run daily at 3 AM:

`0 3 * * * /path/to/mini-scraper/run.sh >> scraper.log 2>&1`

🧠 Technologies Used
````
Tool	Purpose
Scrapy	Main crawler
Playwright	JavaScript rendering
Python	Scraping logic
Cron	Automation
````

🔥 Best Practices Implemented
````
✔ Virtual environment
✔ .env configuration
✔ .gitignore
✔ Organized resource folders
✔ No duplicate downloads
✔ Compatible with dynamic websites
✔ Modular code
````
🧪 Use Cases
````
This project can be used for:

Professional web scraping

Static website mirroring

SEO audits

Offline HTML analysis

Extracting data from e-commerce sites

Academic scraping experiments
````
⚠️ Legal Notice

Use this project only for:

✅ learning
✅ testing
✅ your own websites
✅ websites with permission

Always respect robots.txt and website terms of service.