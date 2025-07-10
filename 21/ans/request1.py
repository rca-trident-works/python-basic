import requests

url = 'https://www.yahoo.co.jp/'
response = requests.get(url, timeout=5)

print(response)
print('-='*10)
print(response.status_code)
print('-='*10)
print(response.headers)
print('-='*10)
print(response.text)
print('-='*10)
print(response.content)
print('-='*10)
print(response.encoding)
print('-='*10)
print(response.cookies)
