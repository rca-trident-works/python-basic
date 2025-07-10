import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def get_link(url):
    # リクエストを送信してHTMLコンテンツを取得 (SSL検証を有効)
    response = requests.get(url, verify=True)
    response.raise_for_status()  # エラーが発生した場合は例外を発生させる

    # BeautifulSoupを使用してHTMLコンテンツを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # aタグを全て取得し、href属性からリンクを抽出
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    # フルURLに変換し、一意のリストを作成
    unique_links = set(urljoin(url, link) for link in links)

    return unique_links


# トップページのURL
# url = 'https://computer.trident.ac.jp/'
url = 'https://sat.f5.si/~yoshimura/nt/'
# url = 'https://sat.f5.si/~yoshimura/nt/trident.html'
base_url = urlparse(url).netloc

unique_links = get_link(url)

# 一意のリンクを表示
for link in sorted(unique_links):
    if urlparse(link).netloc != base_url:
        print(f'外部 Link:{link}')
    else:
        print(f'内部 Link:{link}')
        next_unique_links = get_link(link)
        if next_unique_links:
            for lk in sorted(next_unique_links):
                print(f'\t{lk}')
        else:
            print('\tLinkなし')
    time.sleep(1)
