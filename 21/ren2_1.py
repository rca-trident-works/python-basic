import requests
import sys
import collections
import bs4
import os

URL_PREFIX = 'https://computer.trident.ac.jp'

TEST_URL = 'https://www.yahoo.co.jp'

def main():
    target_url = sys.argv[1] if len(sys.argv) > 1 else None
    if not target_url:
        # usage()
        # sys.exit(1)
        target_url = TEST_URL

    contents = fetch_page_content(target_url)
    urls = extract_urls(contents)
    if not urls:
        print("No URLs found.")
        return
    
    for url in urls:
        formatted_url = format_url(url, URL_PREFIX)

    # remove dup
    unique_urls = set(urls)

    for url in unique_urls:
        print(url)

def usage():
    """Prints the usage instructions."""
    print("Usage: python %s <URL>" % os.path.basename(__file__))
    print("Example: python %s https://www.example.com" % os.path.basename(__file__))
    sys.exit(1)

def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error fetching {url}: Status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_urls(content):
    if content:
        soup = bs4.BeautifulSoup(content, 'html.parser')
        urls = [a['href'] for a in soup.find_all('a', href=True)]
        return urls
    return []

def format_url(url, base_url):
    if url.startswith('/'):
        return base_url + url
    return url

if __name__ == "__main__":
    main()
