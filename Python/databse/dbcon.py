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
# cur.execute("SHOW DATABASES")

# for db in cur:
#     print(db)

cur.execute("SHOW TABLES")

for tbl in cur:
    print(tbl)

# cur.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# cur.execute("INSERT INTO customers (name, address) VALUES ('naresh', 'delhi')")
# cur.execute("UPDATE customers SET address='hyd' WHERE id=5")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
# cur.executemany(sql,val)
# mydb.commit()
# cur.execute("SELECT * FROM customers")
# cur.execute("SELECT name, id FROM customers")


# rows = cur.fetchall()


# for row in rows:
#     print(row)

# rows = cur.fetchone()
# print(rows)


# cur.execute("SELECT name, id FROM customers WHERE address='hyd'")
# cur.execute("SELECT name, address, id FROM customers WHERE address LIKE '%way%'")

# for d in cur:
#     print(d)

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# cur.execute(sql, adr)

# cur.execute("SELECT * FROM customers ORDER BY name DESC")
# res = cur.fetchall()

# for data in res:
#     print(data)

# cur.execute("DELETE FROM customers WHERE id=5")

# mydb.commit()