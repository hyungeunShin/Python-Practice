import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                       db='python', charset='utf8')

e_id = "5"
e_name = "5"
sex = "5"
addr = "5"

curs = conn.cursor()

sql = f"INSERT INTO emp VALUES ('{e_id}', '{e_name}', '{sex}', '{addr}')"
print(sql)

# cnt = curs.execute(sql)
# print(cnt)
curs.execute(sql)
print(curs.rowcount)

conn.commit()

curs.close()
conn.close()