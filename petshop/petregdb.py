import psycopg2 as pg

# con=pg.connect('dbname=postgres user=postgres password=Finserv@2023')
# cur = con.cursor()
# cur.execute('create table pets(pid serial primary key, ptype varchar(10), pbreed varchar(20), pname varchar(20),  page int, pown varchar(20));')
# con.commit()
# cur.execute('drop table pets;')
# con.commit()

class Pet:
    def __init__(self,ptype,pbreed,pname,page,pown) -> None:
        self.ptype=ptype
        self.pbreed=pbreed
        self.pname=pname
        self.page=page
        self.pown=pown

class DBConnection:
    con=None
    cur=None
    def __init__(self) -> None:
        pass

    @classmethod
    def connect_db(cls):
        cls.con=pg.connect('dbname=postgres user=postgres password=Finserv@2023')
        cls.cur = cls.con.cursor()

    @classmethod
    def create_pets(cls):
        cls.cur.execute(f'create table pets(pid serial primary key, ptype varchar(10), pbreed varchar(20), pname varchar(20),  page int, pown varchar(20));')
        cls.con.commit()

    @classmethod
    def read_pets(cls):
        cls.cur.execute('select * from pets;')
        cls.con.commit()
        petdetails=cls.cur.fetchall()
        return petdetails

    @classmethod
    def insert_pets(cls,pet):
        cls.cur.execute(f"insert into pets(ptype,pbreed,pname,page,pown) values('{pet.ptype}','{pet.pbreed}','{pet.pname}',{pet.page},'{pet.pown}');")
        cls.con.commit()

    @classmethod
    def update_pets(cls,pet,petid):
        cls.cur.execute(f"update pets set ptype='{pet.ptype}',pbreed='{pet.pbreed}',pname='{pet.pname}',page={pet.page},pown='{pet.pown}' where pname={pet.pname};")
        cls.con.commit()

    @classmethod
    def delete_pets(cls,delid):
        cls.cur.execute(f"delete from pets where pid={delid}")
        cls.con.commit()





# pet=Pet()
# pets_db=DBConnection()
# pets_db.connect_db()
# pets_db.create_pets()
