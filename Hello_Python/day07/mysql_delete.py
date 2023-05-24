import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                       db='python', charset='utf8')

curs = conn.cursor()

sql = f"""
    delete
    from emp
    WHERE e_id = '3'
"""

curs.execute(sql)
print(curs.rowcount)

conn.commit()

curs.close()
conn.close()