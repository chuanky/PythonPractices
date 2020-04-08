from bs4 import BeautifulSoup

html_doc_path = "reference/webCrawler/alice.html"

soup = BeautifulSoup(open(html_doc_path), 'lxml')

links = soup.findAll('a')
for link in links:
    print(link)