import mysql.connector
import requests

tank_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "tank20200420"
)

def fetch_data(tank_db):
    '''从数据库中去信息，存到一个列表中后返回'''
    mycursor = tank_db.cursor()

    sql = "SELECT id ,url from site WHERE tankTag = 1"

    mycursor.execute(sql)
    results = mycursor.fetchall()

    links = []
    sites_without_link = []
    for r in results:
        if r[1] == None or r[1] == '': continue

        links.append([r[0], r[1]])

    return links

def get_html_head(url):
    headers = {
        'user-agent' : 'Mozilla/5.0'
    }
    try:
        r = requests.head(url, headers=headers, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.headers
    except requests.HTTPError as e:
        print(url + " 下载失败")
        print("Status Code: " + str(r.status_code))
    except Exception as e:
        print(url + " 下载失败")
        print(e)

def get_html_text(url):
    headers = {
        'user-agent' : 'Mozilla/5.0'
    }
    try:
        r = r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print(url + " 下载失败")

# print(get_html_head('http://www.harvard.edu/'))
# print(get_html_head('http://www.usip.org/'))

def main():
    urls = fetch_data(tank_db)
    for url in urls:
        print("正在检测：" + url[1])
        r = get_html_head(url[1])
        title = str(url[0])
        link = url[1]
        if r:
            print(link + " 下载成功")
            with open('successSites.txt', 'a', encoding='utf-8') as f:
                f.write(title + '\t' + link + " 下载成功\n")
        else:
            with open('failedSites.txt', 'a', encoding='utf-8') as f:
                f.write(title + '\t' + link + " 下载失败\n")


# urls = fetch_data(tank_db)
# print(len(urls))

main()