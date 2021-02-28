import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

import const

"""
need pagination
"""


def kakao(keywords):
    hrefs, titles = [], []
    job_posting_msg = []

    url = const.CompanyUrl.KAKAO + "/" + "jobs"
    html = urlopen(url)
    bs_object = BeautifulSoup(html, "html.parser")

    page_list = bs_object.findAll("a", {"class": "link_page"})
    page_count = len(page_list) + 1

    for page_num in range(1, page_count + 1):
        html = urlopen(url + "?page=" + str(page_num))
        bs_object = BeautifulSoup(html, "html.parser")

        for cover in bs_object.find_all('ul', {'class': 'list_jobs'}):
            hrefs = cover.select(
                'li > div > div > a'
            )
            titles = cover.select(
                'li > div > div > a > h4'
            )

        for a, tls in zip(hrefs, titles):
            href = a.get('href')
            tl = tls.text.lower()
            if re.compile('|'.join(keywords), re.IGNORECASE).search(tl):
                job_posting_msg.append(
                    (tls.text, const.CompanyUrl.KAKAO + href))

    return job_posting_msg
