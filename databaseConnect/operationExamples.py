import mysql.connector

tank_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "tank20200420"
)

mycursor = tank_db.cursor()

'''JOIN语句'''
# sql = "SELECT site.name AS title, \
#         sitefeed.entryLink AS seedLink \
#         FROM site \
#         JOIN sitefeed ON site.id = sitefeed.siteId\
# "

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for r in myresult:
#     print(r)


'''SELECT语句 + LIMIT从句'''
# mycursor.execute("SELECT * FROM site LIMIT 5")

# myresult = mycursor.fetchall()

# print(myresult)

'''SELECT语句 + WHERE从句'''
# sql = "SELECT * FROM site WHERE id = %s"
# val = (1, )

# mycursor.execute(sql, val)
# myresult = mycursor.fetchone()

# print(myresult)

'''INSERT语句'''
# sql = "INSERT INTO config (id, name, module) VALUES (%s, %s, %s)"
# val = (1, "name", "collect")

# mycursor.execute(sql, val)

# tank_db.commit()

# print(mycursor.rowcount, "record inserted.")

'''DELETE语句'''
# sql = "DELETE FROM config WHERE 1"

# mycursor.execute(sql)

# tank_db.commit()

# print(mycursor.rowcount, "record(s) deleted")

mycursor.close()