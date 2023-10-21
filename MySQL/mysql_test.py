import mysql.connector

# for reference --> https://www.interviewbit.com/mysql-cheat-sheet/
# for reference --> https://realpython.com/python-mysql/#installing-mysql-server
# for reference --> https://medium.com/@jinendra-singh/master-sql-joins-chapter-5-9901a83302f8
# connecting to mysql database
connection = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  # database="mydatabase"
)

print(connection)
cursor = connection.cursor()
print("display all databases in server")
cursor.execute("SHOW DATABASES;")
for i in cursor:
  print(i)

# cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")
cursor.execute(" USE mydatabase;")
print("display all tables in database")
cursor.execute("SHOW TABLES;")
for i in cursor:
    print(i)
if 0:  # data types
    if 0: # character data type
        # we can support any character data, but we cannot specify particular datatype
        # i.e we cannot specify to store only ascii, or utf8, utf16
        # so we cannot use like  country_code CHAR(20) CHARACTER SET ascii
        # and do not use TINYTEXT data type also, it may slow down the system

        # cursor.execute('''DROP TABLE IF EXISTS char_table;''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS char_table
        (
        country_code CHAR(20),
        postal_code CHAR(10),
        name VARCHAR(100)
        );''')

        cursor.execute('''INSERT IGNORE INTO char_table(country_code,postal_code,name) VALUES(%s,%s,%s);''',('abc','def','GHI'))
        cursor.executemany('''INSERT IGNORE INTO char_table VALUES(%s,%s,%s);''', [('def', 'abc','GHI'),('ghi','jkl','ABC')])
        cursor.execute('SELECT * FROM char_table;')
        for i in cursor:
            print(i)

    if 0: # date data types
        # cursor.execute('''DROP TABLE IF EXISTS date_table;''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS date_table
        (
        my_date DATE, /* '1000-01-01' to '9999-12-31' */
        my_datetime DATETIME, /* '1000-01-01 00:00:00' to '9999-12-31 23:59:59' */
        my_timestamp TIMESTAMP, /* '1970-01-01 00:00:01'UTC to '2038-01-19 03:14:07' UTC. */
        my_year YEAR, /* 0000 to 9999 */
        my_time TIME /*  '-838:59:59' to '838:59:59' */
        );''')
        cursor.execute('''INSERT IGNORE INTO date_table(my_date,my_datetime,my_timestamp,my_year,my_time)
        VALUES('2023-08-11','2023-08-11 23:59:50','2023-08-11 23:59:50 UTC',2026,'23:23:23')''')

        cursor.execute('''INSERT IGNORE INTO date_table(my_date,my_datetime,my_timestamp,my_year,my_time)
        VALUES(%s,%s,%s,%s,%s)''',('2023-08-11','2023-08-11 23:59:50','2023-08-11 23:59:50 UTC',2023,'23:59:50'))

        cursor.executemany('''INSERT IGNORE INTO date_table(my_date,my_datetime,my_timestamp,my_year,my_time)
        VALUES(%s,%s,%s,%s,%s)''',
        [('0001-01-01', '0001-01-01 00:00:01', '0001-01-01 00:00:01 UTC', 1000, '-838:59:59'),
        ('9999-12-30', '9999-12-30 22:59:59', '9999-12-30 22:59:59 UTC', 9999, '838:59:59')])

        cursor.executemany('''INSERT IGNORE INTO date_table(my_date,my_datetime,my_timestamp,my_year,my_time)
        VALUES(%s,%s,%s,%s,%s)''',
        [('0001-01-01', '0001-01-01 00:00:01', '0001-01-01 00:00:01 UTC', 1000, '00:00:01'),
         ('9999-12-30', '9999-12-30 22:59:59', '9999-12-30 22:59:59 UTC', 9999, '23:59:59')])

        cursor.execute('SELECT * FROM datE_table;')
        for i in cursor:
            print(i)
    if 0: # integer types
        # INT and INTEGER both are having same range

        # cursor.execute('''DROP TABLE IF EXISTS integer_table;''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS integer_table
        (
        my_tinyint TINYINT,
        my_smallint SMALLINT,
        my_medumint MEDIUMINT,
        my_int INT,
        my_integer INTEGER,
        my_bigint BIGINT
        );''')

        cursor.execute('''INSERT IGNORE INTO integer_table VALUES
        (255,65535,16777215,4294967295,4294967295,18446744073709551615)''')
        cursor.execute('SELECT * FROM integer_table;')
        for i in cursor:
            print(i)
    if 0:# fixed point types
        # cursor.execute('DROP TABLE IF EXISTS fixed_types;')
        cursor.execute('''CREATE TABLE IF NOT EXISTS fixed_types
        (
        my_decimal DECIMAL,
        my_numeric NUMERIC,
        my_decimal_adjust DECIMAL(5,2),
        my_numeric_adjust NUMERIC(6,2)
        );''')
        cursor.execute('''INSERT IGNORE INTO fixed_types VALUES
        (7977.7879,567565.3242,876546.66,46455667.45);''')
        cursor.execute('SELECT * FROM fixed_types;')
        for i in cursor:
            print(i)

    if 0:#float types
        cursor.execute('DROP TABLE IF EXISTS float_types;')
        cursor.execute('''CREATE TABLE IF NOT EXISTS float_types
                (
                my_float FLOAT,
                my_decimal DECIMAL
                );''')
        cursor.execute('''INSERT IGNORE INTO float_types VALUES
                (7977.7879,567565.3242);''')
        cursor.execute('SELECT * FROM float_types;')
        for i in cursor:
            print(i)

    if 0: #bit type data
        cursor.execute('DROP TABLE IF EXISTS bit_types;')
        cursor.execute('''CREATE TABLE IF NOT EXISTS bit_types
                        (
                        my_bit BLOB,
                        my_bits BLOB
                        );''')
        cursor.execute('''INSERT IGNORE INTO bit_types(my_bit,my_bits)
        VALUES (10101101, 01010101001);''')
        cursor.executemany('''INSERT IGNORE INTO bit_types (my_bit, my_bits)
        VALUES (%s, %s)''',[(b'10101101', b'01010101001')])
        cursor.execute('SELECT * FROM bit_types;')
        for i in cursor:
            print(i)

# copying the data from other table
if 0:
    # collect data from sqlite database
    import sqlite3
    # connecting to sqlite database
    database = sqlite3.connect('preparation.db')
    cur = database.cursor()
    cur.execute("SELECT * FROM customers;")

    # create table in mysql database
    cursor.execute('DROP TABLE IF EXISTS users;')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
    (
    userId INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(40) NOT NULL, LastName VARCHAR(20) NOT NULL,
    Company VARCHAR(80), Address VARCHAR(70),
    City VARCHAR(40), State VARCHAR(40),
    Country VARCHAR(40), PostalCode VARCHAR(10),
    Phone VARCHAR(24), Fax VARCHAR(24),
    Email VARCHAR(60) NOT NULL, SupportRepId INTEGER
    );''')
    for i in cur:
        cursor.execute('INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',i)

    # closing the sqlite database
    cur.close()

if 0: #select functionality
    if 0: #selecting all columns
        cursor.execute('SELECT * FROM users;')
        names = [description[0] for description in cursor.description]
        print(names)

        # ['userId', 'FirstName', 'LastName', 'Company', 'Address', 'City', 'State',
        # 'Country', 'PostalCode', 'Phone', 'Fax', 'Email', 'SupportRepId']

        # for i in cursor:
        #     print(i)

    if 0:
        # DISTINCT keyword should be next to SELECT only
        cursor.execute('SELECT DISTINCT Country,userId FROM users;')
        for i in cursor:
            print(i)

    if 0: #slecting the specific column name
        cursor.execute('SELECT FirstName FROM users;')
        for i in cursor:
            print(i)

    if 0:# SELECT with WHERE
        cursor.execute('SELECT userId,Country FROM users WHERE Country ="India"')
        for i in cursor:
            print(i)

    if 0: # SELECT with LIKE
        cursor.execute('SELECT userId,Country FROM users WHERE Country LIKE "%nd%";')
        for i in cursor:
            print(i)
        #SELECT with LIKE pattern 2
        cursor.execute('SELECT userId,Country FROM users WHERE Country LIKE "%l_nd%";')
        for i in cursor:
            print(i)

    if 0:# SELECT WITH CASE
        cursor.execute('''SELECT userId, Country,
         CASE WHEN Country == 'India' THEN 'locals'
         ELSE 'non-local' 
         END as depends FROM users;''')
        for i in cursor:
            print(i)

    # not supported in SQLite but support in others like MYSQL
    if 0:# SELECT WITH IF
        cursor.execute('''SELECT userId, Country,
         IF (Country == 'India','locals','non-local') as depends FROM users;''')
        for i in cursor:
            print(i)

    if 0: #SELECT with AS
        cursor.execute('SELECT userId AS id,Country as nation FROM users;')
        names= [i[0] for i in cursor.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:# SELECT with LIMIT
        cursor.execute('SELECT userId,Country FROM users LIMIT 3;')
        for i in cursor:
            print(i)

    if 0:# SELECT with LIMIT and offset
        # starts the limit from 20th offset
        cursor.execute('SELECT userId,Country FROM users LIMIT 3,20;')
        for i in cursor:
            print(i)

    if 0:# SELECT with BETWEEN
        cursor.execute('SELECT userId,Country FROM users WHERE userId>=2 and userId <=6;')
        for i in cursor:
            print(i)

        cursor.execute('SELECT userId,Country FROM users WHERE userId BETWEEN 2 and 5;')
        for i in cursor:
            print(i)

    if 0:# SELECT with NOT BETWEEN
        cursor.execute('SELECT userId,Country FROM users WHERE userId<2 or userId > 57;')
        for i in cursor:
            print(i)

        cursor.execute('SELECT userId,Country FROM users WHERE userId NOT BETWEEN 2 and 57;')
        for i in cursor:
            print(i)

if 0:#sql joins
    f1 =open('joins_result.txt','w')
    cursor.execute("DROP TABLE IF EXISTS table1;")
    cursor.execute("DROP TABLE IF EXISTS table2;")
    cursor.execute('''CREATE TABLE IF NOT EXISTS table1(
    user_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(50),
    order_id INT NOT NULL
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS table2(
        order_id INT NOT NULL,
        price INT,
        profit INT  
        );''')
    cursor.execute('''INSERT IGNORE INTO table1
    (name,order_id) VALUES
    ('raj',123),('ramesh',234),
    ('arun',456),('kamal',567);
    ''')
    cursor.execute('''INSERT IGNORE INTO table2
    (order_id,price,profit) VALUES
    (123,450,150),(234,550,50),
    (789,567,45),(987,456,12);''')
    for i in cursor:
        print(i)
    print("table1 details")
    f1.writelines("\ntable1 data\n")
    cursor.execute('''SELECT * FROM table1;''')
    names = [description[0] for description in cursor.description]
    f1.writelines(str(names)+"\n")
    for i in cursor:
        f1.writelines(str(i)+"\n")
        print(i)

    print("table2 details")
    f1.writelines("\ntable2 data\n")
    cursor.execute('''SELECT t2.order_id,t2.price,t2.profit FROM table2 as t2;''')
    names=[i[0] for i in cursor.description]
    f1.writelines(str(names)+"\n")
    for i in cursor:
        f1.writelines(str(i) + "\n")
        print(i)
    if 0: #cross join
        f1.writelines("\ncross join result\n")
        cursor.execute('''SELECT t1.name,t2.profit FROM table1 as t1 CROSS JOIN table2 as t2;''')
        names=[i[0] for i in cursor.description]
        f1.writelines(str(names) + "\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i) + "\n")

    if 0: #inner join
        print("inner join result")
        f1.writelines("\ninner join result\n")
        cursor.execute('''SELECT t1.order_id,t1.name,t2.profit FROM table1 as t1 
                                            INNER JOIN table2 as t2 ON t1.order_id = t2.order_id;''')
        names=[i[0] for i in cursor.description]
        f1.writelines(str(names) + "\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i) + "\n")
    if 0: #left join
        print("left join result")
        f1.writelines("\nleft join result\n")
        cursor.execute('''SELECT t1.order_id,t1.name,t2.profit FROM table1 as t1 
                                            LEFT JOIN table2 as t2 ON t1.order_id = t2.order_id;''')
        names=[i[0] for i in cursor.description]
        f1.writelines(str(names) + "\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i) + "\n")
    if 0: #right join
        print("right join result")
        f1.writelines("\nright join result\n")
        cursor.execute('''SELECT t1.order_id,t1.name,t2.profit FROM table1 as t1 
                                            RIGHT JOIN table2 as t2 ON t1.order_id = t2.order_id;''')
        names=[i[0] for i in cursor.description]
        f1.writelines(str(names) + "\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i) + "\n")
    if 0: #full join
        print("full join result")
        f1.writelines("\nfull join result is combination of left and right join result\n")
        cursor.execute('''SELECT t1.order_id,t1.name,t2.profit FROM table1 as t1 
                                            LEFT JOIN table2 as t2 ON t1.order_id = t2.order_id UNION
                          SELECT t1.order_id,t1.name,t2.profit FROM table1 as t1 
                                            RIGHT JOIN table2 as t2 USING(order_id)
                                        ;''')
        names=[i[0] for i in cursor.description]
        f1.writelines(str(names) + "\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i) + "\n")
    if 1:#self join

        cursor.execute('''DROP TABLE IF EXISTS color_table;''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS color_table(
        color VARCHAR(50),name VARCHAR(50),assigned_color VARCHAR(50));''')
        cursor.execute('''INSERT IGNORE INTO color_table
        (color,name,assigned_color) VALUES
        ('blue','raj','black'),
        ('red','ram','blue'),
        ('yellow','kamal','red'),
        ('black','amar','yellow');''')
        print("color table data")
        f1.writelines("color table data\n")
        cursor.execute('''SELECT * FROM color_table;''')
        names=[i[0] for i in cursor.description]
        f1.writelines(str(names)+"\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i)+"\n")
        print("self join result")
        f1.writelines("\nself join result\n")
        cursor.execute('''SELECT t1.name,t1.assigned_color,t2.name AS 'santa'  FROM color_table as t1
                                                    JOIN color_table as t2 ON t1.assigned_color=t2.color;''')
        names = [i[0] for i in cursor.description]
        f1.writelines(str(names) + "\n")
        for i in cursor:
            print(i)
            f1.writelines(str(i) + "\n")

    f1.close()

# cursor.execute("DROP DATABASE mydatabase;")
# cursor.execute("DROP DATABASE IF EXISTS mydatabase;")
a=cursor.fetchall() #to avoid "Unread result found" error

connection.commit()
cursor.close()
connection.close()
