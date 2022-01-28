from connection.connection import Con
d=Con()
con=d.getCon()
print(con)
car=con.cursor()
car.execute("create Database kfc")