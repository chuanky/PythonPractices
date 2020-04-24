import mysql.connector
import requests

irica_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "irica20140408"
)

def fetch_data(db):
    mycursor = db.cursor()

    sql = "SELECT title, providerName from rssfeed"
    where = ""

    mycursor.execute(sql)
    results = mycursor.fetchall()

    with open('rss_200_title.txt', 'w', encoding='utf-8') as f:
        for r in results:
            f.write(r[0] + '\n')

    with open('rss_200_provider.txt', 'w', encoding='utf-8') as f:
        for r in results:
            f.write(r[1] + '\n')


fetch_data(irica_db)

