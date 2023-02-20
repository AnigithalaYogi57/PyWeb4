# import mysql.connector
from mysql.connector import connect
mydb = connect(
    user="root",
    password="USTech@1225",
    host="localhost",
    database='jandb'
)

print(mydb)

cur = mydb.cursor()

# cur.execute("CREATE DATABASE jandb")
# cur.execute("use jandb")
# cur.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
