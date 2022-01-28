from connection.connection import Con
c=Con()
con=c.getCon()
print(con)
ram=con.cursor()
ram.execute("create table kfc.chicken(SN int, NameOfChicken varchar(30) , price int)")