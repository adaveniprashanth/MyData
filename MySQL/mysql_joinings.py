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

#AUTOINCREMENT will work only when we use INTEGER PRIMARY KEY


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
if 0:
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
        ON DELETE CASCADE
        );''')
    #ON DELETE CASCADE helps to delete the data from orders if we delete the corresponding customer
    # from customers table
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
    ('2006-03-12',234.32,2),
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
    if 0:#using EXPLICIT INNER JOIN logic i.e it prints prints the data present in both tables
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
        if 0:#priniting the values from both tables in date ascending order
            print("priniting the values from both tables in amount ascending date")
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM orders INNER JOIN customers 
            ON customers.id = orders.customer_id ORDER BY order_date;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#finding the total spent by the customer for purchasing the orders
            data = cursor.execute('''
            SELECT first_name,last_name,SUM(amount) AS total_spent FROM customers JOIN orders
             ON orders.customer_id = customers.id GROUP BY orders.customer_id ORDER BY total_spent DESC;
            ''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
    if 0:#LEFT JOIN. It prints the data in left table and present in both tables but not in the right table
        if 0:#prints the data present in left table(customers) but not in right table(orders)
            data = cursor.execute('''SELECT * FROM customers LEFT JOIN orders ON customers.id=orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#printing the customers and orders from tables
            data = cursor.execute('''SELECT first_name,last_name,order_date,amount FROM customers LEFT JOIN orders
             ON customers.id = orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#printing the customers and total amount spend in orders
            data = cursor.execute('''SELECT first_name,last_name,order_date,SUM(amount) FROM customers LEFT JOIN orders
             ON customers.id = orders.customer_id GROUP BY customers.id ORDER BY SUM(amount);''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#printing the customers and total amount spend in orders and checking any customer amount is None
            data = cursor.execute('''SELECT first_name,last_name,order_date,IFNULL(SUM(amount),0) AS total_spent FROM customers LEFT JOIN orders
             ON customers.id = orders.customer_id GROUP BY customers.id ORDER BY total_spent;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#printing the customers and total amount spend in descending order
            data = cursor.execute('''SELECT first_name,last_name,order_date,IFNULL(SUM(amount),0) AS total_spent FROM customers LEFT JOIN orders
             ON customers.id = orders.customer_id GROUP BY customers.id ORDER BY total_spent DESC;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
    if 1:#RIGHT JOIN. It gives the output from the right table and present in both tablesi.e total right table
        #currently RIGHT JOIN and FULL OUTER JOIN are not supporting by sqlite3 library
        #but we can peform by switching the tables from left to right and right to left
        if 0:#printing all the values from tight table
            data = cursor.execute('''SELECT * FROM customer RIGHT JOIN orders ON customers.id=orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#printing all the values from tight table
            data = cursor.execute('''SELECT IFNULL(first_name,'missing') AS first_name,
            IFNULL(last_name,'missing') AS last_name,order_date,amount FROM customers RIGHT JOIN orders ON customers.id=orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
        if 0:#printing all the values from left table. i mean reverse tables positions with LEFT JOIN
            print("printing the orders given by the customers some times we may get orders from missing persons also")
            data = cursor.execute('''SELECT IFNULL(first_name,'missing') AS first_name,
            IFNULL(last_name,'user') AS last_name,order_date,amount FROM orders LEFT JOIN customers ON customers.id=orders.customer_id;''')
            names = [i[0] for i in data.description]
            print(names)
            for i in cursor:
                print(i)
# Exercise on Joints
if 0:
    cursor.execute("PRAGMA foreign_keys = ON;")  # need to enable the foreign key
    cursor.execute('''DROP TABLE IF EXISTS students;''')
    cursor.execute('''DROP TABLE IF EXISTS papers;''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,first_name VARCHAR(100));''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS papers(
    id INTEGER PRIMARY KEY,title VARCHAR(20),
    grade INT,student_id INT,
    FOREIGN KEY(student_id) REFERENCES students(id)ON DELETE CASCADE);''')
    cursor.execute('''INSERT OR IGNORE INTO students
    (first_name) VALUES
    ('raju'),('ramu'),
    ('kalyan'),('pawan'),('samantha');''')
    cursor.execute('''INSERT OR IGNORE INTO papers
    (title,grade,student_id) VALUES
    ('maths',50,1),('science',56,1),
    ('english',60,2),('hindi',70,2),('telugu',76,4);''')

    if 0:#printing total data
        data=cursor.execute('''SELECT * FROM students;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
        data = cursor.execute('''SELECT * FROM papers;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#INNER JOIN
        data = cursor.execute('''SELECT first_name,title,grade FROM students INNER JOIN papers 
        ON papers.student_id=students.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#LEFT JOIN
        data = cursor.execute('''SELECT first_name,title,grade FROM students LEFT JOIN papers 
        ON papers.student_id=students.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#LEFT JOIN
        data = cursor.execute('''SELECT first_name,IFNULL(title,'MISSING') AS title,IFNULL(grade,0) AS grade FROM students LEFT JOIN papers 
        ON papers.student_id=students.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:##printing the result of each student
        data = cursor.execute('''SELECT first_name,AVG(IFNULL(grade,0)) AS average FROM students LEFT JOIN papers 
        ON papers.student_id=students.id GROUP BY students.id ORDER BY average DESC;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing the result status of each student
        data = cursor.execute('''SELECT first_name,
        CASE
            WHEN AVG(IFNULL(grade,0)) >= 50 THEN 'PASSING'
            ELSE 'FAILING'
        END AS passing_status FROM students LEFT JOIN papers 
                ON papers.student_id=students.id GROUP BY students.id ORDER BY passing_status DESC;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

if 1:#MANY-MANY Relationship
    #Example is series(marvel) ratings from the customers
    #so it needs 3 tables.
    # 1.customers table to store customer name and other details
    # 2.series table to store what are the series are playing and which year etc.
    # 3.reviews table to store the reviews of customers for the series
    cursor.executescript('''DROP TABLE IF EXISTS marvel_movies;
                      DROP TABLE IF EXISTS customers;
                      DROP TABLE IF EXISTS ratings;''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS marvel_movies
    (id INTEGER PRIMARY KEY,movie_name VARCHAR(100),
     released_year YEAR(4),genre VARCHAR(30));''')
    #YEAR(4) means it supports from 0000 to 9999 years only
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers
    (id INTEGER PRIMARY KEY,first_name VARCHAR(100),last_name VARCHAR(100));''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings
    (id INTEGER PRIMARY KEY,rating DECIMAL(2,1),movie_id INT,customer_id INT,
    FOREIGN KEY(movie_id) REFERENCES marvel_movies(id),
    FOREIGN KEY(customer_id) REFERENCES customers(id)
    ON DELETE CASCADE);''')

    #adding data into tables
    cursor.execute('''INSERT OR IGNORE INTO marvel_movies
    (movie_name,released_year,genre) VALUES
    ('avengers',2003,'fantasy'),('iron man',2004,'action'),
    ('black panther',2007,'wonder'),('wakanda',2009,'sci-fi'),
    ('guardians',2011,'sci-fi'),('spyder man',2006,'fantasy'),
    ('fantastic',2009,'funny'),('captain america',2011,'action'),
    ('the mask',2019,'funny'),('captain marvel',2017,'action');''')

    cursor.execute('''INSERT OR IGNORE INTO customers
    (first_name,last_name) VALUES
    ('raj','kumar'),('ramesh','yadav'),
    ('narsing','yadav'),('pavan','kalyan'),
    ('kalyan','kumar'),('suraj','varma');''')

    cursor.execute('''INSERT OR IGNORE INTO ratings
    (customer_id,movie_id,rating) VALUES
    (3,4,4.5),(2,6,5.4),(1,5,7.7),(5,7,7.7),(3,8,8.9),(2,7,3.4),(2,4,6.5),
    (1,6,8.7),(4,3,5.5),(5,7,6.7),(3,7,7.6),(2,7,8.7),(4,6,8.8),(5,4,7.7),
    (2,6,8.9),(3,6,7.6),(2,7,8.8),(3,2,7.4),(1,1,7.5),(3,2,7.7),(3,7,8.9);''')

    if 0:
        #printing the data present in tables
        data= cursor.execute('''SELECT * FROM marvel_movies;''')
        names=[i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
        data = cursor.execute('''SELECT * FROM customers;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
        data = cursor.execute('''SELECT * FROM ratings;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing the data
        data = cursor.execute('''SELECT * FROM marvel_movies JOIN ratings ON ratings.movie_id=marvel_movies.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing the movie name and rating from data
        data = cursor.execute('''SELECT movie_name,rating FROM marvel_movies JOIN ratings ON ratings.movie_id=marvel_movies.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#printing the movie name and average rating of movie from data
        data = cursor.execute('''SELECT movie_name,AVG(IFNULL(rating,0)) AS average_rating 
        FROM marvel_movies JOIN ratings
         ON ratings.movie_id=marvel_movies.id
          GROUP BY marvel_movies.id ORDER BY average_rating ASC;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#priniting the customer names and their reviews for the movies they gave
        data = cursor.execute('''SELECT first_name,last_name,rating FROM customers JOIN ratings
        ON customers.id = ratings.customer_id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#printing the movies which has no ratings
        data = cursor.execute(''' SELECT movie_name AS unreviewed_movie,rating FROM marvel_movies LEFT JOIN ratings 
        ON marvel_movies.id=ratings.movie_id WHERE rating IS NULL;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:# printing the average rating of each genre
        data = cursor.execute(''' SELECT genre,AVG(IFNULL(rating,0)) AS average_rating 
        FROM marvel_movies INNER JOIN ratings 
        ON marvel_movies.id=ratings.movie_id GROUP BY genre;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:# printing the average rating round off to 2 values of each genre
        data = cursor.execute(''' SELECT 
        genre,
        ROUND(
        AVG(IFNULL(rating,0)),2) AS average_rating 
        FROM marvel_movies INNER JOIN ratings 
        ON marvel_movies.id=ratings.movie_id GROUP BY genre;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#printing the customer name, his max,min average ratings and his status
        data = cursor.execute('''SELECT 
        first_name||' '||last_name AS full_name,
        COUNT(rating) AS count,
        IFNULL(MAX(rating),0) AS max_rating,
        IFNULL(MIN(rating),0) AS min_rating,
        ROUND(AVG(IFNULL(rating,0)),2) AS avg_rating,
        CASE 
            WHEN COUNT(rating) > 0 THEN 'Active'
            ELSE 'Inactive'
        END AS 'customer_status'
        FROM customers LEFT JOIN ratings
        ON customers.id = ratings.customer_id
        GROUP BY customers.id;
        ''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing the customer name, his max,min average ratings and his status
        #using IF logic.************  Note:it is not working
        data = cursor.execute('''SELECT 
        first_name||' '||last_name AS full_name,
        COUNT(rating) AS count,
        IFNULL(MAX(rating),0) AS max_rating,
        IFNULL(MIN(rating),0) AS min_rating,
        ROUND(AVG(IFNULL(rating,0)),2) AS avg_rating,
        IF(COUNT(rating) > 0, 'Active','Inactive') AS 'customer_status'      
        FROM customers LEFT JOIN ratings
        ON customers.id = ratings.customer_id
        GROUP BY customers.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 1:#printing the movie name, customer rating and customer name
        data = cursor.execute(''' SELECT movie_name,rating,first_name||' '||last_name AS full_name
        FROM marvel_movies INNER JOIN ratings ON marvel_movies.id = ratings.movie_id
        INNER JOIN customers ON ratings.customer_id = customers.id
        ORDER BY marvel_movies.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

#handler close
cursor.close()

#close database connection
database.close()
