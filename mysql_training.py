print("welcome to sql training")
import sqlite3

#******The below commands we cannot run using sqlite3 module
'''
show databases;  <-- to list the databases in server
SHOW TABLES; <-- to diaplay the tables in database
SHOW COLUMNS FROM <table name> --< to display the columns from table
CREATE DATABSE <DB name>;  <-- to create a database in server
DROP DATABASE <DB_name>;  <-- to delete the databse
USE <DB Name> <-- to use that databse to create tables and run queries
SELECT database(); <-- to display which database is currently using
select @@hostname; <-- to check the hostname
SHOW WARNINGS; <-- to dislpay the warnings
'''

'''
MySQL and SQL may have different data types.
MySQL data types:
a.numaric types:
    1.INT(+ve,-ve and 0) 2.SMALLINT 3.TINYINT 4.MEDIUMINT 5.BIGINT 6.DECIMAL 7.NUMERIC 8.FLOAT 9.DOUBLE 10.BIT
b.string types:
    1.CHAR(fixed length of characters) 2.VARCHAR(1-255 characters) 3.BINARY 4.VARBINARY 5.BLOB 6.TINYBLOB 7.MEDIUMBLOB 8.LONGBLOB 
    9.LONGBLOB 10.TEXT 11.TINYTEXT 12.MEDIUMTEXT 13.LONGTEXT 14.ENUM
c.date types:
    1.DATE 2.DATETIME 3.TIMESTAMP 4.TIME 5.YEAR
'''


# Connect to DB if exists or else create new database
database = sqlite3.connect('database.db')

print("Opened database successfully")

#create a handle for database
cursor = database.cursor()

#deleting tables
cursor.execute("DROP TABLE IF EXISTS company;")
cursor.execute("DROP TABLE IF EXISTS cakes;")
cursor.execute("DROP TABLE IF EXISTS people;")
cursor.execute("DROP TABLE IF EXISTS employees;")
cursor.execute("DROP TABLE IF EXISTS hostels;")
cursor.execute("DROP TABLE IF EXISTS shirts;")

#CRUD OPERATIONS
###################################################################
#CREATE operations:

#primary key is an unique identifier. we can make multiple columns as primary key to avoid duplicate values
#CREATE TABLE IF NOT EXIST <table_name> (column1 datatype other_params(NOT NULL,PRIMARY), column1 datatype);
cursor.execute('''CREATE TABLE IF NOT EXISTS company
         (ID INT PRIMARY KEY     NOT NULL DEFAULT 0,
         NAME           TEXT    NOT NULL DEFAULT "no name",
         AGE            INT     NOT NULL DEFAULT 99,
         ADDRESS        CHAR(50) DEFAULT "bng",
         SALARY         REAL DEFAULT 0.0);''')
         
#insert data into table (multi line query)
cursor.execute('''INSERT OR IGNORE INTO company (ID,NAME,AGE,ADDRESS,SALARY)
      VALUES (1, 'Paul', 32, 'California', 20000.00 );''')
#single line query
cursor.execute("INSERT OR IGNORE INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 );")
cursor.execute("INSERT OR IGNORE INTO company (ID,NAME,ADDRESS) VALUES (3, 'Allen', 'Texas');")
cursor.execute("INSERT OR IGNORE INTO company (ID) VALUES (4);") #no error due to default values and primary key must to provide
cursor.execute("INSERT OR IGNORE INTO company (ID,ADDRESS) VALUES (5,NULL);") #no error due to address accepts null value also

#multiple queries at single time
cursor.executescript('''INSERT OR IGNORE INTO company (ID,NAME,AGE,ADDRESS,SALARY) 
      VALUES (6, 'Teddy', 23, 'Norway', 20000.00 );
      INSERT OR IGNORE INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES (7, 'Mark', 25, 'Rich-Mond ', 65000.00 );''')

#skipping some column values  while insert due to default value in column
cursor.execute("INSERT OR IGNORE INTO company (ID,NAME,AGE,ADDRESS) VALUES (8,'Marktwin', 35, 'Rich-Monds');")

# print("Records created successfully")
if 0:
    #display the data in tables
    print("\ndisplay the data from company table")
    cursor.execute("SELECT * FROM company")
    for i in cursor:
        print(i)

#primary key is an unique identifier we can have multiple columns with PRIMARY KEY
cursor.execute('''CREATE TABLE IF NOT EXISTS cakes ( ID INT NOT NULL, NAME VARCHAR(100), QUANTITY INT,PRIMARY KEY (ID));''')
                
cursor.executescript('''INSERT OR IGNORE INTO cakes (ID,NAME,QUANTITY) VALUES (1,'honey',40);
                        INSERT OR IGNORE INTO cakes (ID,NAME,QUANTITY) VALUES (2,'choco',10);
                        INSERT OR IGNORE INTO cakes (ID,QUANTITY,NAME) VALUES (3,11,'berry');
                    ''')

#multiple values insert command
cursor.execute("INSERT OR IGNORE INTO cakes (ID,NAME,QUANTITY) VALUES (4,'chocolate',1),(5,'cream',3),(6,'butterscotch',5);")

if 0:
    print("\ndisplay the data from cakes table")
    cursor.execute("SELECT * FROM cakes")
    for i in cursor:
        print(i)

#AUTO INCREMENT the value. Note: AUTO_INCREMENT and NOT NULL should not be at same time.
# if we decide to make column as primary key we have to give PRIMARY KEY at the end.
#we cannot use AUTO_INCREMENT in sqlite3 but we can make it work by using INTEGER and PRIMARY KEY
cursor.execute("CREATE TABLE IF NOT EXISTS people (ID INTEGER PRIMARY KEY, first_name VARCHAR(10), last_name VARCHAR(20), age INTEGER);")
cursor.executescript('''INSERT OR IGNORE INTO people(first_name,last_name,age) VALUES ('raj','kumar',20),('prashanth','pj',12);
                        INSERT OR IGNORE INTO people(age,first_name,last_name) VALUES (12,'rajesh','kumar');
                        INSERT OR IGNORE INTO people(age,first_name,last_name) VALUES (20,'raja','kumari'),(23,'pss','selvam');
                        INSERT OR IGNORE INTO people(age,first_name,last_name) VALUES (23,'ps1','selva');''')
if 0:
    print("\ndisplay the data from people table")
    cursor.execute("SELECT * FROM people;")
    for i in cursor:
        print(i)

cursor.executescript('''
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY,
last_name VARCHAR(100) NOT NULL,
first_name VARCHAR(100) NOT NULL,
middle_name VARCHAR(100),
age INT NOT NULL,
current_status VARCHAR(25) NOT NULL DEFAULT "employed");
''')

cursor.execute('INSERT INTO employees (first_name,last_name,age) VALUES ("abc","def",25)')
if 0:
    print("printing from employees table")
    cursor.execute("SELECT * FROM employees")
    for i in cursor:
        print(i)

########################################
#READ operations:
cursor.executescript('''CREATE TABLE IF NOT EXISTS hostels(
                    id INTEGER NOT NULL PRIMARY KEY,
                    name VARCHAR(20) NOT NULL,
                    location VARCHAR(50) NOT NULL,
                    cost INT NOT NULL);''')
#CREATE operations:
cursor.executescript('''
INSERT OR IGNORE INTO hostels 
(name,location,cost) VALUES 
('lakshmi','agara',5000),
('srija','belandur',5500),
('raghu','silk board',4500),
('rajesh','agara',5000),
('ram','hsr',4500),
('kasi','intel',4500),
('kaasi','AGARA',5500),
('satya','kalamandir',5000);
''')
cursor.execute("INSERT OR IGNORE INTO hostels (cost,name,location) VALUES(5500,'ramya','belandur');")

#READ operation
if 0:
    if 0:
        print("print data from hostels table")
        print("read all columns from table")
        cursor.execute("SELECT * FROM hostels;")
        for i in cursor:
            print(i)
    if 0:
        print("specific column from table")
        cursor.execute("SELECT name FROM hostels;")
        for i in cursor:
            print(i)
    if 0:
        print("specific columns from table")
        cursor.execute("SELECT name,location FROM hostels;")
        for i in cursor:
            print(i)

        cursor.execute("SELECT cost,name,location FROM hostels;")
        for i in cursor:
            print(i)

    # WHERE clause
    if 0:
        cursor.execute("SELECT * FROM hostels WHERE cost = 5000; ")
        for i in cursor:
            print(i)
        print("location column")
        cursor.execute("SELECT * FROM hostels WHERE location = 'agara'; ")
        for i in cursor:
            print(i)
    if 0:
        print("location again")
        cursor.execute("SELECT * FROM hostels WHERE location = 'AGARA'; ")
        for i in cursor:
            print(i)
        cursor.execute("SELECT name,location from hostels WHERE location ='agara';")
        for i in cursor:
            print(i)

    #Alias usage
    if 0:
        print("alias usage")
        cursor.execute("SELECT name,location as address FROM hostels WHERE location = 'agara'; ")
        for i in cursor:
            print(i)
        print("multiple aliases")
        cursor.execute("SELECT name AS hostel_name,location AS address FROM hostels WHERE cost=4500; ")
        for i in cursor:
            print(i)
#UPDATE operations:
if 0:
    if 0:
        cursor.execute("UPDATE hostels SET cost=6000 WHERE location = 'AGARA';")
        cursor.execute("SELECT * FROM hostels; ")
        for i in cursor:
            print(i)
    if 0:
        # print("location change")
        cursor.execute("UPDATE hostels SET location =='marathalli' WHERE location='hsr';")
        cursor.execute("SELECT * FROM hostels;")
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("UPDATE hostels SET cost=6000 WHERE name ='ram';")
        cursor.execute("SELECT * FROM hostels WHERE name ='ram';")
        for i in cursor:
            print(i)

    print("name change")
    cursor.execute("UPDATE hostels SET name ='ram karthik' WHERE name ='ram';")
    cursor.execute("SELECT * FROM hostels;")
    for i in cursor:
        print(i)

# DELETE operations:
if 0:
    print("printing all items")
    cursor.execute("SELECT *FROM hostels;")
    for i in cursor:
        print(i)
    if 0:
        cursor.execute("DELETE FROM hostels WHERE location ='AGARA';")
        print("printing after removal")
        cursor.execute("SELECT *FROM hostels;")
        for i in cursor:
            print(i)
    if 0:
        print("deleting items based on cost")
        cursor.execute("DELETE FROM hostels WHERE cost=5500;")
        print("printing after removal")
        cursor.execute("SELECT *FROM hostels;")
        for i in cursor:
            print(i)
    if 0:
        print("deleting all cats")
        cursor.execute("DELETE FROM hostels;")
        print("printing after removal")
        cursor.execute("SELECT *FROM hostels;")
        for i in cursor:
            print(i)

# CRUD Exercise
if 0:
    # creating a table
    cursor.executescript('''CREATE TABLE IF NOT EXISTS shirts(
                            shirt_id INTEGER NOT NULL PRIMARY KEY,
                            article VARACHAR(25),
                            color VARCHAR(25),
                            shirt_size VARCHAR(10),
                            last_worn INTEGER);''')
    # CREATE operation i.e data creation
    if 1: #this has to be True always
        cursor.executescript('''INSERT OR IGNORE INTO shirts
                                (article,color,shirt_size,last_worn) 
                        VALUES  ('t-shirt','white','S',10),('t-shirt','green','S',200),
                                ('polo shirt','black','M',10),('tank top','blue','S',50),
                                ('t-shirt','pink','S',0),('polo shirt','red','M',5),
                                ('tank top','white','S',200),('tank top','blue','M',15)
                            ''')
        if 0:
            print("printing all the shirts")
            cursor.execute("SELECT *FROM shirts;")
            for i in cursor:
                print(i)
        if 1: #this has to be True always
            #print("adding new shirt purple color polo shirt with size of Medium worn 50 days back")
            cursor.execute("INSERT OR IGNORE INTO shirts (color,article,shirt_size,last_worn) VALUES ('purple','polo shirt','M',50)")
        if 0:
            print("checking the addition")
            cursor.execute("SELECT *FROM shirts WHERE color = 'purple';")
            for i in cursor:
                print(i)

    # READ operation
    if 0:
        #reading all shirts and colors
        print("reading all shirts and colors")
        cursor.execute("SELECT article,color FROM shirts;")
        for i in cursor:
            print(i)
    if 0:
        print("reading all shirts with size Medium but not shirt_id ")
        cursor.execute("SELECT article,color,shirt_size,last_worn FROM shirts WHERE shirt_size='M';")
        for i in cursor:
            print(i)
    # UPDATE operation
    if 0:
        print("updating all polo shirts size to Large")
        cursor.execute("UPDATE shirts SET shirt_size='L' WHERE article='polo shirt';")
        # cursor.execute("SELECT * FROM shirts WHERE article = 'polo shirt';")
        # for i in cursor:
        #     print(i)
    if 0:
        print("change the last_worn to 0 which are having 15 days last_worn")
        cursor.execute("SELECT * FROM shirts WHERE last_worn = 15;")
        for i in cursor:
            print(i)
        cursor.execute("UPDATE shirts SET last_worn = 0 WHERE last_worn = 15;")
        cursor.execute("SELECT * FROM shirts;")
        for i in cursor:
            print(i)
    if 0:
        print("changing 2 params at a time")
        cursor.execute("SELECT * FROM shirts WHERE color = 'white';")
        for i in cursor:
            print(i)
        print("changing the color and size of white shirt")
        cursor.execute("UPDATE shirts SET color='off white',shirt_size='XS' WHERE color='white';")
        cursor.execute("SELECT * FROM shirts;")
        for i in cursor:
            print(i)
    #DELETE operation
    if 1:
        print("printing all old shirts")
        cursor.execute("SELECT * FROM shirts WHERE last_worn =200;")
        for i in cursor:
            print(i)
        print("deleting all old shirts")
        cursor.execute("DELETE FROM shirts WHERE last_worn=200;")
        cursor.execute("SELECT * FROM shirts WHERE last_worn =200;")
        for i in cursor:
            print(i)
    if 1:
        print("printing all tank tops")
        cursor.execute("SELECT * FROM shirts WHERE article='tank top';")
        for i in cursor:
            print(i)
        print("deleting all tank tops")
        cursor.execute("DELETE FROM shirts WHERE article='tank top';")
        cursor.execute("SELECT * FROM shirts WHERE article='tank top';")
        for i in cursor:
            print(i)
    if 1:
        print("printing all remaining shirts")
        cursor.execute("SELECT * FROM shirts;")
        for i in cursor:
            print(i)
        print("deleting all shirts")
        cursor.execute("DELETE FROM shirts;")
        cursor.execute("SELECT * FROM shirts;")
        for i in cursor:
            print(i)




#handler close
cursor.close()

#close database connection
database.close()
