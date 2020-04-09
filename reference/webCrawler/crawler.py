from bs4 import BeautifulSoup
import requests
import os


def store(html_string, file_dir, file_name):
    '''保存html到本地'''
    full_path = file_dir + file_name
    try:
        file = open(full_path, 'r')
    except FileNotFoundError:
        os.makedirs(os.getcwd() + '/' + file_dir)
        file = open(full_path, 'w')
        file.write(html_string)
    else:
        print(full_path + " exists")
    finally:
        file.close()

html_doc_path = "reference/webCrawler/alice.html"
url = 'https://blog.csdn.net/zhuangailing/article/details/79046187'
download_dir = 'reference/webCrawler/downloads/'

r = requests.get(url)
remote_html = r.text
soup = BeautifulSoup(remote_html, 'lxml')
file_name = soup.title.text + '.html'

store(remote_html, download_dir, file_name)
    

