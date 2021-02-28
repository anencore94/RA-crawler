import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

import const

"""
single page
"""


def get_msgs(keywords):
    hrefs, titles = [], []
    job_posting_msg = []

    url = const.CompanyUrl.LINE + "/ko/jobs?co=Korea"
    html = urlopen(url)
    bs_object = BeautifulSoup(html, "html.parser")

    for cover in bs_object.find_all('ul', {'class': 'job_list'}):
        hrefs = cover.select(
            'li > a'
        )
        titles = cover.select(
            'li > a > h3'
        )

    for a, tls in zip(hrefs, titles):
        href = a.get('href')
        tl = tls.text.lower()
        if re.compile('|'.join(keywords), re.IGNORECASE).search(tl):
            job_posting_msg.append((tls.text, const.CompanyUrl.LINE + href))

    return job_posting_msg
