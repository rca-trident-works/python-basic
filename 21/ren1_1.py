import collections
import requests
import re
import glob
import sys
import os

# regex pattern for matching URLs
URL_REGEX_PATTERN = r'"(https?://.+?)"'

def main():
    target_url = sys.argv[1] if len(sys.argv) > 1 else None
    if not target_url:
        usage()
        sys.exit(1)

    contents = fetch_page_content(target_url)

    # Extract URLs from the content
    url_dict = collections.Counter(extract_urls(contents))

    if not url_dict:
        print("No URLs found.")
        return

    for url, count in url_dict.most_common(10):
        if count >= 1:
            print(f"{count} - {url}")

def usage():
    """Prints the usage instructions."""
    print("Usage: python %s <URL>" % os.path.basename(__file__))
    print("Example: python %s https://www.example.com" % os.path.basename(__file__))
    sys.exit(1)

def fetch_page_content(url):
    """Fetches the content of a web page given its URL."""

    content = None
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.text
        else:
            print(f"Error fetching {url}: Status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

    return content

def extract_urls(content):
    """Extracts URLs from the given content using regex."""
    if content:
        return re.findall(URL_REGEX_PATTERN, content)
    return []

if __name__ == "__main__":
    main()
