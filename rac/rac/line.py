import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

import const

"""
single page
"""
job_posting_msg = []

line_url = const.CompanyUrl.LINE + "/ko/jobs?co=Korea"
html = urlopen(line_url)
bsObject = BeautifulSoup(html, "html.parser")
for cover in bsObject.find_all('ul', {'class': 'job_list'}):
    hrefs = cover.select(
        'li > a'
    )
    titles = cover.select(
        'li > a > h3'
    )

for a, tls in zip(hrefs, titles):
    href = a.get('href')
    tl = tls.text.lower()
    if re.compile('|'.join(const.keywords_to_search), re.IGNORECASE).search(tl):
        job_posting_msg.append((tls.text, const.CompanyUrl.LINE + href))
