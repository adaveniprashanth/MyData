import mysql.connector

# for reference --> https://www.interviewbit.com/mysql-cheat-sheet/
# for reference --> https://realpython.com/python-mysql/#installing-mysql-server

# connecting to mysql database
connection = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  # database="filmfare"
)

cursor = connection.cursor()
# 9666626348 hussain basha.
if 0:#show databases
    cursor.execute('SHOW DATABASES;')
    a = cursor.fetchall()
    print(a)
if 0:
    cursor.execute('''DROP DATABASE IF EXISTS filmfare;''')
    cursor.execute('''CREATE DATABASE filmfare;''')
    cursor.execute('''USE filmfare;''')

# cursor.execute('''DROP TABLE IF EXISTS actor;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS actor
(actor_id SMALLINT PRIMARY KEY,
first_name VARCHAR(50),last_name VARCHAR(50),
last_update TIMESTAMP
);''')

# cursor.execute('''DROP TABLE IF EXISTS advisor;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS advisor
(advisor_id SMALLINT PRIMARY KEY,
first_name VARCHAR(50),last_name VARCHAR(50),
is_chairman SMALLINT
);''')

# cursor.execute('''DROP TABLE IF EXISTS film_text;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS film_text
(film_id SMALLINT PRIMARY KEY,
title VARCHAR(50),
description TEXT
);''')

# cursor.execute('''DROP TABLE IF EXISTS country;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS country
(country_id SMALLINT PRIMARY KEY,
country VARCHAR(20),
last_update TIMESTAMP
);''')

# cursor.execute('''DROP TABLE IF EXISTS category;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS category
(category_id TINYINT PRIMARY KEY,
name VARCHAR(20),
last_update TIMESTAMP
);''')

# cursor.execute('''DROP TABLE IF EXISTS language;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS language
(language_id SMALLINT PRIMARY KEY,
name VARCHAR(20),
last_update TIMESTAMP
);''')

# cursor.execute('''DROP TABLE IF EXISTS investor;''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS investor 
(investor_id SMALLINT PRIMARY KEY,
first_name VARCHAR(50),last_name VARCHAR(50),
company_name VARCHAR(50)
);''')

# cursor.execute('''DROP TABLE IF EXISTS city;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS city
(city_id SMALLINT PRIMARY KEY,
city VARCHAR(50),
country_id SMALLINT,
last_update TIMESTAMP,
FOREIGN KEY(country_id) REFERENCES country(country_id) ON DELETE CASCADE 
);''')

# cursor.execute('''DROP TABLE IF EXISTS actor_award;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS actor_award
(actor_award_id SMALLINT PRIMARY KEY,
actor_id SMALLINT,
first_name VARCHAR(50),last_name VARCHAR(50),
awards VARCHAR(45),
last_update TIMESTAMP,
FOREIGN KEY(actor_id) REFERENCES actor(actor_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS address;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS address
(address_id SMALLINT PRIMARY KEY,
address VARCHAR(50),
address2 VARCHAR(50),
district VARCHAR(50),
city_id SMALLINT,
postal_code VARCHAR(20),
phone VARCHAR(20),
last_update TIMESTAMP,
FOREIGN KEY(city_id) REFERENCES city(city_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS film;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS film
(film_id SMALLINT PRIMARY KEY,
title VARCHAR(50),
description TEXT,
release_yaer YEAR,
language_id SMALLINT,
original_language_id TINYINT,
rental_duration TINYINT,
rental_rate DECIMAL(7,2),
length SMALLINT,
replacement_cost DECIMAL(7,2),
rating ENUM('1','2','3','4','5'),
special_feature SET('graphics','action','vfx','animation'),
last_update TIMESTAMP,
FOREIGN KEY(language_id) REFERENCES language(language_id) ON DELETE CASCADE 
);''')

# cursor.execute('''DROP TABLE IF EXISTS store;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS store
(store_id SMALLINT PRIMARY KEY,
address_id SMALLINT,
last_update TIMESTAMP,
FOREIGN KEY(address_id) REFERENCES address(address_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS customer;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS customer
(customer_id SMALLINT PRIMARY KEY,
store_id SMALLINT,
first_name VARCHAR(50),last_name VARCHAR(50),
email VARCHAR(50),
address_id SMALLINT,
active TINYINT,
create_date DATETIME,
last_update TIMESTAMP,
FOREIGN KEY(store_id) REFERENCES store(store_id) ON DELETE CASCADE,
FOREIGN KEY(address_id) REFERENCES address(address_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS inventory;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
(inventory_id SMALLINT PRIMARY KEY,
film_id SMALLINT,
store_id SMALLINT,
last_update TIMESTAMP,
FOREIGN KEY(film_id) REFERENCES film_text(film_id) ON DELETE CASCADE,
FOREIGN KEY(store_id) REFERENCES store(store_id) ON DELETE CASCADE
);''')
#
# cursor.execute('''DROP TABLE IF EXISTS staff;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS staff
(staff_id SMALLINT PRIMARY KEY,
first_name VARCHAR(50),last_name VARCHAR(50),
address_id SMALLINT,email VARCHAR(50),
store_id SMALLINT,active TINYINT(1),
username VARCHAR(40),password VARCHAR(40),
last_update TIMESTAMP,
FOREIGN KEY(address_id) REFERENCES address(address_id) ON DELETE CASCADE,
FOREIGN KEY(store_id) REFERENCES store(store_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS rental;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS rental
(rental_id SMALLINT PRIMARY KEY,
rental_data DATETIME,
inventory_id SMALLINT,
customer_id SMALLINT,
return_date DATETIME,
staff_id SMALLINT,
last_update TIMESTAMP,
FOREIGN KEY(inventory_id) REFERENCES inventory(inventory_id) ON DELETE CASCADE,
FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
FOREIGN KEY(staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS payment;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS payment
(payment_id SMALLINT PRIMARY KEY,
customer_id SMALLINT,
staff_id SMALLINT,
rental_id SMALLINT,
amount DECIMAL(7,2),
payment_date DATETIME,
last_update TIMESTAMP,
FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
FOREIGN KEY(staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
FOREIGN KEY(rental_id) REFERENCES rental(rental_id) ON DELETE CASCADE
);''')

# cursor.execute('''DROP TABLE IF EXISTS film_actor;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS film_actor
(actor_id SMALLINT,film_id SMALLINT,
last_update TIMESTAMP,
PRIMARY KEY(actor_id,film_id),
FOREIGN KEY(film_id) REFERENCES film(film_id) ON DELETE CASCADE
);''')
# ###################################


connection.commit()
cursor.close()
connection.close()

