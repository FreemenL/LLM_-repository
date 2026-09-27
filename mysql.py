import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=7899,
    user='root',
    passwd='1234',
    database='mysql',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()


cursor.execute("SELECT VERSION()")

print(f"mysql version: {cursor.fetchone()}")

cursor.close()

conn.close()

print('基础版python 链接mysql 成功')