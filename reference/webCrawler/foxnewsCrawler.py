import requests
import json
import re

from bs4 import BeautifulSoup

file_dir = 'reference/webCrawler/downloads/'
file_name = 'jared-kushner-denies-shadow-task-force.html'
path = file_dir + file_name
soup = BeautifulSoup(open(path, encoding='utf-8'), 'lxml')
typeTag = "application/ld+json"

def get_article_info(soup, typeTag):
    json_data = soup.find(type=typeTag).text
    return json.loads(json_data)
    
def get_article_content(soup):
    article_content = soup.find(attrs={'class': 'article-content'}).find_all('p')
    result = ''
    for p in article_content:
        result += p.text + '\n'
    return result

print('article info: --------------')
print(get_article_info(soup, typeTag))
print('article content: -----------')
print(get_article_content(soup))

# print(len(soup.find_all('a')))