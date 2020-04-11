from bs4 import BeautifulSoup
from selenium import webdriver

import requests
import os
import traceback


def store(file_data, file_dir, file_name):
    '''保存html到本地'''

    full_path = file_dir + file_name
    if os.path.exists((full_path)):
        print(full_path + " exists")
        return

    if not os.path.exists((file_dir)):
        os.makedirs(os.getcwd() + '/' + file_dir)

    try:
        with open(full_path, 'wb') as file:
            file.write(file_data)
    except:
        traceback.print_exc()

def main(driver):
    html_doc_path = "reference/webCrawler/alice.html"

    # url = 'https://blog.csdn.net/zhuangailing/article/details/79046187'
    url = 'http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002845&announcementId=1207473648&orgId=9900029474&announcementTime=2020-04-10'
    download_dir = 'reference/webCrawler/downloads/'
    
    file_data = ''
    current_url = ''
    file_name = '公告'
    file_ext = '.pdf'

    driver.get(url)

    while True:
        msg = input("waitting user input...")
        if msg == "quit":
            break

        # 只有当前url更新的时候才更新数据
        if current_url != driver.current_url:
            current_url = driver.current_url
            driver.get(url)
            file_data = requests.get(driver.current_url)
            store(file_data.content, download_dir, file_name + file_ext)
        
    
with webdriver.Safari() as driver:
    main(driver)
