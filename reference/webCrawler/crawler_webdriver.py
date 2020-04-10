from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os


def store(file_data, file_dir, file_name):
    '''保存html到本地'''

    full_path = file_dir + file_name
    try:
        file = open(full_path, 'r')
    except FileNotFoundError:
        # 如果本地不存在自动建立该文件
        if not os.path.exists(file_dir): 
            os.makedirs(os.getcwd() + '/' + file_dir)
        file = open(full_path, 'wb')
        file.write(file_data)
    else:
        print(full_path + " exists")
    finally:
        file.close()

def main(driver):
    html_doc_path = "reference/webCrawler/alice.html"

    # url = 'https://blog.csdn.net/zhuangailing/article/details/79046187'
    url = 'http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002845&announcementId=1207473648&orgId=9900029474&announcementTime=2020-04-10'
    download_dir = 'reference/webCrawler/downloads/'
    
    file_data = ''
    current_url = ''

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
            try:
                store(file_data.content, download_dir, "公告.pdf")
            except Exception as e:
                print("store failure: " + str(e))
        
    
driver = webdriver.Safari()
main(driver)
driver.close()

