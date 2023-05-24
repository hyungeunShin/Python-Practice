import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                       db='python', charset='utf8')

curs = conn.cursor()

e_name = "6"
sex = "6"
addr = "6"

sql = f"""
    UPDATE emp
    SET
        e_name = '{e_name}',
        sex = '{sex}',
        addr = '{addr}'
    WHERE e_id = '3'
"""

curs.execute(sql)
print(curs.rowcount)

conn.commit()

curs.close()
conn.close()