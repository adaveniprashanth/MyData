print("welcome to database triggers")
import sqlite3
# python code for running the commands:
# sql='SELECT x FROM myTable WHERE x LIKE %s'
# args=[beginningOfString+'%']
# cursor.execute(sql,args)

# beginningOfString += '%'
# cursor.execute("SELECT x FROM myTable WHERE x LIKE ?", (beginningOfString,) )

#AUTOINCREMENT will work only when we use INTEGER PRIMARY KEY

# Connect to DB if exists or else create new database
database = sqlite3.connect('database3.db')
# <databasehandle>.create_function(<function name>,no.of arguments,operation)
database.create_function("strrev", 1, lambda s: s[::-1])
print("Opened database successfully")
'''
Triggers are like the pre/post operation of INSERT/UPDATE/DELETE in the table

    trigger_time    trigger_event       table_name
    BEFORE          INSERT              photos
    AFTER           UPDATE              users
                    DELETE
'''

#create a handle for database
cursor = database.cursor()
if 1:
    if 1:#pre-conditions
        cursor.executescript('''DROP TABLE IF EXISTS users;
                                CREATE TABLE IF NOT EXISTS users(
                                username VARCHAR(255),
                                age INT);
                            ''')
    if 0:#trigger startup code
        cursor.execute('''
                DELIMITER //
                    CREATE TRIGGER trigger_name
                        trigger_time trigger_event ON table_name FOR EACH ROW
                        BEGIN
                        END
                //
                DELIMITER ;
                ''')
    if 0:#creating the trigger
        cursor.execute('''
        DELIMITER //
            CREATE TRIGGER must_be_an_adult
                BEFORE INSERT ON users FOR EACH ROW
                BEGIN
                    IF NEW.age < 18
                        THEN 
                            SIGNAL SQLSTATE '45000' 
                                SET MESSAGE_TEXT = 'Must be an adult!';
                    ENDIF;
                END
        //
        DELIMITER ;
        ''')
    if 0:
        cursor.executescript('''delimiter $$
        CREATE TRIGGER  Check_age  BEFORE INSERT ON users 
        FOR EACH ROW
        BEGIN
        IF NEW.age < 25 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'ERROR: 
                 AGE MUST BE ATLEAST 25 YEARS!';
        ENDIF;
        END $$
        delimiter ;
                ''')





#handler close
cursor.close()

#close database connection
database.close()

'''
delimiter $$
CREATE TRIGGER  Check_age  BEFORE INSERT ON employee 
FOR EACH ROW
BEGIN
IF NEW.age < 25 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'ERROR: 
         AGE MUST BE ATLEAST 25 YEARS!';
END IF;
END; $$
delimiter; 
'''