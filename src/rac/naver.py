from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from const import *

"""
더보기
https://signing.tistory.com/47
selenium 필요
"""

answer = []
page_num = 1

url = naver_url_base + "/list/developer"
html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

for cover in bsObject.find_all('ul', {'class': 'list_jobs'}):
    hrefs = cover.select(
        'li > div > div > a'
    )
    titles = cover.select(
        'li > div > div > a > h4'
    )

for a, tls in zip(hrefs, titles):
    href = a.get('href')
    tl = tls.text.lower()
    if re.compile('|'.join(search_list), re.IGNORECASE).search(tl):
        answer.append((tls.text, kakao_url_base + href))

print(answer)
