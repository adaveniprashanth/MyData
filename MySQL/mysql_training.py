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
source <sql file name>  <-- it will work only in mysql CLI environment only
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
# <databasehandle>.create_function(<function name>,no.of arguments,operation)
database.create_function("strrev", 1, lambda s: s[::-1])
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

#CRUD OPERATION
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
# Create Table
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
# Getting column names of table
# To use cursor.description, you have to fetch at least one row from table.
# names = [description[0] for description in cursor.description]
# print(names)

#READ operation
if 0:
    if 0:
        print("print data from hostels table")
        print("read all columns from table")
        cursor.execute("SELECT * FROM hostels;")
        for i in cursor:
            print(i)
        # Getting column names of table
        names = [description[0] for description in cursor.description]
        print(names)
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


# loading the commands from file
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

    file = 'create_table.sql'  # commands in the file should be in single line only
    commands = split_commands(file)
    execute_commands(commands)
    print("printing the values")
    for i in cursor:
        print(i)

# SQL string functions
if 0:
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    for i in cursor:
        print(i)

    if 0:
        # CONCAT method and using Alias concept also.Note: CONCAT is not supporting
        # cursor.execute("SELECT CONCAT(first_name,' ',last_name) FROM organisation;")
        # cursor.execute("SELECT CONACT_WS(' ',first_name,last_name) FROM organisation;")
        cursor.execute("SELECT first_name||' '||last_name AS 'employee_details' FROM organisation;")
        for i in cursor:
            print(i)
        print("priniting the column names")
        names = [description[0] for description in cursor.description]
        print(names)
        print("without alias")
        cursor.execute("SELECT first_name||' '||last_name FROM organisation;")
        for i in cursor:
            print(i)
    if 0:
#         SUBSTRING Method--> substr('string',start,end) or substr('string',start)
        print("with starting and end positions")
        cursor.execute("SELECT substr(first_name,1,4) FROM organisation;")
        for i in cursor:
            print(i)
        print("with starting position only")
        cursor.execute("SELECT substr(first_name,1) FROM organisation;")
        for i in cursor:
            print(i)

        print("with negative indexing")
        cursor.execute("SELECT SUBSTR(first_name,-5) FROM organisation;")
        for i in cursor:
            print(i)

        print("using SUBSTR and concat methods together")
        cursor.execute("SELECT SUBSTR(first_name,1,10)||'...' AS 'short_name' FROM organisation;")
        for i in cursor:
            print(i)
    if 0: #RELPACE Method --> RELPACE(string, sub_string,replace_with)
        print("using REPLACE method")
        cursor.execute("SELECT REPLACE(first_name,'A','a') 'short_name' FROM organisation;")
        for i in cursor:
            print(i)
        print("using REPLACE and SUBSTR methods together")
        cursor.execute("SELECT REPLACE(SUBSTR(first_name,1,5),'A','a') AS 'short_name' FROM organisation;")
        for i in cursor:
            print(i)
        print("using REPLACE and SUBSTR and concat methods together")
        cursor.execute("SELECT REPLACE(SUBSTR(first_name,1,5),'A','a')||'...' AS 'short_name' FROM organisation;")
        for i in cursor:
            print(i)
    if 0: #REVERSE Method --> strrev(string)
        # <databasehandle>.create_function(<function name>,no.of arguments,operation)
        database.create_function("strrev", 1, lambda s: s[::-1])
        cursor.execute("SELECT strrev(first_name) AS 'short_name' FROM organisation;")
        for i in cursor:
            print(i)
    if 0:#CHAR_LENGTH Method --> length(string)
        cursor.execute("SELECT last_name,length(last_name) AS 'length' FROM organisation;")
        for i in cursor:
            print(i)
        print("using CHAR_LENGTH and concat methods together")
        cursor.execute("SELECT last_name||' is '||length(last_name)||' characters long ' AS 'length' FROM organisation;")
        for i in cursor:
            print(i)
    if 0: #UPPER nad LOWER methods --> upper(string),LOWER(string)
        cursor.execute("SELECT UPPER(first_name) FROM organisation;")
        for i in cursor:
            print(i)
        cursor.execute("SELECT LOWER(first_name) FROM organisation;")
        for i in cursor:
            print(i)
        print("using lower and concat methods together")
        cursor.execute("SELECT 'My favourite name is '||LOWER(last_name) FROM organisation;")
        for i in cursor:
            print(i)
    if 0:#practice
        database.create_function("strrev", 1, lambda s: s[::-1])
        cursor.execute("SELECT UPPER(strrev('why does my cat looks so weird'))")
        for i in cursor:
            print(i)
        cursor.execute("SELECT REPLACE('I'||' '||'like'||' '||'cats',' ','-');")
        for i in cursor:
            print(i)
        cursor.execute("SELECT REPLACE(first_name||' '||last_name,' ','-->') AS 'full name' FROM organisation;")
        for i in cursor:
            print(i)
        cursor.execute("SELECT first_name AS 'forward',strrev(first_name) AS 'backward' FROM organisation;")
        for i in cursor:
            print(i)
        cursor.execute("SELECT LOWER(first_name||' '||last_name) AS 'full name in lower case' FROM organisation;")
        for i in cursor:
            print(i)
        cursor.execute("SELECT first_name||' '||last_name||' was joined in '||joining_year AS 'blurb' FROM organisation;")
        for i in cursor:
            print(i)
        cursor.execute(
            "SELECT first_name||' '||last_name AS 'full name',length(first_name||' '||last_name) AS 'char. count' FROM organisation;")
        for i in cursor:
            print(i)
        print("full name,profession and salary")
        cursor.execute(
            "SELECT SUBSTR(first_name||' '||last_name,1,10)||'...' AS 'short name',profession AS 'Job','salary is '|| salary AS salary FROM organisation;")
        for i in cursor:
            print(i)
        print("priniting the column names")
        cursor.execute("SELECT * FROM organisation;")
        names = [description[0] for description in cursor.description]
        print(names)

# Refining selections like getting particular rows and particular order
if 0:
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    for i in cursor:
        print(i)

    if 0:#DISTINCT i.e getting unique values. like set in python
        cursor.execute("SELECT DISTINCT last_name FROM organisation;")
        for i in cursor:
            print(i)
        cursor.execute("SELECT DISTINCT joining_year FROM organisation;")
        for i in cursor:
            print(i)
        print("using concat with DISTINCT")
        cursor.execute("SELECT DISTINCT first_name||' '||last_name AS 'full name' FROM organisation;")
        for i in cursor:
            print(i)
        #The below is also same as the above. DISTINCt will work on whole items
        cursor.execute("SELECT DISTINCT first_name,last_name FROM organisation;")
        for i in cursor:
            print(i)
    if 0:#ORDER BY --> By default, it is ordered in ascending order
        print("ordered items in ascending order")
        cursor.execute("SELECT * FROM organisation ORDER BY joining_year;")
        for i in cursor:
            print(i)

        print("ordered items in descending order")
        cursor.execute("SELECT * FROM organisation ORDER BY joining_year DESC;")
        for i in cursor:
            print(i)

        print("ordered items based on positional of argument")
        cursor.execute(
            "SELECT first_name,last_name,salary FROM organisation ORDER BY 3;")#it will order based on salary
        for i in cursor:
            print(i)

        cursor.execute(
            "SELECT first_name,last_name,salary FROM organisation ORDER BY 1 DESC;")#it will order in descending based on first name
        for i in cursor:
            print(i)

        # first it will order based on joining year and then that list will order again based on their salary
        cursor.execute(
            "SELECT first_name,last_name,joining_year,salary FROM organisation ORDER BY joining_year,salary;")
        for i in cursor:
            print(i)
    if 0:#LIMIT --> gives fixed no.of result instead of all matches we have to use it at the end of the query.
        # --> LIMIT starting row i.e from which row it has to start(optional), how many rows
        print("printing only 3 rows from table")
        cursor.execute("SELECT * FROM organisation LIMIT 3;")
        for i in cursor:
            print(i)
        print("printing the rows which are having low salaries and early joined")
        cursor.execute("SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary, joining_year LIMIT 5;")
        for i in cursor:
            print(i)
        print("printing the rows which are having high salaries and late joined")
        cursor.execute(
            "SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary DESC,joining_year DESC;")
        for i in cursor:
            print(i)
        print("printing the rows which are having high salaries and late joined 5 rows")
        cursor.execute(
            "SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary DESC,joining_year DESC LIMIT 5;")
        for i in cursor:
            print(i)
        print("printing the rows which are having high salaries and late joined 5 rows from start of the table")
        cursor.execute(
            "SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary DESC,joining_year DESC LIMIT 0,5;")
        for i in cursor:
            print(i)
        print("printing the rows which are having high salaries and late joined 5 rows from 2nd row of the table")
        cursor.execute(
            "SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary DESC,joining_year DESC LIMIT 1,5;")
        for i in cursor:
            print(i)
        print("printing the rows which are having high salaries and late joined from 11th row of the table to end of table")
        print("LIMIT 1,<very large number> to go to end of the list" )
        cursor.execute(
            "SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary DESC,joining_year DESC LIMIT 10 ,3214242354325436;")
        for i in cursor:
            print(i)
    if 1:#LIKE   --> pattern matching--> LIKE %<pattern>% -->% is wild card. it can support 0 or more characters
        # like '____'--> _ represents a single digit/character.
        # we can use \(escape char) to remove the properties of % and _ while searching for % and _ like. regular expression
        cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                                    VALUES ('rajesh_ayyer','kumar','ENGINEER',2006,30000,3),
                                                                           ('pawan%kalyan','kumar','ANALYST',2003,23000,2);''')
        print("searching which are having ST in their profession")
        cursor.execute("SELECT first_name,last_name,profession FROM organisation WHERE profession LIKE '%ST%';")
        for i in cursor:
            print(i)
        print("searching which are starting with S in their profession")
        cursor.execute("SELECT first_name,last_name,profession FROM organisation WHERE profession LIKE 'S%';")
        for i in cursor:
            print(i)
        print("searching which are ending with ER in their profession")
        cursor.execute("SELECT first_name,last_name,profession FROM organisation WHERE profession LIKE '%ER';")
        for i in cursor:
            print(i)
        if 0:#not performing well
            print("searching which are having % in their first_name")
            cursor.execute("SELECT first_name,last_name,profession FROM organisation WHERE first_name LIKE '%\%%';")
            for i in cursor:
                print(i)
            print("searching which are having _ in their first_name")
            cursor.execute("SELECT first_name,last_name,profession FROM organisation WHERE first_name LIKE '%\_%';")
            for i in cursor:
                print(i)

        print("searching which are having salary starts with 3")
        cursor.execute("SELECT first_name,last_name,profession,salary FROM organisation WHERE salary LIKE '3____';")
        for i in cursor:
            print(i)

if 0:#Exercise for refining functions
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    for i in cursor:
        print(i)

    print("selecting all first names which are having 'A' in their first_name")
    cursor.execute("SELECT first_name,last_name FROM organisation WHERE first_name LIKE '%A%';")
    for i in cursor:
        print(i)
    print("finding the high salary paid person in organisation")
    cursor.execute("SELECT first_name,last_name,salary FROM organisation ORDER BY salary DESC LIMIT 1;")
    for i in cursor:
        print(i)
    print("printing the details of recent joined employees ")
    cursor.execute("SELECT first_name||' '||last_name||'-'||joining_year AS 'summary'FROM organisation ORDER BY joining_year DESC LIMIT 3;")
    for i in cursor:
        print(i)
    print("finding the lowest salary paid persons in organisation")
    cursor.execute("SELECT first_name,last_name,salary FROM organisation ORDER BY salary LIMIT 3;")
    for i in cursor:
        print(i)
    print("finding the persons in organisation which are having low salary and early joined")
    cursor.execute("SELECT first_name,last_name,salary,joining_year FROM organisation ORDER BY salary,joining_year;")
    for i in cursor:
        print(i)

    print("printing full name in lastname alphabetical order")
    cursor.execute("SELECT 'My full name is '||first_name||' '||last_name AS 'yell' FROM organisation ORDER BY last_name;")
    for i in cursor:
        print(i)

# Aggregate Functions like count,sum, average etc.
if 0:
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,12000,2),
                                                                   ('kalyan','rajesh','ANALYST',2003,23000,2),
                                                                   ('kalyan','kumar','ENGINEER',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    for i in cursor:
        print(i)

    if 0:#COUNT--> COUNT(params)
        print("counting how many rows in table")
        cursor.execute("SELECT COUNT(*) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing how many unique first names in table")
        cursor.execute("SELECT COUNT(DISTINCT first_name) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing how many unique full names in table")#DISTINCT(first_name,last_name ) will not work.
        cursor.execute("SELECT COUNT(DISTINCT first_name||' '||last_name) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing how many first names contains A in table")  # DISTINCT(first_name,last_name ) will not work.
        cursor.execute("SELECT COUNT(first_name) FROM organisation WHERE first_name LIKE '%A%';")
        for i in cursor:
            print(i)
    if 0:#GROUP BY
        print("grouping the data by profession i.e how many are having which profession")
        cursor.execute('''SELECT profession, COUNT(*) FROM organisation GROUP BY profession ORDER BY COUNT(*) DESC,profession DESC;''')
        for i in cursor:
           print(i)
        print("grouping the data by joining year i.e how many are joined in which year")
        cursor.execute(
            '''SELECT first_name,last_name,joining_year, COUNT(*) FROM organisation GROUP BY joining_year ORDER BY COUNT(*) DESC,joining_year DESC;''')
        for i in cursor:
            print(i)
        cursor.execute('''
                    SELECT 'In '||profession||' '||COUNT(*)||' '||'are working' FROM organisation GROUP BY profession ORDER BY COUNT(*) DESC''')
        for i in cursor:
            print(i)

    if 0:#MIN/MAX ge6tting the min/max value from the selection
        print("printing the lowest paid person from the organisation")
        #it will gives only the first found minimum values related to search
        cursor.execute("SELECT first_name||' '||last_name,MIN(salary) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing the lowest paid person from the organisation in other way")
        cursor.execute('''SELECT first_name||' '||last_name,salary FROM organisation
                            WHERE salary=(SELECT MIN(salary) FROM organisation);''')
        for i in cursor:
            print(i)
        print("printing the lowest paid person from the organisation in another way")
        cursor.execute('''SELECT first_name||' '||last_name,salary FROM organisation ORDER BY salary LIMIT 1;''')
        for i in cursor:
            print(i)

        print("printing the highest paid person from the organisation")
        cursor.execute("SELECT first_name||' '||last_name,MAX(salary) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing the person who joined lately from the organisation")
        cursor.execute("SELECT first_name||' '||last_name,MAX(joining_year) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing the person who joined early from the organisation")
        cursor.execute("SELECT first_name||' '||last_name,MIN(joining_year) FROM organisation;")
        for i in cursor:
            print(i)
        print("printing the person who joined lately from the organisation with less salary")
        cursor.execute("SELECT first_name||' '||last_name,salary,joining_year FROM organisation ORDER BY joining_year DESC,salary ASC LIMIT 2;")
        for i in cursor:
            print(i)
        print("printing the person who joined lately from the organisation in the same year")
        cursor.execute(
            "SELECT first_name||' '||last_name,salary,joining_year FROM organisation GROUP BY joining_year;")
        for i in cursor:
            print(i)
        print("printing the highest paid person from each profession")
        cursor.execute(
            "SELECT first_name||' '||last_name,MAX(salary),profession FROM organisation GROUP BY profession;")
        for i in cursor:
            print(i)
    if 0:#SUM
        print("printing the total amount paying to the employees in organisation")
        cursor.execute('''SELECT SUM(salary) FROM organisation;''')
        for i in cursor:
            print(i)
        print("printing the amount paying to each profession ")
        cursor.execute("SELECT SUM(salary),profession FROM organisation GROUP BY profession;")
        for i in cursor:
            print(i)
    if 0:#AVG
        print("printing the average amount providing to each profession")
        cursor.execute("SELECT AVG(salary),profession FROM organisation GROUP BY profession;")
        for i in cursor:
            print(i)

#exercise for SUM,AVG,MIN,MAX functions
if 0:
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,12000,2),
                                                                   ('kalyan','rajesh','ANALYST',2003,23000,2),
                                                                   ('kalyan','kumar','ENGINEER',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    for i in cursor:
        print(i)

    print("printing the total no.of employees")
    cursor.execute("SELECT COUNT(*) FROM organisation;")
    for i in cursor:
        print(i)
    print("printing how many people joined in each year")
    cursor.execute("SELECT joining_year,COUNT(*) FROM organisation GROUP BY joining_year;")
    for i in cursor:
        print(i)
    print("printing the total salary paying to employees")
    cursor.execute("SELECT SUM(salary) FROM organisation;")
    for i in cursor:
        print(i)
    print("printing the average salary paying to each profession")
    cursor.execute("SELECT profession,AVG(salary) FROM organisation GROUP BY profession;")
    for i in cursor:
        print(i)
    print("printing the highest salary payee to each profession")
    cursor.execute("SELECT first_name||' '||last_name AS full_name,salary FROM organisation ORDER BY salary DESC LIMIT 1;")
    for i in cursor:
        print(i)
    print("printing the the people joined in each year and average salary of those people")
    cursor.execute(
        "SELECT joining_year,COUNT(*),AVG(salary) FROM organisation GROUP BY joining_year;")
    for i in cursor:
        print(i)

# Datatypes supported in MySQL
# string types
# CHAR --> fixed length and speed. if value not satisfies size, it adds spaces at the end of the value
# VARCHAR --> not fixed length and less speed.
if 0:#testing the CHAR and VARCHAR note:it is not working fine
    cursor.execute("DROP TABLE IF EXISTS dogs;")
    cursor.execute('''CREATE TABLE IF NOT EXISTS dogs(
                        name CHAR(3),
                        breed VARCHAR(5));''')
    cursor.execute('''INSERT OR IGNORE INTO dogs 
    (name,breed) VALUES
    ('abc','beaver'),
    ('tommy','kaggle'),
    ('sweetie','labradors');''')
    cursor.execute("SELECT * FROM dogs;")
    for i in cursor:
        print(i)
# Number types
# INT  --> DECIMAL(M,D)--> it means total M digits in the number and it can have D floating values
# in that M values ex:DECIMAL(5,2) 999.99 or 50000 0<M<65 and 0<D<30.
# DECIMAL datatypes used for small number and for correct precision values
# FLOAT, DOUBLE will be used for storing large values with approx. values.

# Testing the INTEGERS note:it is not working fine
if 0:#testing the CHAR and VARCHAR
    cursor.execute("DROP TABLE IF EXISTS items;")
    cursor.execute('''CREATE TABLE IF NOT EXISTS items(
                        name CHAR(3),
                        price DECIMAL(5,2));''')
    cursor.execute('''INSERT OR IGNORE INTO items
        (name,price) VALUES
        ('soap',12),
        ('chana',130.99),
        ('candle',12.9999),
        ('iron',465465345671),
        ('potato',1.9999);''')
    cursor.execute("SELECT * FROM items;")
    for i in cursor:
        print(i)
# Dates and Times
# DATE ('yyyy-mm-dd'), TIME('hh:mm:ss') and DATETIME('yyyy-mm-dd hh:mm:ss')
if 0:#testing the DATE,TIME and DATETIME
    if 0:#CURDATE()--> DATE()
        print("printing the today date")
        cursor.execute("SELECT DATE();")
        for i in cursor:
            print(i)
    if 0:#CURTIME()-->TIME()
        print("printing the today time")
        cursor.execute("SELECT TIME();")
        for i in cursor:
            print(i)
    if 0:#NOW()--> DATETIME()
        print("printing the today date and time in local format")
        cursor.execute("SELECT DATETIME();")
        for i in cursor:
            print(i)
    if 0:#NOW('now','localtime')--> DATETIME('now','localtime')
        print("printing the today date and time in UTC")
        cursor.execute("SELECT DATETIME('now','localtime');")
        for i in cursor:
            print(i)
    if 0:#DAYOFWEEK()
        print("printing the day of week")
        cursor.execute("SELECT strftime('%w','now');")#if it returns 6 means saturday
        for i in cursor:
            print(i)
    if 0:#DAYOFYEAR()
        print("printing the day of year")
        cursor.execute("SELECT strftime('%j','now');")  # if it returns 6 means saturday
        for i in cursor:
            print(i)
    if 0:#accessing the date, month and year from the given date
        print("accessing the date, month and year from the given date")
        cursor.execute("SELECT strftime('%Y %m %d','now');")
        for i in cursor:
            print(i)
    if 0:#accessing the hour, minute ,seconds and milliseconds from the given time
        print("accessing the hour, minute and second and milliseconds from the given time")
        cursor.execute("SELECT strftime('%H %M %S %s','now','localtime');")
        for i in cursor:
            print(i)
    if 1:#creation of table and it is always true
        # creating the posts table
        cursor.executescript('''
        DROP TABLE IF EXISTS posts;
        CREATE TABLE IF NOT EXISTS posts(
        name VARCHAR(100),
        posted_on DATE,
        posted_at TIME,
        posted DATETIME,
        changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')
        #current timestamp will gives current date&time

        cursor.execute(''' 
        INSERT OR IGNORE INTO posts
        (name,posted_on,posted_at,posted) VALUES
        ('raju','1983-11-25','02:44:33','1983-11-25 02:44:33'),
        ('ramesh','1993-12-12','12:34:53','1993-12-12 12:34:53'),
        ('ram','1995-10-30','11:54:13','1995-10-30 11:54:13'),
        ('kalyan','2005-11-23','09:44:11','2005-11-23 09:44:11')
        ''')
        #  adding the row in the post table using the DATE(),TIME() and DATETIME()
        cursor.execute(''' 
        INSERT OR IGNORE INTO posts
        (name,posted_on,posted_at,posted) VALUES
        ('mohan',DATE(),TIME(),DATETIME())''')
        data = cursor.execute("SELECT * FROM posts;")
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
        if 0:#accessing the date,month and year from full date format
            cursor.execute("SELECT strftime('%Y %m %d',posted_on) FROM posts;")
            for i in cursor:
                print(i)

        if 0:#accessing the hour,minute and second from full time format
            # Getting column names of table after reading the data from table
            # names = [description[0] for description in cursor.description]
            # print(names)
            data = cursor.execute("SELECT strftime('%H %M %S',posted_at) FROM posts;")
            print("data",data.description)
            for i in cursor:
                print(i)
        if 0:#priniting the year,month,date,dayof week,day of year,hour,minute,seconds and milliseconds
            data = cursor.execute('''
            SELECT strftime('%Y',posted) AS year,strftime('%m',posted) AS month,
                   strftime('%d',posted) AS date,strftime('%w',posted) AS 'day of week',
                   strftime('%W',posted) AS 'week number in year',strftime('%j',posted) AS 'dayofyear'
                   ,strftime('%H',posted) AS hour,strftime('%M',posted) AS minute,
                   strftime('%S',posted) AS second,strftime('%s',posted) AS millisecond
                    FROM posts;
            ''')
            print([i[0]for i in data.description])
            for i in cursor:
                print(i)
        if 0:#differences between the given dates
            # cursor.execute("SELECT DATEDIFF(DATE(),'12-12-2021');")#it will not work
            print("printing the difference of 2 days")
            cursor.execute('''
             SELECT JULIANDAY(DATE('now')) - JULIANDAY(DATE('now','+1 day'));''')
            for i in cursor:
                print(i)
            print("printing the difference of 2 days")
            cursor.execute('''
                         SELECT JULIANDAY(DATE('now','+1 day')) - JULIANDAY(DATE('now'));''')
            for i in cursor:
                print(i)
            print("printing the difference of 2 days with 2 different times")
            cursor.execute('''
                                     SELECT JULIANDAY(DATETIME('now','+1 day','+1 hour')) - JULIANDAY(DATETIME('now'));''')
            for i in cursor:
                print(i)
            print("printing the difference of 2 days with 2 different times")
            cursor.execute('''
                         SELECT DATETIME(JULIANDAY(DATETIME('now','+1 day','+1 hour')) - JULIANDAY(DATETIME('now')));''')
            for i in cursor:
                print(i)
        if 1:#updation of date and time
            if 0:
                print("printing the current date in utc")
                cursor.execute("SELECT DATE('now');")
                for i in cursor:
                    print(i)
                print("printing the current date in local time")
                cursor.execute("SELECT DATE('now','localtime');")
                for i in cursor:
                    print(i)
                print("adding 1 day to the current date")
                cursor.execute("SELECT DATE('now','+1 day','localtime');")
                for i in cursor:
                    print(i)
                print("adding 1 month to the current date")
                cursor.execute("SELECT DATE('now','+1 month','localtime');")
                for i in cursor:
                    print(i)
                print("adding 1 year to the current date")
                cursor.execute("SELECT DATE('now','+1 year','localtime');")
                for i in cursor:
                    print(i)
            if 0:
                print("moving to start of the month")
                cursor.execute("SELECT DATE('now','start of month','localtime');")
                for i in cursor:
                    print(i)
                print("moving to start of the year")
                cursor.execute("SELECT DATE('now','start of year','localtime');")
                for i in cursor:
                    print(i)
                print("moving to start of the day")
                cursor.execute("SELECT DATE('now','start of day','localtime');")
                for i in cursor:
                    print(i)

            if 0:
                print("printing the current time in utc")
                cursor.execute("SELECT TIME('now');")
                for i in cursor:
                    print(i)
                print("printing the current time in local time")
                cursor.execute("SELECT TIME('now','localtime');")
                for i in cursor:
                    print(i)
                print("adding 1 hour to the current time")
                cursor.execute("SELECT TIME('now','+1 hour','localtime');")
                for i in cursor:
                    print(i)
                print("adding 1 minute to the current time")
                cursor.execute("SELECT TIME('now','+1 minute','localtime');")
                for i in cursor:
                    print(i)
                print("adding 1 second to the current time")
                cursor.execute("SELECT TIME('now','+1 second','localtime');")
                for i in cursor:
                    print(i)
            if 0:
                print("moving to start of the day in utc")
                cursor.execute("SELECT TIME('now','start of day');")
                for i in cursor:
                    print(i)
                print("moving to start of the day in localtime it means we have to add 5.30 hrs")
                cursor.execute("SELECT TIME('now','start of day','localtime');")
                for i in cursor:
                    print(i)
                # it will not work
                # print("moving to start of the hour")
                # cursor.execute("SELECT TIME('now','start of hour','localtime');")
                # for i in cursor:
                #     print(i)
            if 0:
                print("adding 1 month and 1 hour at a time")
                cursor.execute("SELECT DATETIME('now','+1 month','+1 hour','localtime');")
                for i in cursor:
                    print(i)
                print("printing the current timestamp")
                cursor.execute("SELECT CURRENT_TIMESTAMP, DATETIME('now');")
                for i in cursor:
                    print(i)
# exercise on date and time
if 0:# creating the posts table
    cursor.executescript('''
    DROP TABLE IF EXISTS posts;
    CREATE TABLE IF NOT EXISTS posts(
    name VARCHAR(100),
    posted_on DATE,
    posted_at TIME,
    posted DATETIME,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')
    #current timestamp will gives current date&time

    cursor.execute(''' 
    INSERT OR IGNORE INTO posts
    (name,posted_on,posted_at,posted) VALUES
    ('raju','1983-11-25','02:44:33','1983-11-25 02:44:33'),
    ('ramesh','1993-12-12','12:34:53','1993-12-12 12:34:53'),
    ('ram','1995-10-30','11:54:13','1995-10-30 11:54:13'),
    ('kalyan','2005-11-23','09:44:11','2005-11-23 09:44:11')
    ''')
    #  adding the row in the post table using the DATE(),TIME() and DATETIME()
    cursor.execute(''' 
    INSERT OR IGNORE INTO posts
    (name,posted_on,posted_at,posted) VALUES
    ('mohan',DATE(),TIME(),DATETIME()),
    ('rammohan',DATE('now','localtime'),TIME('now','localtime'),DATETIME('now','localtime'))''')
    data = cursor.execute("SELECT * FROM posts;")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    if 0:
        cursor.executescript('''
        DROP TABLE IF EXISTS dummy;
        CREATE TABLE IF NOT EXISTS dummy
        (person_name VARCHAR(100),
        gender CHAR(1),
        salary DECIMAL(7,2),
        projects INTEGER)
        ''')
        print("printing the date time specific format")
        # DATETIME has more range(1000-9999) and TIMESTAMP has less range(1970 to 2038 because epoch value will reset)
        data=cursor.execute("SELECT DATE(),TIME(),DATETIME(),CURRENT_TIMESTAMP,strftime('%m/%d/%Y','now');")
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
        cursor.executescript('''
        DROP TABLE IF EXISTS tweets_table;
        CREATE TABLE IF NOT EXISTS tweets_table(
        content VARCHAR(100),
        username VARCHAR(100),
        craeted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        ''')
# Logical operators
if 1:
    def split_commands(filename):
        f=open(filename,'r')
        commands = f.readlines()# we have to use readlines only. other wise use split with \n only
        f.close()
        return commands
    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)

    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    data = cursor.execute("SELECT * FROM organisation;")
    names = [i[0] for i in data.description];print(names)
    for i in cursor:
        print(i)

    if 0: # != operator
        data = cursor.execute("SELECT first_name||' '||last_name AS full_name FROM organisation WHERE profession != 'ENGINEER';")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0: # NOT LIKE operator
        print("printing the people whose salary starts with 5")
        data = cursor.execute("SELECT first_name||' '||last_name AS full_name,salary AS salary  FROM organisation WHERE salary LIKE '5____';")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people whose salary not starts with 5")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary AS salary  FROM organisation WHERE salary NOT LIKE '5____';")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:# > and >= operators
        print("checking the > operator")
        cursor.execute("SELECT 99>1;")#returns 1 True
        for i in cursor:
            print(i)
        print("checking the > operator")
        cursor.execute("SELECT 9>19;")#return 0 False
        for i in cursor:
            print(i)
        print("printing the people whose salary greater than 20000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary AS salary  FROM organisation WHERE salary > 20000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)

        print("printing the people whose salary >= 30000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary AS salary  FROM organisation WHERE salary >= 30000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:# < and <=
        print("printing the people whose joined before 2000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,joining_year  FROM organisation WHERE joining_year < 2000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people whose salary <= 20000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary  FROM organisation WHERE salary <= 20000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:#logical AND (&&)
        print("printing the people whose salary <= 20000 and joined before 2000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary <= 20000 AND joining_year <2000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people whose salary <= 20000 and joined before 2000 and selecting particular person")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary <= 20000 AND joining_year <2000 AND first_name = 'SAM';")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:#logical OR (||)
        print("printing the people whose salary <= 20000 or joined before 2000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary <= 20000 OR joining_year <2000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people whose salary > 30000 or joined after 2000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary > 30000 OR joining_year > 2000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0: #BETWEEN
        print("printing the people whose salary between 20000 to 30000 using AND")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary < 30000 AND salary > 20000 ;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people whose salary between 20000 to 30000 using BETWEEN")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary BETWEEN 20000 AND 30000;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:#NOT BETWEEN
        print("printing the people joined before 1960 and after 1990 using OR")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE joining_year < 1960 OR joining_year > 1990;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people joined before 1960 and after 1990 using NOT BETWEEN")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE joining_year NOT BETWEEN 1960 AND 1990;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0: #IN operator
        print("printing the people joined in 1961,1971 and 1981 using IN")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE joining_year IN (1961,1971,1981);")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people their salaries are 30000,50000,20000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary IN (20000,30000,50000);")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0: #NOT IN operator
        print("printing the people not joined in 1961,1971 and 1981 using NOT IN")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE joining_year NOT IN (1961,1971,1981);")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people their salaries are not 30000,50000,20000")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE salary NOT IN (20000,30000,50000);")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people their salaries are not 30000,50000,20000 who joined after 1970")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE joining_year >= 1970 AND salary NOT IN (20000,30000,50000) ORDER BY salary DESC;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:#% operator
        print("printing the people who joined after 1970 and next even years")
        data = cursor.execute(
            "SELECT first_name||' '||last_name AS full_name,salary,joining_year  FROM organisation WHERE joining_year >= 1970 AND joining_year %2 = 0 ORDER BY salary DESC;")
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
    if 0:#case statements i. like IF ELSE logic
        print("printing the people whose salary >= 30000")
        data = cursor.execute(
            '''SELECT first_name||' '||last_name AS full_name,salary,joining_year,
              CASE WHEN salary >= 30000 THEN 'high salary person'
                   ELSE 'low salary person' 
                   END AS 'salary_position'
              FROM organisation;''')
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people joined in old era or new era")
        data = cursor.execute(
            '''SELECT first_name||' '||last_name AS full_name,salary,joining_year,
              CASE WHEN joining_year >= 1970 THEN 'new era'
                   ELSE 'old era' 
                   END AS 'joined_era'
              FROM organisation;''')
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)
        print("printing the people with salary division")
        data = cursor.execute(
            '''SELECT first_name||' '||last_name AS full_name,salary,joining_year,
              CASE WHEN salary >= 10000 AND salary < 30000 THEN 'low salary person'
                   WHEN salary >= 30000 AND salary < 50000 THEN 'mid salary person'
                   ELSE 'high salary person' 
                   END AS 'salary_position'
              FROM organisation;''')
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)

        print("printing the people with salary division 2nd logic")
        data = cursor.execute(
            '''SELECT first_name||' '||last_name AS full_name,salary,joining_year,
              CASE WHEN salary BETWEEN 10000 AND 30000 THEN 'low salary'
                   WHEN salary BETWEEN 30000 AND 50000 THEN 'mid salary'
                   ELSE 'high salary' 
                   END AS 'salary_position'
              FROM organisation;''')
        names = [i[0] for i in data.description];
        print(names)
        for i in cursor:
            print(i)

# exercise on logical operators
if 0:
    def split_commands(filename):
        f = open(filename, 'r')
        commands = f.readlines()  # we have to use readlines only. other wise use split with \n only
        f.close()
        return commands


    def execute_commands(commands):
        for i in commands:
            cursor.execute(i)


    file = 'organisation_table.sql'  # commands in the file should be in single line only
    # it contains id,first_name,last_name,profession,joining_year,salary as columns
    commands = split_commands(file)
    execute_commands(commands)
    cursor.executescript('''INSERT OR IGNORE INTO organisation (first_name, last_name, profession, joining_year, salary,switched_companies)
                                                            VALUES ('rajesh','kumar','ENGINEER',2006,30000,3),
                                                                   ('kalyan','kumar','ANALYST',2003,23000,2),
                                                                   ('pawan','kalyan','MANAGER',1997,45000,3);''')
    print("printing the values")
    data = cursor.execute("SELECT * FROM organisation;")
    names = [i[0] for i in data.description];
    print(names)
    for i in cursor:
        print(i)

    print("print people joined before 1970")
    data = cursor.execute("SELECT first_name||' '||last_name,joining_year FROM organisation WHERE joining_year <1970;")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)

    print("print people only engineers and analyst")
    data = cursor.execute("SELECT first_name||' '||last_name,profession FROM organisation WHERE profession = 'ENGINEER' OR profession = 'ANALYST';")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    print("print people only analyst and joined after 1980")
    data = cursor.execute(
        "SELECT first_name||' '||last_name,profession,joining_year FROM organisation WHERE profession = 'ANALYST' AND joining_year > 1980;")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    print("print people salary between 30000  and 50000")
    data = cursor.execute(
        "SELECT first_name||' '||last_name AS 'full_name',profession,salary FROM organisation WHERE salary BETWEEN 30000 AND 50000;")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)

    print("print people salary is having 2 or 4 in their income")
    data = cursor.execute(
        "SELECT first_name||' '||last_name AS 'full_name',profession,salary FROM organisation WHERE salary LIKE '2____' OR salary LIKE '4____';")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    print("print people level based on their salary")
    data = cursor.execute(
        '''SELECT first_name||' '||last_name AS 'full_name',salary,
         CASE WHEN salary >= 10000 AND salary < 30000 THEN 'lower class'
              WHEN salary >= 30000 AND salary < 50000 THEN 'middle class'
              ELSE 'upper class'
              END AS 'classes'
                FROM organisation''')
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    print("print people grouped on their profession ")
    data = cursor.execute(
        '''SELECT profession,
         CASE WHEN COUNT(*) = 1 THEN COUNT(*)||' person'
              ELSE COUNT(*)||' persons'
              END AS 'total members'
                FROM organisation GROUP BY profession;''')
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)

if 0:# creating the posts table it is not working
    cursor.executescript('''
    DROP TABLE IF EXISTS posts;
    CREATE TABLE IF NOT EXISTS posts(
    name VARCHAR(100),
    posted_on DATE,
    posted_at TIME,
    posted DATETIME,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')
    #current timestamp will gives current date&time

    cursor.execute(''' 
    INSERT OR IGNORE INTO posts
    (name,posted_on,posted_at,posted) VALUES
    ('raju','1983-11-25','02:44:33','1983-11-25 02:44:33'),
    ('ramesh','1993-12-12','12:34:53','1993-12-12 12:34:53'),
    ('ram','1995-10-30','11:54:13','1995-10-30 11:54:13'),
    ('kalyan','2005-11-23','09:44:11','2005-11-23 09:44:11')
    ''')
    #  adding the row in the post table using the DATE(),TIME() and DATETIME()
    cursor.execute(''' 
    INSERT OR IGNORE INTO posts
    (name,posted_on,posted_at,posted) VALUES
    ('mohan',DATE(),TIME(),DATETIME()),
    ('rammohan',DATE('now','localtime'),TIME('now','localtime'),DATETIME('now','localtime'))''')
    data = cursor.execute("SELECT * FROM posts;")
    names = [i[0] for i in data.description]
    print(names)
    for i in cursor:
        print(i)
    if 0:#not working
        print("printing the tweets between 1993 to current date")
        cursor.execute("SELECT * FROM posts WHERE posted_on BETWEEN CAST('1993-01-01' AS DATETIME) AND CAST('2022-12-01' AS DATETIME);")
        for i in cursor:
            print(i)






#handler close
cursor.close()

#close database connection
database.close()