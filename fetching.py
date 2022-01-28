from connection.connection import Con
d=Con()
con=d.getCon()
print(con)
car=con.cursor()
car.execute("select * from kfc.chicken")
fetch=car.fetchall()
for i in fetch:
    print(i)