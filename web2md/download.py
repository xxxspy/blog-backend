import os
import requests
import wget
import logging
import subprocess
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin, urlparse, unquote
import time
from pathlib import Path

# =============================================================================
# Logging Configuration
# =============================================================================
# Configure logging to both file and console for real-time debugging and post-run analysis.
logging.basicConfig(filename='web_scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# =============================================================================
# Persistent Session with Retry Logic
# =============================================================================
# This session is reused for all HTTP requests. The retry logic helps to automatically
# recover from transient network errors.
session = requests.Session()
retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)

# =============================================================================
# Utility Functions
# =============================================================================
def save_file(url, destination):
    """
    Downloads a file from a URL to the specified destination using wget.

    Args:
        url (str): URL of the file to download.
        destination (str): Local path where the file will be saved.
    """
    try:
        logging.info(f"Downloading file: {url} to {destination}")
        wget.download(url, destination)
        logging.info(f"Successfully downloaded file: {url}")
    except Exception as e:
        logging.error(f"Error downloading file {url}: {e}")

def create_directory(path):
    """
    Creates a directory if it does not exist.

    Args:
        path (str): The directory path to create.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created directory: {path}")


def get_html(url, destination):
    parsed_url = urlparse(url)
    page_path = os.path.join(destination, parsed_url.netloc + parsed_url.path)
    


def download_page(url, destination):
    """
    Downloads an HTML page using a persistent session and saves it to the specified destination.

    Args:
        url (str): URL of the page to download.
        destination (str): Local directory where the page should be saved.

    Returns:
        tuple: (BeautifulSoup object, path to saved page) if successful, otherwise (None, None)
    """
    parsed_url = urlparse(url.strip())
    logging.debug(f"Starting download of page: {url} path={parsed_url.path.strip().strip('/')}")
    page_path = Path(destination) / parsed_url.netloc.strip('www.') / parsed_url.path.strip().strip('/')
    print('will download page path:', page_path)
    page_path = Path(page_path)

    if page_path.exists() and page_path.is_file():
        if page_path.suffix == '.html':
            return BeautifulSoup(page_path.read_text('utf8'), 'html.parser')
        else:
            return None

    alter_path = Path(page_path / 'index.html')
    logging.debug('alter path:' + alter_path.as_posix())
    if alter_path.exists() and alter_path.is_file():
        print('exists:', alter_path)
        return BeautifulSoup(alter_path.read_text('utf8'), 'html.parser')

    response = session.get(url, timeout=10)
    if response.status_code == 404:
        return

    response.raise_for_status()

    content_type = response.headers.get('content-type', '')
    print('content type:', content_type)

    if 'text/html' in content_type:
        # page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Build file path based on the URL structure
        if page_path.suffix != '.html':
            page_path = page_path / 'index.html'
        print('write page:', page_path)
        page_path.parent.mkdir(exist_ok=True, parents=True)
        with open(page_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
    else:
        soup = None
        Path(page_path).parent.mkdir(exist_ok=True, parents=True)
        with open(page_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logging.error(f'write file: {page_path}')
    

    return soup


def get_domain(url:str)->str:
    domain = urlparse(url).netloc
    if not domain.startswith('www.'):
        domain = 'www.' + domain
    return domain

def download_website(url, destination, max_pages=-1, link_tags=['link', 'script', 'a', 'img'], ignore_url_ptns=[]):
    """
    Recursively downloads the main page and all linked internal pages and resources.
    Stops when the number of downloaded pages reaches max_pages. Also estimates and logs
    the total and remaining download time.

    Args:
        url (str): Starting URL for the website crawl.
        destination (str): Local directory to save the website.
        max_pages (int): Maximum number of pages to download.
    """
    allowed_domain = get_domain(url)
    logging.info(f"Allowed domain for website crawl: {allowed_domain}")
    to_download = [url]
    downloaded = set()


    while to_download:
        if max_pages>0 and len(downloaded) < max_pages:
            break
        current_url = to_download.pop()
        logging.debug(f"Processing URL: {current_url}")
        soup = download_page(current_url, destination)
        downloaded.add(current_url)
        if not soup:
            continue
        # extract links
        for tag in soup.find_all(link_tags):
            src = tag.get('src') or tag.get('href')
            if not src:
                continue
            link = urljoin(current_url, src)
            domain = get_domain(link)
            if domain and domain==allowed_domain:
                if link not in downloaded and link not in to_download:
                    if not any(i in link for i in ignore_url_ptns) :
                        logging.debug(f'append link: "{link}" with domain "{domain}"')
                        to_download.append(link)
                    else:
                        print('ignore link:', link)
            

# =============================================================================
# Main Execution
# =============================================================================
if __name__ == "__main__":
    # Retrieve environment variables (if set)
    url_to_download = 'https://www.spss-tutorials.com/'
    download_destination = r'D:\dev\blog-backend\web2md\.outputs\spss-tutorials-html'
    logging.info(f"Starting download for {url_to_download} into {download_destination}")
    download_website(url_to_download, download_destination, -1, ignore_url_ptns=['/comment-page-', '/wp-json/', '/feed/'])
