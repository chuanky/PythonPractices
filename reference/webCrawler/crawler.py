from bs4 import BeautifulSoup
import requests
import os
import re


def store(html_string, file_dir, file_name):
    '''保存html到本地'''
    full_path = file_dir + file_name
    try:
        file = open(full_path, 'r')
    except FileNotFoundError:
        if not os.path.exists(file_dir): 
            os.makedirs(os.getcwd() + '/' + file_dir)
        file = open(full_path, 'w', encoding='utf-8')
        file.write(html_string)
    else:
        print(full_path + " exists")
    finally:
        file.close()

html_doc_path = "reference/webCrawler/alice.html"
Cookie = "JSESSIONID=85A18ABEED606C160C61DB52758902FB; insert_cookie=37836164; UC-JSESSIONID=0070DA5C847C74BA7DF96A2B0919DA3D; _sp_ses.2141=*; cninfo_user_browse=300250,9900020348,%E5%88%9D%E7%81%B5%E4%BF%A1%E6%81%AF; _sp_id.2141=de6fd1b2-db80-4cb7-adb9-d2f99c8babdd.1586185227.2.1586437195.1586185871.3c10b96c-c073-4a16-9d1b-d47621a9fae0"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': Cookie,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'www.cninfo.com.cn',
    'Referer': 'http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002845&announcementId=1207473648&orgId=9900029474&announcementTime=2020-04-10'
}

data = {
    'announceId': '1207473648',
    'flag': 'true',
    'announceTime': '2020-04-10'
}

# url = 'https://blog.csdn.net/zhuangailing/article/details/79046187'
url = 'http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002845&announcementId=1207473648&orgId=9900029474&announcementTime=2020-04-10'
download_dir = 'reference/webCrawler/downloads/'

r = requests.post(url, data=data, headers=headers)
remote_html = r.text
print(remote_html)
soup = BeautifulSoup(remote_html, 'lxml')
file_name = soup.title.text + '.html'

store(remote_html, download_dir, file_name)

# print(soup.find_all(href=re.compile(".pdf")))

