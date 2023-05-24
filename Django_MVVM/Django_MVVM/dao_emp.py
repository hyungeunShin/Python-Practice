import pymysql

class DaoEmp :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                       db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    def selectOne(self, e_id):
        sql = f"select * from emp where e_id = '{e_id}'"
        self.curs.execute(sql)
        emp = self.curs.fetchone()
        return emp
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"insert into emp values ('{e_id}', '{e_name}', '{sex}', '{addr}')"
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def update(self, e_id, e_name, sex, addr):
        sql = f"update emp set e_name = '{e_name}', sex = '{sex}', addr = '{addr}' where e_id = '{e_id}'"
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def delete(self, e_id):
        sql = f"delete from emp where e_id = '{e_id}'"
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()    

if __name__ == '__main__':
    de = DaoEmp()
    # mylist = de.selectList()
    # print(mylist)
    # arr = de.selectOne("1")
    # print(arr)
    #cnt = de.insert("5", "5", "5", "5")
    #print(cnt)
    #cnt = de.update("5", "3", "3", "3")
    #print(cnt)
    cnt = de.delete("5")
    print(cnt)