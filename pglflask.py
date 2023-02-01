import psycopg2 as pg

# con=pg.connect('dbname=postgres user=postgres password=Finserv@2023')
# cur = con.cursor()
# # cur.execute('drop table test')
# cur.execute('CREATE table test(id serial primary key, num integer, data varchar);')
# cur.execute('insert into test(num,data) values(%s,%s)',(102,'computers'))
# cur.execute('select * from test')
# con.commit()
# print(cur.fetchone())
# print(cur.fetchall())
class Student:
    def __init__(self,sid,sname,sadd) -> None:
        self.sid=sid
        self.sname=sname
        self.sadd=sadd

class DBConnection:
    conn=None
    cur=None
    def __init__(self) -> None:
        pass
    @classmethod
    def connect_db(cls):
        cls.conn=pg.connect('debname=postgres user=postgres password=Finserv@2023')
        cls.cur = cls.conn.cursor()

    @classmethod
    def create_table(cls, tname, f1, f2, f3):
        cls.cur.execute('create table'+str(tname)+'('+str(f1)+'varchar primary key,'+str(f2)+'varchar);')
        cls.conn.commit()
    
    @classmethod
    def select_records(cls,tname):
        cls.cur.execute('select * from'+str(tname)+';')
        students=cls.cur.fetchall()
        for student in students:
            print(students)

    @classmethod
    def insert_db(cls,tname,f1,f2):
        cls.cur.execute('insert into'+str(tname)+'('+str(f1)+','+str(f2)+') values('+str(f1))
