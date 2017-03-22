import mysql.connector
conn = mysql.connector.connect(user='photo', password='photo', database='photo')
cursor = conn.cursor()
cursor.execute('select * from idol')
values = cursor.fetchall()
print(values[0][1])
cursor.close()
conn.close()