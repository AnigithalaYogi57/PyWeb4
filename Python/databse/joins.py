import mysql.connector

mydb=mysql.connector.connect(
    user="root",
    password="USTech@1225",
    host="localhost",
    database='mylastdb'
)

cur = mydb.cursor()

sql = "SELECT * FROM users"

# cur.execute(sql)

# for user in cur:
#     print(user)

sql = "SELECT users.name AS user, products.name AS favorite FROM users INNER JOIN products ON users.fav = products.id"
cur.execute(sql)

res = cur.fetchall()

for d in res:
    print(d)