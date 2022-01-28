import mysql.connector
class Con:
    def getCon(self):
        con=mysql.connector.connect(host="localhost",user="root",password="")
        return con