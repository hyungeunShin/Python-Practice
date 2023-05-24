import pymysql

class DaoMem :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                       db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from mem"
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    def selectOne(self, m_id):
        sql = f"select * from mem where m_id = '{m_id}'"
        self.curs.execute(sql)
        mem = self.curs.fetchone()
        return mem
    
    def insert(self, m_id, m_name, tel, address):
        sql = f"insert into mem values ('{m_id}', '{m_name}', '{tel}', '{address}')"
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def update(self, m_id, m_name, tel, address):
        sql = f"update mem set m_name = '{m_name}', tel = '{tel}', address = '{address}' where m_id = '{m_id}'"
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def delete(self, m_id):
        sql = f"delete from mem where m_id = '{m_id}'"
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()    
