import psycopg2 as pg

con=pg.connect('dbname=postgres user=postgres password=Finserv@2023')
cur = con.cursor()
cur.execute('drop table pets;')
con.commit()