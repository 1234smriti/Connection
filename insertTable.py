from connection.connection import Con
c=Con()
con=c.getCon()
print(con)
ram=con.cursor()
ram.execute("insert into kfc.chicken(NameOfChicken,price) values('chilliChicken',50),('handiChicken',140)")
con.commit()