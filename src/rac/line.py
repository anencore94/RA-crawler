from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from const import *

"""
single page
"""
job_posting_msg = []

line_url = line_url_base + "/ko/jobs?co=Korea"
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
    if re.compile('|'.join(keywords_to_search), re.IGNORECASE).search(tl):
        job_posting_msg.append((tls.text, line_url_base + href))
