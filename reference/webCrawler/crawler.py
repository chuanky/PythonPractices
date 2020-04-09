from bs4 import BeautifulSoup
import requests
import os


def store(html_string, path):
    '''保存html到本地'''
    
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        file = open(path, 'w')
        file.write(html_string)
    else:
        print(path + " exists")
    finally:
        file.close()

html_doc_path = "reference/webCrawler/alice.html"
url = 'https://blog.csdn.net/zhuangailing/article/details/79046187'
download_dir = 'reference/webCrawler/downloads/'

r = requests.get(url)
remote_html = r.text
soup = BeautifulSoup(remote_html, 'lxml')
file_path = download_dir + soup.title.text + '.html'

store(remote_html, file_path)
    

