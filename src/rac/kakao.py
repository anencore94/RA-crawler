from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from const import *

"""
need pagination
"""

job_posting_msg = []
page_num = 1

url = kakao_url_base + "/" + "jobs"
html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

page_list = bsObject.findAll("a", {"class": "link_page"})
page_count = len(page_list) + 1
# print(page_count)

for page_num in range(1, page_count + 1):
    html = urlopen(url + "?page=" + str(page_num))
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
        if re.compile('|'.join(keywords_to_search), re.IGNORECASE).search(tl):
            job_posting_msg.append((tls.text, kakao_url_base + href))
