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
database = sqlite3.connect('database2.db')
# <databasehandle>.create_function(<function name>,no.of arguments,operation)
database.create_function("strrev", 1, lambda s: s[::-1])
print("Opened database successfully")

#create a handle for database
cursor = database.cursor()

if 0: #REVERSE Method --> strrev(string)
    # <databasehandle>.create_function(<function name>,no.of arguments,operation)
    database.create_function("strrev", 1, lambda s: s[::-1])
    cursor.execute("SELECT strrev(first_name) AS 'short_name' FROM organisation;")
    for i in cursor:
        print(i)


def run_queries_from_file(filename):
    l = []
    with open(filename,'r') as file:
        for line in file:
            l.append(line.strip())
            # print(line)
    all_commans = "".join(l)
    cursor.executescript(all_commans)


if 1:
    if 1:#creating the tables
        run_queries_from_file('instagram_design_schema.sql')

    if 1:#printing the data from the table
        cursor.execute('SELECT * FROM users;')
        for i in cursor:
            print(i)










#handler close
cursor.close()

#close database connection
database.close()
