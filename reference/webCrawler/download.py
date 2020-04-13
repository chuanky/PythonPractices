import requests
from bs4 import BeautifulSoup

# url = 'https://www.foxnews.com/politics/christine-blasey-ford-attorney-says-she-came-forward-to-get-asterisk-on-kavanaughs-name-ahead-of-abortion-rulings'
url = 'https://www.foxnews.com/politics/jared-kushner-denies-shadow-task-force'
file_dir = 'reference/webCrawler/downloads/'
file_name = 'jared-kushner-denies-shadow-task-force.html'
target_name = 'jared-kushner-denies-shadow-task-force_pretty.html'
path = file_dir + file_name
encoding = 'utf-8'

def download_web_source(url, local_path):
    r = requests.get(url)
    with open(local_path, 'w', encoding=encoding) as file:
        file.write(r.text)

def prettify_web_source(file_dir, source_name, target_name):
    soup = BeautifulSoup(open(file_dir + source_name, encoding=encoding), 'lxml')
    with open(file_dir + target_name, 'w', encoding=encoding) as file:
        file.write(soup.prettify())

download_web_source(url, path)
prettify_web_source(file_dir, file_name, target_name)

