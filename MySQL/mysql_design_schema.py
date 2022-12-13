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
    with open(filename,'r') as file:
        for line in file:
            cursor.execute(line.strip())


if 1:
    if 1:#creating the tables
        run_queries_from_file('instagram_design_schema.sql')
    if 1:#adding data into tables
        cursor.execute('''INSERT OR IGNORE INTO users
        (username) VALUES
        ('Aadrik'),('Adhesht'),('Baalaaji'),('Bhakthavat'),('Charudutta'),('Daksh'),('Dhevaneyan'),('Erran'),('Ezhumalai'),('Fatik'),('Farishta'),
        ('Aarv'),('Adhiraj'),('Balamurli'),('Bhanukiran'),('Charuvrat'),('Dakshit'),('Dhirendra'),('Eelamyntha'),('Fanibhusha'),('Fateh'),('Geethik'),
        ('Aatreya'),('Adikavi'),('Balagovind'),('Bhartesh'),('Cheliyan'),('Daivit'),('Dhruddavra'),('Ekambaram'),('Eniyan'),('Fhazaar'),('Gaalav'),
        ('Aarksh'),('Adisesh'),('Balamani'),('Bhautik'),('Chevatkodi'),('Deekshith'),('Digvijay'),('Ekaraj'),('Elakkiyan'),('Fanish'),('Ganak'),
        ('Aadish'),('Aditeya'),('Banbhatt'),('Chaitan'),('Chayank'),('Deepankar'),('Divinantha'),('Eklavya'),(' Boys from'),('Fanindra'),('Gambhir'),
        ('Aabheer'),('Advaya'),('Banuteja'),('Chinmay'),('Chidambar'),('Denadayal'),('Duranjaya'),('Elamurugu'),('abet'),('Faisal'),('Gabith'),
        ('Aadarsh'),('Agasti'),('Bargav'),('Ceyone'),('Chiranjeev'),('Devadatta'),('Durgadas'),('Elangovan'),('Farhat'),('Fani'),('Giaan'),
        ('Aagam'),('Agendra'),('Basavaraj'),('Charish'),('Chittranja'),('Devendrana'),('Dushyant'),('Elilaendhi'),('Fanishwar'),('Fenil'),('Govardhan'),
        ('Abhyudh'),('Baladitya'),('Bhaagavat'),('Charvik'),('Chyavan'),('Deveshwar'),('Ehan'),('Emmanuel'),('Fravash'),('Falish'),('Gowshik'),
        ('Achyuta'),('Bharat'),('Bhadraksh'),('Chezian'),('Chittesh'),('Dhanaditya'),('Esh/Eshwar'),('Eruyarthth'),('Frany'),('Firoz'),('Greeshkand'),
        ('Adeep'),('Bhavish'),('Bhagesh'),('Chandragup'),('Chitrasen'),('Dhanakoti'),('Eashan'),('Erisudar'),('Falgu'),('Fajyaz'),('Grishmith'),
        ('Adharva'),('Bhargava'),('Bhaidyanat'),('Chanyana'),('Chithayu'),('Dharmanand'),('Easwaran'),('Eshwinraj'),('Faneemdra'),('Faiz'),('Govindaraj')   
            ''')
        cursor.execute('SELECT * FROM users;')
        for i in cursor:
            print(i)










#handler close
cursor.close()

#close database connection
database.close()
