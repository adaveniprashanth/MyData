print("welcome to sql training")
import sqlite3
# For reference--> https://www.w3resource.com/sqlite/core-functions-replace.php for string methods
# for reference --> https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-datetime-function/
# For reference --> https://www.w3resource.com/sqlite/index.php
# For reference --> https://learnsql.com/cookbook/how-to-get-day-names-in-sqlite/
# For reference --> https://learnsql.com/cookbook/how-to-calculate-the-difference-between-two-dates-in-sqlite/
# python code for running the commands:
# sql='SELECT x FROM myTable WHERE x LIKE %s'
# args=[beginningOfString+'%']
# cursor.execute(sql,args)

# beginningOfString += '%'
# cursor.execute("SELECT x FROM myTable WHERE x LIKE ?", (beginningOfString,) )

# Connect to DB if exists or else create new database
database = sqlite3.connect('database1.db')
# <databasehandle>.create_function(<function name>,no.of arguments,operation)
database.create_function("strrev", 1, lambda s: s[::-1])
print("Opened database successfully")

#create a handle for database
cursor = database.cursor()

#deleting tables
cursor.execute("DROP TABLE IF EXISTS company;")
cursor.execute("DROP TABLE IF EXISTS customers;")
cursor.execute("DROP TABLE IF EXISTS orders;")

if 0: #REVERSE Method --> strrev(string)
    # <databasehandle>.create_function(<function name>,no.of arguments,operation)
    database.create_function("strrev", 1, lambda s: s[::-1])
    cursor.execute("SELECT strrev(first_name) AS 'short_name' FROM organisation;")
    for i in cursor:
        print(i)

if 0:
    # cursor.execute("source create_table.sql;")
    #cursor.execute("source <sql file name>") #this method will be done in other way.
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    commands = split_commands(file)
    execute_commands(commands)
    print("printing the values")
    for i in cursor:
        print(i)

# Types of relationships:
# 1-1 Relationship--> single user can give single rating
#1-Many Relationship--> book can have many ratings
# Many - Many Relationship--> each book can be written by multiple authors or
# multiple authors can write multiple books

# ONE-MANY Relationship
if 1:
    cursor.execute("PRAGMA foreign_keys = ON;")#need to enable the foreign key
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
    );''')
    # mapping the customer table id column with orders table customer_id using FOREIGN KEY
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_date DATE,
        amount DECIMAL(8,2),
        customer_id INT,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
        );''')
    cursor.execute('''INSERT OR IGNORE INTO customers
    (first_name,last_name,email) VALUES
    ('raj','kumar','raju@gmail.com'),
    ('pawan','kalyan','pavan@gmail.com'),
    ('rajesh','kumar','rajesh@gmail.com'),
    ('ramesh','yadav','rummy2gmail.com'),
    ('raju','bhai','raja@gmail.com');
    ''')
    data = cursor.execute('''SELECT * FROM customers;''')
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    cursor.execute('''INSERT OR IGNORE INTO orders
    (order_date,amount,customer_id) VALUES
    ('2020-12-30',45.45,1),
    ('2012-11-20',34.23,2),
    ('1980-12-21',93.32,5),
    ('1980-11-31',98.32,5),
    ('1980-12-31',98.32,1),
    ('2006-03-12',234.32,3),
    ('2002-12-12',23.32,4);
    ''')
    data = cursor.execute('''SELECT * FROM orders;''')
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    if 0:#it will fail because we have enabled foreign key using cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT OR IGNORE INTO orders
            (order_date,amount,customer_id) VALUES('2003-12-23',54.34,98);''')
        data = cursor.execute('''SELECT * FROM orders;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#getting the details from 2 tables without using JOIN
        data = cursor.execute('''SELECT * FROM orders WHERE customer_id =
        (SELECT id FROM customers WHERE first_name = 'raj');''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#using CROSS JOIN logic
        # it will map all the customers with all the orders
        data = cursor.execute('''SELECT * FROM orders,customers;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#using IMPLICIT INNER JOIN logic
        if 0:
            data = cursor.execute('''SELECT * FROM customers,orders WHERE customers.id = orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 1:
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM customers,orders WHERE customers.id = orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
    if 1:#using EXPLICIT INNER JOIN logic
        if 0:
            data = cursor.execute('''SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#priniting the values from both tables
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM customers JOIN orders ON customers.id = orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#priniting the values from both tables
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM orders JOIN customers ON customers.id = orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#priniting the values from both tables in amount ascending order
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM orders JOIN customers 
            ON customers.id = orders.customer_id ORDER BY amount;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#priniting the values from both tables in date ascending order
            print("priniting the values from both tables in amount ascending date")
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM orders JOIN customers 
            ON customers.id = orders.customer_id ORDER BY order_date;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 1:#finding the total spent by the customer for purchasing the orders
            data = cursor.execute('''
            SELECT first_name,last_name,SUM(amount) AS total_spent FROM customers JOIN orders
             ON orders.customer_id = customers.id GROUP BY orders.customer_id ORDER BY total_spent DESC;
            ''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)







#handler close
cursor.close()

#close database connection
database.close()
