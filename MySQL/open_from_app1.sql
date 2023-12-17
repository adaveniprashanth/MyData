-- **************ABOUT DATABASES*********************--------
SHOW DATABASES; -- to display databases
DROP DATABASE training; -- deleting the database
DROP DATABASE IF EXISTS training; -- deleting datbase with check
CREATE DATABASE training; -- creating the database
CREATE DATABASE IF NOT EXISTS training; -- creating the databse with check
SHOW CREATE DATABASE training; -- shows any additional infomration about while creating the database 
USE training; -- selecting the database for use
SELECT DATABASE(); -- to display the currently using database
-- *******************CREATE/DROP tables ***************------
SHOW TABLES; -- to display the tables in the currently using database
DROP TABLE IF EXISTS products; -- delting the table with check
DROP TABLE products; -- deleting the table without check. so may raise errors
 CREATE TABLE IF NOT EXISTS products 
 (
	productID INT UNSIGNED NOT NULL AUTO_INCREMENT, productCode CHAR(3) NOT NULL DEFAULT '',
	name VARCHAR(30) NOT NULL DEFAULT '', quantity INT UNSIGNED NOT NULL DEFAULT 0,
	price DECIMAL(7,2) NOT NULL DEFAULT 99999.99,
	PRIMARY KEY (productID)
); -- creating the table with check
CREATE TABLE products 
 (
	productID INT UNSIGNED NOT NULL AUTO_INCREMENT, productCode CHAR(3) NOT NULL DEFAULT '',
	name VARCHAR(30) NOT NULL DEFAULT '', quantity INT UNSIGNED NOT NULL DEFAULT 0,
	price DECIMAL(7,2) NOT NULL DEFAULT 99999.99,
	PRIMARY KEY (productID)
); -- creating the table without check so it may raise error

-- *****************INSERT into table**************-----------
INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);
INSERT INTO products VALUES
	(NULL, 'PEN', 'Pen Blue', 8000, 1.25),
	(NULL, 'PEN', 'Pen Black', 2000, 1.25); -- inserting with null values for auto increment
INSERT INTO products 
	(productCode, name, quantity, price) VALUES
	('PEC', 'Pencil 2B', 10000, 0.48),
	('PEC', 'Pencil 2H', 8000, 0.49); -- using auto increment feature
INSERT INTO products (productCode, name) VALUES ('PEC', 'Pencil HB'); -- inserting only with main values
INSERT INTO products VALUES (NULL,NULL,NULL,NULL,NULL); -- checking the NOT NULL condition
-- ****************SELECT in table ***************----------
SELECT * FROM products; -- selecting all columns
SELECT name,price FROM products; -- selecting particular columns
SELECT 1+1; -- selecting without table
SELECT now(); -- to dislay current time
-- ==> comparision operators (=, <>, <, >, <=, >= )<==
SELECT name,price FROM products WHERE price < 1.0; -- where criteria
SELECT name, quantity FROM products WHERE quantity <= 2000; 
SELECT name, price FROM products WHERE productCode = 'PEN';
-- ******************LIKE and NOT LIKE *************------
SELECT name, price FROM products WHERE productCode LIKE 'PEN';
SELECT name, price FROM products WHERE name LIKE 'PENCIL%';
SELECT name, price FROM products WHERE name LIKE 'P__';
SELECT name, price FROM products WHERE name LIKE 'P__%';
SELECT price,productCode FROM products WHERE productCode NOT LIKE 'P__%';
-- ***************** Logical operators ***************------------
SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'pen %';
SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'pen %' AND price <1.24;

SELECT name,price,quantity FROM products WHERE name LIKE 'pen%' OR quantity >=5000;

SELECT name,price FROM products WHERE NOT price <= 1.23;
SELECT name,price,quantity FROM products WHERE NOT ( name LIKE 'p__' AND quantity <5000);

-- **************IN, NOT IN ******************--------
SELECT * FROM products WHERE name IN ( 'pen blue','pen red');
SELECT * FROM products where quantity NOT IN (3000,5000,8000);

-- *********** BETWEEN, NOT BETWEEN *************----------
SELECT * FROM products WHERE quantity BETWEEN 2000 AND 10000;
SELECT * FROM products WHERE (quantity BETWEEN 2000 AND 10000) AND (price BETWEEN 0.50 AND 1.50);

SELECT name,price,quantity FROM products WHERE quantity NOT BETWEEN 5000 AND 8000;

-- ************** IS NULL and IS NOT NULL***************-----------
SELECT * FROM products WHERE price IS NULL;
SELECT name,price FROM products WHERE name IS NOT NULL;
SELECT name,price FROM products WHERE name = NULL;-- not work in some databases

-- **************ORDER BY clause **************-------------
SELECT * FROM products WHERE name LIKE 'p__%' ORDER BY price DESC;
SELECT * FROM products WHERE name LIKE 'p__%' ORDER BY quantity DESC,price;
SELECT * FROM products ORDER BY RAND(); -- random function

-- ************** LIMIT clause **************-----
SELECT * FROM products ORDER BY price LIMIT 0;
SELECT * FROM products ORDER BY price,name LIMIT 2;
SELECT * FROM products ORDER BY price LIMIT 2;
SELECT * FROM products ORDER BY price LIMIT 2,3; -- offset,limit i.e from 3rd row, 3 rows
SELECT * FROM products ORDER BY price LIMIT 0,3; -- offset,limit i.e from 1st row, 3 rows

-- **************AS Alias **********--------
SELECT productID AS ID, productCode AS Code,
name AS Description, price AS `Unit Price` -- Define aliases to be used as display names
FROM products
ORDER BY ID;

-- *************CONCAT **********----------
SELECT concat(productCode,'-',name) AS 'product Description',name FROM products;

-- ***********aggregate functions**********---------
SELECT price FROM products;
SELECT DISTINCT price FROM products;
SELECT DISTINCT price,name FROM products; -- distinct values of price and name combined

SELECT * FROM products ORDER BY productCode,productID;
-- SELECT * FROM products GROUP BY productCode; -- getting error

SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM products GROUP BY productCode;
SELECT productCode,count(*) AS 'count'FROM products GROUP BY productCode ORDER BY productCode DESC;

SELECT MIN(price) AS 'min. price', 
	   MAX(price) AS 'max. price',
       AVG(price) AS 'avg. price',
       SUM(quantity) AS 'total quantity' FROM products;

SELECT MIN(price) AS 'min. price', 
	   MAX(price) AS 'max. price',
       AVG(price) AS 'avg. price',
       SUM(quantity) AS 'total quantity' FROM products GROUP BY productCode; -- GROUP BY operation

SELECT MIN(price) AS 'min. price', 
	   MAX(price) AS 'max. price',
       CAST(AVG(price) AS DECIMAL(7,2)) AS 'avg. price',
       CAST(SUM(quantity) AS DECIMAL(5,2)) AS 'total quantity' FROM products GROUP BY productCode; -- type casting the value

SELECT name,price FROM products GROUP BY price; -- it will not work because all list columns are not added for groupby clause
SELECT name,price FROM products GROUP BY name,price; -- it will work because all list columns used for group by clause

SELECT price,SUM(quantity) AS 'Total' FROM products GROUP BY price HAVING Total >=8000; -- HAVING clause
SELECT productCode,SUM(quantity) AS 'Total' FROM products GROUP BY productCode WITH ROLLUP;-- show the summary of group summary

-- ********************modifying data -UPDATE**************------
UPDATE products SET price = price * 1.1;
UPDATE products SET quantity=quantity+100 WHERE name = 'Pen Red';
UPDATE products SET quantity=quantity-50,price=price-0.20 WHERE quantity >=5000;

-- ************modifying data DELETE **************-----------

DELETE FROM products WHERE name LIKE 'pencil%'; -- deleting the data based on where clause
DELETE FROM products;
SELECT * FROM products;







/*USE mindtree;
SET @table1 = 'organisation';
-- the below 3 line equals to -->  select * from table1;
SET @query = concat('SELECT * FROM ',@table1);
PREPARE query from @query;
EXECUTE query;
DEALLOCATE PREPARE query;

DELETE from organisation;
-- select with different parameters
SELECT * from organisation; -- collecting all items
SELECT id FROM organisation; -- selecting particular column
SELECT DISTINCT first_name, last_name FROM organisation; -- DISTINCT will  work on all columns not the nearest column 
-- DISTINCT will be used next after SELECT only
*/

