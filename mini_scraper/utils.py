import os
import re
from urllib.parse import urlparse

def clean_query(url):
    parsed = urlparse(url)
    return parsed.scheme + "://" + parsed.netloc + parsed.path

def get_local_path(base_folder, url):
    parsed = urlparse(url)
    path = parsed.path

    if path.endswith("/"):
        path = path + "index.html"
    elif path == "":
        path = "/index.html"

    full_path = os.path.join(base_folder, parsed.netloc, path.lstrip("/"))

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path

def rewrite_links(html_content, domain):
    html_content = re.sub(
        rf'https?://{domain}',
        '',
        html_content
    )
    return html_content
