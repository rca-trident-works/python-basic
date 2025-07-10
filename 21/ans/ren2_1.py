import requests
from bs4 import BeautifulSoup

# トップページのURL
# url = 'https://computer.trident.ac.jp/'
url = 'https://sat.f5.si/~yoshimura/nt/'
# url = 'https://sat.f5.si/~yoshimura/nt/trident.html'

# リクエストを送信してHTMLコンテンツを取得
response = requests.get(url)
response.raise_for_status()  # エラーが発生した場合は例外を発生させる

# BeautifulSoupを使用してHTMLコンテンツを解析
soup = BeautifulSoup(response.text, 'html.parser')

# aタグを全て取得し、href属性からリンクを抽出
links = [a.get('href') for a in soup.find_all('a', href=True)]

# 一意のリストを作成
unique_links = set(links)

# 一意のリンクを表示
for link in unique_links:
    print(link)
