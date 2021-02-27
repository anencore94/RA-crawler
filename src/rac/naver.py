import os
import platform
import re
import time

from selenium import webdriver

from const import *

"""
더보기 버튼으로 인해 selenium 필요
"""

job_posting_msg = []
page_num = 1

url = naver_url_base + "/list/developer"

# chrome driver setting
chrome_options = webdriver.ChromeOptions()
driverPath = ''
if platform.system() == 'Windows':
    driverPath = "../../lib/win/chromedriver.exe"
elif platform.system() == 'Linux':
    driverPath = os.path.join('chromedriver')
    chrome_options.add_argument('--headless')  # headless
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

else:
    print("Not implemented yet")
    exit(1)

driver = webdriver.Chrome(driverPath, chrome_options=chrome_options)
driver.get(url)

# 경력 탭 클릭
seni = driver.find_element_by_xpath('//*[@id="entType002"]/a')
seni.click()

# scroll down & 10 개 더보기 안나올때까지 클릭
scroll_pause_time = 1.5
while True:
    # 끝까지 스크롤 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(scroll_pause_time)
    # break

    # 더보기 버튼 확인 (없으면 종료)
    more_button = driver.find_element_by_xpath('//*[@id="moreDiv"]')
    if not more_button.is_displayed():
        break

    # 더보기 클릭
    driver.find_element_by_xpath('//*[@id="moreDiv"]/button').click()

jobs = driver.find_elements_by_xpath('//*[@id="jobListDiv"]/ul/li')
for i in range(len(jobs)):
    title = jobs[i].find_element_by_xpath('./a/span/strong').text
    href = jobs[i].find_element_by_xpath('./a').get_attribute('href')

    if re.compile('|'.join(keywords_to_search), re.IGNORECASE).search(
            title.lower()):
        job_posting_msg.append((title, href))
