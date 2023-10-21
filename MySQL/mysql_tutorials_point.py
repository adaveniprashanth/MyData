import mysql.connector

# connecting to mysql database
connection = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  # database="filmfare"
)
cursor = connection.cursor()# creating the cursor object
cursor.execute("SHOW DATABASES;")
for i in cursor:
    print(i)
