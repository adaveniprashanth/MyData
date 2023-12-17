import mysql.connector

# for reference --> https://www.interviewbit.com/mysql-cheat-sheet/
# for reference --> https://realpython.com/python-mysql/#installing-mysql-server
# for reference --> https://medium.com/@jinendra-singh/master-sql-joins-chapter-5-9901a83302f8
# connecting to mysql database
connection = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mindtree"
)

print(connection)
cursor = connection.cursor()
print("display all databases in server")
cursor.execute("SHOW DATABASES;")
for i in cursor:
  print(i)

db_name= "mindtree"
# cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(db_name))
# cursor.execute(" USE {};".format(db_name))
print("display all tables in database {}".format(db_name))
cursor.execute("SHOW TABLES;")
for i in cursor:
    print(i)

# creating the tables:
table_name="organisation"
cursor.execute('''DROP TABLE IF EXISTS {};'''.format(table_name))
cursor.execute("""CREATE TABLE IF NOT EXISTS {}
            (id INTEGER PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            profession VARCHAR(30),
            joining_year INTEGER,
            salary INTEGER,
            switched_companies INTEGER DEFAULT 1);""".format(table_name))
# inserting the data
query="INSERT IGNORE INTO {} (id,first_name,last_name,profession,joining_year,salary,switched_companies) VALUES (%s,%s, %s,%s,%s,%s,%s);".format(table_name)
values=[(1,'TONY', 'STARK', 'SOFTWARE ENGINEER',1980, 28000,2),
        (2,'TIM', 'ADOLF', 'SALESMAN', 1951, 16000,2),
        (3,'KIM', 'JARVIS', 'MANAGER', 1961, 35000,2),
        (4,'SAM', 'MILES', 'SALESMAN', 1991, 12000,1),
        (5,'KEVIN', 'HILL', 'MANAGER', 1971, 29000,3),
        (6,'CONNIE', 'SMITH', 'ANALYST', 1982, 30000,3),
        (7,'ALFRED', 'KINSLEY', 'PRESIDENT', 1981, 50000,3),
        (8,'PAUL', 'TIMOTHY', 'SALESMAN', 1991, 15000,2),
        (9,'JOHN', 'ASGHAR', 'SOFTWARE ENGINEER',1983, 31000,1),
        (10,'ROSE', 'SUMMERS', 'TECHNICAL LEAD',1981, 29000,2),
        (11,'ANDREW', 'FAULKNER', 'ANALYST', 1961, 30000,4),(12,'KAREN', 'MATTHEWS', 'SOFTWARE ENGINEER',1982, 33000,1),(13,'WENDY', 'SHAWN', 'SALESMAN', 1991, 50000,2),(14,'BELLA', 'SWAN', 'MANAGER', 1971, 34000,1),(15,'MADII', 'HIMBURY', 'ANALYST', 1941, 20000,2),(16,'ATHENA', 'WILSON', 'ANALYST', 1992, 70000,4),(17,'JENNIFER', 'HUETTE', 'ANALYST', 1996, 50000,3)]
cursor.executemany(query,values)
# executing the queries
# all items
if 0:
    cursor.execute("SELECT * FROM {};".format(table_name))
    for i in cursor:
        print(i)
#specific column names
if 0:
    cursor.execute("SELECT id FROM {};".format(table_name))
    for i in cursor:
        print(i)
# LIKE clause
if 0:
    if 0:
        cursor.execute("SELECT profession FROM {} WHERE profession LIKE '%ana%';".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("SELECT profession FROM {} WHERE profession LIKE '%man';".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("SELECT profession FROM {} WHERE profession LIKE 'man%';".format(table_name))
        for i in cursor:
            print(i)
# CASE clause
if 0:
    cursor.execute("""SELECT 
    CASE WHEN salary >= 30000 THEN 'pass' ELSE 'fail' END AS remarks,
    first_name,profession FROM organisation WHERE profession LIKE '%man';""".format(table_name))
    for i in cursor:
        print(i)

# ALIAS(AS) clause
if 0:
    if 0:
        cursor.execute("""SELECT 
                first_name AS surname,
                profession AS designation FROM {};""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT 
        first_name AS surname,
        CASE WHEN salary >= 20000 THEN 'pass' ELSE 'fail' END AS remarks,
        profession FROM organisation WHERE profession LIKE '%man';""".format(table_name))
        for i in cursor:
            print(i)
# LIMIT clause
if 0:
    if 0:
        cursor.execute("""SELECT * FROM {} LIMIT 2;""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT 
                    first_name AS surname,
                    salary,
                    CASE WHEN salary >= 20000 THEN 'pass' ELSE 'fail' END AS remarks,
                    profession FROM organisation WHERE profession LIKE '%man' ORDER BY salary LIMIT 2;""".format(table_name))
        for i in cursor:
            print(i)
    if 0: #limit with offset
        cursor.execute("""SELECT 
                    first_name AS surname,
                    salary,
                    CASE WHEN salary >= 20000 THEN 'pass' ELSE 'fail' END AS remarks,
                    profession FROM organisation WHERE profession LIKE '%man' ORDER BY salary LIMIT 1,3;""".format(table_name))
        for i in cursor:
            print(i)

# BETWEEN clause
if 0:
    if 0:
        cursor.execute("""SELECT * FROM {} WHERE salary BETWEEN 10000 AND 30000;""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT * FROM {} WHERE salary NOT BETWEEN 10000 AND 30000;""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT 
                    first_name AS surname,
                    salary,
                    CASE WHEN salary >= 20000 THEN 'pass' ELSE 'fail' END AS remarks,
                    profession FROM organisation WHERE profession LIKE '%man' AND salary BETWEEN 10000 AND 30000 ORDER BY salary LIMIT 1,3 ;""".format(table_name))
        for i in cursor:
            print(i)

# WHERE clause
if 0:
    if 0:
        cursor.execute("""SELECT * FROM {} WHERE id = (SELECT id FROM {} WHERE profession = 'PRESIDENT');""".format(table_name,table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT 
                    first_name AS surname,
                    salary,
                    CASE WHEN salary >= 20000 THEN 'pass' ELSE 'fail' END AS remarks,
                    profession FROM organisation WHERE profession LIKE '%man' AND salary BETWEEN 10000 AND 30000 ORDER BY salary LIMIT 1,3 ;""".format(table_name))
        for i in cursor:
            print(i)
# LIKE with _
if 0:
    if 0:
        cursor.execute("""SELECT * FROM {} WHERE salary LIKE '1_000';""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT 
                    first_name AS surname,
                    salary,
                    CASE WHEN salary >= 20000 THEN 'pass' ELSE 'fail' END AS remarks,
                    profession FROM organisation WHERE profession LIKE '%man' AND salary BETWEEN 10000 AND 30000 AND salary LIKE '1_000' ORDER BY salary LIMIT 1,3 ;""".format(table_name))
        for i in cursor:
            print(i)




# RANK function #this will overlap the rank values
if 1:
    if 0:
        cursor.execute("""SELECT RANK() OVER(ORDER BY salary) AS rank_score,
                                 salary,
                                 first_name,
                                 profession
                                 FROM {}""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT RANK() OVER(ORDER BY salary) AS rank_score,
                                   salary,
                                   first_name,
                                   profession
                            FROM {} 
                            WHERE RANK() OVER(ORDER BY salary) > 5""".format(table_name))

        for i in cursor:
            print(i)

# DENSE_RANK function will not overlaps
if 1:
    if 0:
        cursor.execute("""SELECT DENSE_RANK() OVER(ORDER BY salary) AS rank_score,
                                         salary,
                                         first_name,
                                         profession
                                         FROM {}""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT DENSE_RANK() OVER(PARTITION BY profession ORDER BY salary) AS rank_score,
                                         salary,
                                         first_name,
                                         profession
                                         FROM {}""".format(table_name))
        for i in cursor:
            print(i)
    if 0:
        cursor.execute("""SELECT DENSE_RANK() OVER( ORDER BY salary) AS rank_values
                                         salary,
                                         first_name,
                                         profession
                                         FROM {} WHERE rank_values >30000""".format(table_name))
        for i in cursor:
            print(i)

# ROW_NUMBER
if 1:
    if 0:
        cursor.execute("""SELECT ROW_NUMBER() OVER(PARTITION BY salary) AS row_numbers,
                                         salary,
                                         first_name,
                                         profession
                                         FROM {}""".format(table_name))
        for i in cursor:
            print(i)

# LAG function
if 1:
    if 0:
        cursor.execute("""SELECT salary,first_name,profession,
                    LAG(salary) OVER(PARTITION BY profession ORDER BY salary) AS salary_adjust 
                    FROM {};""".format(table_name))
        for i in cursor:
            print(i)
    if 0:#not working
        cursor.execute("""SELECT salary, first_name, profession, salary_adjust
        FROM(
            SELECT
        LAG(salary) OVER(PARTITION BY profession ORDER BY salary) AS salary_adjust FROM organisation) AS lagged_data 
        WHERE salary_adjust > 30000;""")

        for i in cursor:
            print(i)

cursor.close()
connection.close()


