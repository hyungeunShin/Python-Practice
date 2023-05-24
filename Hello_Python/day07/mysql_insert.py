import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                       db='python', charset='utf8')

curs = conn.cursor()

sql = "INSERT INTO emp VALUES (%s, %s, %s, %s)"

curs.execute(sql, ('4', '4', '4', '4'))
conn.commit()

curs.close()
conn.close()