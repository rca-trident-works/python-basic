import time
import requests
import hashlib
import datetime


def site_md5(text):
    return hashlib.md5(text.encode()).hexdigest()


# トップページのURL
# url = 'https://computer.trident.ac.jp/'
url = 'https://sat.f5.si/~yoshimura/nt/'
# url = 'https://sat.f5.si/~yoshimura/nt/trident.html'

# 内容を取得
site_hash_old = ''
while True:
    time.sleep(5)
    response = requests.get(url, verify=True).text
    site_hash = site_md5(response)
    dt_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{dt_now} ', end='')
    if site_hash == site_hash_old:
        print('変更なし')
        continue
    else:
        print(f'変更を検知：{site_hash} {url}')
        site_hash_old = site_hash
