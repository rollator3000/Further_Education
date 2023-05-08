# COMPLETE SQL-MASTERCLASS

Notes to the Online-Course 'Die komplette SQL Masterclass: Vom Anfänger zum Profi' - https://www.udemy.com/course/sql-komplett/  

## Overview
1. Introduction  
2. Installation of PostgreSQL  
3. Databank Queries
	- SELECT  
	- WHERE  
	- COUNT  
	- DISTINCT  
	- 1st Exercise  
	- LIKE  
	- IN & BETWEEN  
	- 2nd Exercise  
	- ORDER BY 
	- LIMIT
	- Bulit-In Functions
	- AS
	- 3rd Exercise
4. Manage Data
	- INSERT INTO
	- UPDATE
	- DELETE 
	- 4th Exercise
5. Manage tables
	- DATATYPES
		- TEXT
		- NUMBERS
	- Manage Columns
	- NULL
	- Standard Values
	- ID / Primary-Key
	- 5th Exercise
6. Complex Queries 
	- SUBSELECT
	- Renaming of tables
	- Naming subselect columns 
	- SUBSELECTS w/ multiple rows
	- 6th Exercise
7. JOINS
	- CROSSJOIN
	- INNERJOIN
	- LEFT-/ RIGHTJOIN
	- FULLJOIN
	- 7th Exercise
8. GROUP BY
	- Filter
	- 8th Exercise
9. Time & Date
	- UNIX-TimeStamp
	- Calculations
	- Formations
	- 9th Exercise
10. Index
	- CREATE INDEX
	- INDEX over multiple columns
	- 10th Exericse
11. FOREIGN KEY
	- FOREIGN KEY
	- ON DELETE
	- ON DELETE
12. VIEW
	- CREATE VIEW
	- CREATE MATERIALIZED VIEW
13. COLLACTION
14. TRANSACTION
	- START TRANSACTION 
	- Locking
15. Modeling databases
	- 1st Normalform
	- 2nd Normalform
	- 3rd Normalform  
	- Alternatives to Normalform
	- Postgre Example
16. Permissions
	- PostgreSQL
17. Stored Functions & Procedures  
	- Return multiple values  
	- Return a table  
	- Pass parameters to a function    
	- Optimize functions    
		- IMMUTABLE  
		- STABLE  
		- VOLATILE  
	- Function privileges  
	- Log-Files  
	- DrawBacks  
	- 11th Exercise
18. Full text search  
	- to_tsvector
	- Querying
		- Ranking search results
		- Saving ts_vector
19. Execute functions automatically
	- Trigger
	- Meaninful values
	- VIEW / MATERIALIED VIEW
	- 12th Exercise
20. Constraints

<br/>

# (1) Introduction
This course covers the two databank-systems 'MySQL' & 'PostgreSQL' - both are commonly used frameworks with only small differences.  
- MySQL:  
	- Less Features than PostgreSQL   
	- often part of WebHosters  

- PostgreSQL:  
	- more features than MySQL   
	- ideal for complex queries  

There is a SQL-Tool available online: https://downloads.codingcoursestv.eu/043%20-%20sql/online-sql/dist/index.html

**Exemplary Query:**  
Select the columns "id", "creator", "title" & "downloads" from the table "books" where "creator" equals ''Niemann, August'.  

		SELECT "id", "creator", "title", "downloads"
		FROM books
		WHERE creator = 'Niemann, August'

# (2) Installation of PostgreSQL
As MySQL doesn't work on MacOS, I've only set-up PostgreSQL. <br/> 

- Download of a databank *(s. 'data/')*
- Configuration of PostgreSQL
	- PGAdmin4 
	- Servers
	- Creation of new data-base

# (3) Databank Queries
## SELECT
Select columns from a data-base. <br/> 
- Optimally, put colnames in " " *(' ' doesn't work)*  
- Case-Sensitive

Select all columns from data-base// only columns A, B from TABLE 

	SELECT * FROM TABLE			
	SELECT "A", "B" FROM TABLE

## WHERE 
Select rows that full-fill a condition. <br/> 
- Mathematically: >, <, >=, <=
- Equal/ Unequal: =, <>
- AND, OR
	- in brackets: ... WHERE ("name" = 'Alex' AND "gender" = 'M' AND "year" = 2010)
- NOT:
	- in brackets: ... WHERE NOT("age" > 20) 
- Put strings in ' ' *(" " doesn't work)*
 
Get all columns for the rows, where title = 'Hr. Dr'// 'Fr. Dr' & where AGE > 30

	SELECT * 
	FROM TABLE
	WHERE (TITLE = 'Fr. Dr.' OR TITLE = 'Hr. Dr') AND	
		AGE > 30  							

## COUNT & DISTINCT
- 'COUNT' counts the amount of rows
- 'DISTINCT' shows all unique values of a column  
	- use brackets over multiple columns 
	- PostgreSQL differs between a - ä, ... + CaseSensitive *(MySQL not!)*
 
Get amount of rows from TABLE that fullfill the WHERE clause

	SELECT COUNT(*) 
	FROM TABLE
	WHERE AGE <= 12

Get the individial names *(name, lastname)* from TABLE

	SELECT DISTINCT("name", "lastname") 
	FROM TABLE

Get the amount of individual names from TABLE

	SELECT COUNT(DISTINCT("name", "lastname"))
	FROM TABLE

## 1. Exercise - 'baby_names'
### (1) Wie viele Einträge gibt es insgesamt in der Tabelle baby_names?

	SELECT COUNT(*) FROM baby_names

### (2)  Wie viele männliche Personen (gender = M) wurden im Jahr 2010 geboren, die „Alex“ heißen?

	SELECT COUNT(*) FROM baby_names WHERE 
		("name" = 'Alex' AND "gender" = 'M' AND "year" = 2010)

### (3) Wie viele unterschiedliche Namen gibt es in unserer Tabelle… wenn:
#### (3-1) Das Geschlecht egal ist (d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählt als der gleiche Name)

	SELECT COUNT(DISTINCT("name")) FROM baby_names 

#### (3-2) Das Geschlecht nicht egal ist (d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählen als 2 unterschiedliche Namen)

	SELECT COUNT(DISTINCT("name", "gender")) FROM baby_names 

### (4) Welcher Baby-Name wurde in einem bestimmten Jahr exakt 19250 mal vergeben?

	SELECT * FROM baby_names WHERE count = 19250

### (5) Gibt es das Geschlecht „divers“ in unserer Tabelle? Kannst du das mit den dir bisher bekannten Befehlen herausfinden?

	SELECT DISTINCT("gender") FROM baby_names  

## LIKE
Effective fullltext search - e.g. all E-Mails that contain '@gmail'.  

- LIKE % = none, one or multiple letters
- LIKE _ = exactly one letter
- Strings have to be put in ' '
- LIKE is case-sensitive & 'ILIKE'

Get all rows, where name starts with an 'a' followed by none, one or multiple letters

	SELECT * FROM TABLE
	WHERE name LIKE 'a%'

Get all rows, where the name contains a 'a' at any position

	SELECT * FROM TABLE
	WHERE name LIKE '%a%'

Get all rows that end with '@gmail.com'

	SELECT * FROM TABLE
	WHERE name LIKE '%@gmail.com'

Get all rows that end with '@gmail.com' // '@googlemail'

	SELECT * FROM TABLE
	WHERE name LIKE '%@g%mail.com'

Get all rows of names starting with 'a' and 3 more letters

	SELECT * FROM TABLE
	WHERE name LIKE 'a____'

## IN & BETWEEN
Optimize your queries, by combining multiple AND/ OR commands into a single one.  
Instead of `SELECT * WHERE (name = 'Julia' OR name = 'Paul`)

	SELECT * FROM TABLE
	WHERE name IN ('Julia', 'Anna')
<br/>

	SELECT * FROM TABLE
	WHERE age BETWEEN 18 AND 25
<br/>

	SELECT * FROM TABLE
	WHERE age BETWEEN 18 AND 25 AND
	WHERE name IN ('Julia', 'Anna')

## 2. Exercise - 'baby_names'
### (1) Wie viele unterschiedliche Vornamen gibt es, die mit „Alex“ anfangen, „Alex“ eingeschlossen? Hierbei spielt das Geschlecht keine Rolle.

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE 'Alex%' # -> 20 

### (2) Wie viele unterschiedliche Vornamen gibt es, in denen im Vornamen ein „m“ enthalten ist? Das „m“ darf auch an erster Stelle stehen.  

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE '%m%' OR "name" LIKE 'M%' # -> 1183	

### (3) Wie viele Zeilen gibt es in der Tabelle, bei denen das Jahr im 20. Jahrhundert (1900 bis einschließlich 1999) ist? 
Einmal mit BETWEEN einmal ohne

	SELECT COUNT("year") FROM baby_names WHERE "year" BETWEEN 1900 AND 1999      # -> 100
	SELECT COUNT("year") FROM baby_names WHERE "year" >= 1900 AND "year" <= 1999 # -> 100

### (4) Wie viele Zeilen gibt es in der Tabelle, bei denen das Jahr im 20. Jahrhundert (1900 bis einschließlich 1999) ist, und durch 10 Teilbar ist?

Löse diese Aufgabe mit vielen ORs

	SELECT COUNT("year") FROM baby_names WHERE 
		"year" = 1900 OR "year" = 1910 OR "year" = 1920 OR "year" = 1930 OR
	    "year" = 1940 OR "year" = 1950 OR "year" = 1960 OR "year" = 1970 OR
	    "year" = 1980 OR "year" = 1990 # -> 15307

Löse diese Aufgabe mit einem WHERE IN()

	SELECT COUNT("year") FROM baby_names WHERE 
		"year" IN (1990, 1980, 1970, 1960, 1950, 1940, 1930, 1920, 1910, 1900) # -> 15307

Löse die Aufgabe mit einem LIKE

	SELECT COUNT("year") FROM baby_names WHERE year::varchar LIKE '19_0'       # -> 15307

Löse diese Aufgabe mit einem Modulo

	SELECT COUNT("year") FROM baby_names WHERE 								   # -> 15307
		"year"%10 = 0 AND year BETWEEN 1900 AND 1999

## ORDER BY 
- ORDER BY goes to end of each query
- ORDER BY ASC is ascending & analog w/ DESC

Can be applied to mutliple variables

	SELECT * FROM TABLE
	ORDER BY name DESC, age ASC

## LIMIT
- LIMIT can be used to limit the amount of shown rows
- OFFSET is used to skip the first X rows

Get the rows 11-30 - skip the first then and then show max of 20 

	SELECT * FROM TABLE
	OFFSET 10 LIMIT 20

## Bulit-In Functions & AS
Useful bulit-in funtions 

- **MIN(numeric col)** Minimum of a column
- **MAX(numeric col)** Maximum of a column
- **AVG(numeric col)** Mean of a column
- **SUM(numeric col)** Sum of a column
- **COUNT(\*)** Amount of rows 
- **UPPER(char col)** Text in capital
- **LOWER(char col)** Text in lower
- **LENGTH(char col)** Amount of chars
- **SUBSTR(char col, POS, LEN)** Get substring, from POS to LEN chars
- **CONCAT(char col, char col)** Paste two char-cols
- **REPLACE(col1, char1, char2)** Replace all char1 elements w/ char2 in col1

Can also be combined + take care that they return the same amount of rows.  
Use 'AS' to name columns.

	SELECT CONCAT(UPPER(name), ' - ', LOWER(lastname)) AS last_name FROM TABLE
<br/>

	SELECT AVG(MIN(age), MAX(age)) AS LOL FROM TABLE

## 3. Exercise - 'baby_names'
### (1) Welcher Vorname kam insgesamt (d.h. für ein beliebiges Geschlecht in einem beliebigen Jahr) am häufigsten vor?

	SELECT * FROM baby_names ORDER BY "count" DESC LIMIT 3 # -> Linda

### (2) Welches Jahr ist das erste Jahr in unserer Datenbasis?
Löse dies mit Hilfe der MIN()-Funktion

	SELECT MIN("year") FROM baby_names # -> 1880

Löse dies ohne die MIN()-Funktion

	SELECT DISTINCT("year") FROM baby_names ORDER BY "year" LIMIT 5  # -> 1880

### (3) Wie viele unterschiedliche Vornamen gibt es, die aus exakt 5 Buchstaben bestehen?
Löse dies mit einem WHERE und der LENGTH()-Funktion

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE LENGTH("name") = 5  # -> 1590

Löse dies mit einem WHERE und einem LIKE (hier gab es einen speziellen Platzhalter)

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE '_____' # -> 1590

### (4) Wie viele Babys sind für das Jahr 2000 insgesamt in unserer Datenbasis? Berechne hier die Summe aller Einträge!

	SELECT SUM(count) FROM baby_names WHERE year = 2020 # -> 3.320.671

### (5) Wenn wir alle unterschiedlichen Vornamen betrachten (Geschlecht ist egal), und aufsteigend alphabetisch sortieren - Welcher Vorname steht auf der 2. Seite ganz oben, wenn die erste Seite aus 10 Einträgen besteht?

	SELECT DISTINCT("name") FROM baby_names ORDER BY "name" OFFSET 10 LIMIT 1 # -> Aarna

# (4) Manage Data
## INSERT INTO
Put new data permanently into existing data - if 'TABLE' had an 3rd column the added row would contain NULL.  

	INSERT INTO TABLE (col1, col2)
		VALUES('LOL', 1312)


## UPDATE
Update data values - einzelne values or whole columns & rows Reihen & Spalten.  

Set ALL values of col1 to 'lol' & col to 1234  

	UPDATE TABLE
		SET col1 = 'lol', col2 = 1234

Select specific rows/ values with WHERE - in case you want to replace a single row only use the row-ID

	UPDATE TABLE
		SET col1 = 'lol', col2 = 1234
		WHERE col1 = 'lohl'

Both commands have the same effect ('-' is replaced by '--') - UPDATE is permanently

	SELECT REPLACE(title, '-', '--') FROM categories
<br/>

	UPDATE categories SET title = REPLACE(title, '-', '--')

## DELETE 
Delete a whole dateset/ single rows e.g. with the value '5' in the column 'id'

	DELETE FROM TABLE
<br/>

	DELETE FROM TABLE WHERE id = 5

## 4. Exercise - 'locations'
### (1) Leider hat sich in diesen Daten ein kleiner Fehler eingeschlichen. Die Adresse der „Buchhandlung DOM“ ist das Domkloster 4 und nicht das Domkloster 1. Aktualisiere daher die Daten mit einem UPDATE-Befehl.
Hinweis 1: Beachte hierbei, dass die Stadt und die Postleitzahl erhalten bleibt.  
Hinweis 2: Genau aus diesem Grund speichert man die Adresse oft aufgeteilt in verschiedenen Feldern in der Datenbank, d.h. 1 Feld für die Straße, eins für die Stadt, eins für die Postleitzahl,…

	UPDATE locations SET address = 'Domkloster 4, 50667 Köln' WHERE address = 'Domkloster 1, 50667 Köln' 

### (2) Die Buchhandlung Alexanderplatz musste Anfang dieses Monats geschlossen werde. Entferne sie daher aus der Datenbank!

	DELETE FROM locations WHERE id = 2

### (3) Eine neue Buchhandlung soll nach nur 20 Jahren Bauzeit noch diesen Monat in Berlin eröffnet werden. Füge daher folgenden Eintrag in die Datenbank ein:
Titel: Buchhandlung Flughafen BER & Adresse: Melli-Beese-Ring 1, 12529 Schönefeld, Deutschland

	INSERT INTO locations ("title", "address") VALUES ('Buchhandlung Flughafen BER', 'Melli-Beese-Ring 1, 12529 Schönefeld, Deutschland')

# (5) Manage tables
## CREATE
Create a new dataset - data-type needs to be defined.  

### DATATYPES:
#### TEXT
- VARCHAR: Text with variable & max amount of chars *(performant up to 1.000 chars)*  
- TEXT: Text of defined length *(max. of 100gb)*

#### NUMBERS
1byte = 8bit --> 2^8 possible numbers.  

- SMALLINT: 2^16 *(2byte)* 
- IMNTEGER: 2^32 *(4byte)*
- BIGINT: 2^64 *(8byte)*
- DECIMAL(num1, num2): num1 = digits before the comma // num2 = digits after the comma
	- Wird nicht immer gerundet wie Zweifel
- REAL: Kommazahl *(4byte)*
- DOUBLE: Kommazahl *(8byte)* - im Zweifel genauer <br/>


Create a table 'doku' with the colums Name, Age, & Earnings 

	CREATE TABLE newsletter (
			Name VARCHAR(100)     # Max of 100 chars allowed
		    Age SMALLINT,
		    Earnings DOUBLE
		)

## MANAGE COLUMNS
Remove a table

	DROP TABLE table_name
</br>

Remove a column

	ALTER TABLE table_name DROP COLUMN col_name
</br>

Add a column

	ALTER TABLE table_name ADD COLUMN col_name datatype  
	ALTER TABLE stores ADD COLUMN city VARCHAR(127)
	ALTER TABLE stores ADD COLUMN rent DOUBLE(5, 2)
</br>

Modify a column & change its datatype

	ALTER TABLE table_name MODIFY COLUMN col_name datatype  
	ALTER TABLE stores ADD COLUMN city VARCHAR(129)
<br/>

Fill the columns of a table *(also s. Chapter 4 - 'INSERT INTO')*

	INSERT INTO stores (city, rent)
		VALUES ("Munich", 10000.00)

## NULL
- Non existing value - comperable to NA, NaN, ... - different from '' / 0 ;)  
- Can also be forbidden in certain columns with `NOT NULL` behind the data-type argument *(NULL allowed is the standard)*  
- Values can be found with `WHERE col_name IS NULL` // `WHERE col_name IS NOT NULL`  
	- When fillling values into a table, we MUST specify values for these columns *(we must not leave them out, when calling `INSERT INTO()` ;))*!
- Setting a column/ values to NULL possible with SET: `.. SET num_order = NULL WHERE ID = 234`

Example:

	CREATE TABLE table_name (
		num_orders INTEGER NOT NULL
		swag_level INTEGER NULL
		)

`INSERT INTO table_name(swag_level) VALUES(1000)` would lead to an error then!  
`INSERT INTO table_name(num_orders) VALUES(12)` works & sets 'swag_level' to NULL!  

## STANDARD VALUES
- If we have standard values these are set automatically *(instead of NULL)* with `INSERT`  

Example:

	CREATE TABLE table_name (
		num_books INT NOT NULL DEFAULT 0
		)
<br/>

	ALTER TABLE table_name (
		ADD COLUMN num_books INT NOT NULL DEFAULT 0
		)

--> In these cases: If we add a row & don't define 'num_books' its added with the value 0

## ID / Primary-Key
- Column to identify rows cleary - no duplicated values possible  
- 'auto-increment' adds a new ID automatically for all new added rows *(doesn't need to be defined in `INSERT`)*
- has key-word 'SERIAL'

Example:

	CREATE TABLE table_name (
		id SERIAL PRIMARY KEY
		title VARCHAR(100) NOT NULL
	)
<br/>

	INSERT INTO table_name (title)
		VALUES ("LOL")

--> This adds a new row with 'LOL' as title & automatically adds the primary key 'ID'

## 5. Exercise Tabellen verwalten
### (1) Erstelle eine Tabelle („newsletter“), in der wir die Registrierungen für einen Newsletter abspeichern können.
Wir benötigen folgende Spalten:
ID  
E-Mail-Adresse vom Kunden (zwingend benötigt)  
Name vom Kunden (optional)  
Alter in Jahren (optional)  

		CREATE TABLE newsletter (
		    ID SERIAL PRIMARY KEY,
		    EMail VARCHAR(1000) NOT NULL,
		    Name VARCHAR(1000),
		    Alter INTEGER
		)

### (2) Tabellen abändern
Füge anschließend folgende Spalte zu der Tabelle noch hinzu: 
- Datenschutzvereinbarung akzeptiert: Datentyp: BOOLEAN Standardmäßig ausgefüllt mit FALSE

		ALTER TABLE newsletter 
			ADD COLUMN Datenschutz BOOLEAN NOT NULL DEFAULT FALSE


# (6) Complex Queries - SubSelect
## SUBSELECT
- Query in a query aka a subquery
- Can be used for complex queries with multiple conditions

Example:

Customers table:
<br/>
| ID | name | surname |
|----|------|---------|
| 1  | Max  | Müller  |
| 2  | Paul | Schmidt |
| 3  | Pia  | Hut     |
| ...| ...  | ...     | 
<br/> 

Orders table:
<br/>
| ID   | amount | date   | customer_id |
|------|--------|--------|-------------|
| 123  | 12,23  | 1.1.22 | 1           |
| 1234 | 19,42  | 1.1.22 | 5           |
| 1234 | 123,12 | 2.1.22 | 2           |
| ...  | ...    |        | ...         |
<br/>

Add columns name & surname from the table Customers to the table Orders *(comperable to a 'join')* & map the names per ID *(Customers)* & customer_id *(Orders)*

	SELECT *,
		(SELECT name, surname FROM Customers
			WHERE Customers.ID = Orders.customer_id) 
	FROM Orders


| ID   | amount | date   | customer_id | name | surname |
|------|--------|--------|-------------|------|---------|
| 123  | 12,23  | 1.1.22 | 1           | Max  | Müller  |
| 1234 | 19,42  | 1.1.22 | 5           | ABCD | EFGHDJH |
| 1234 | 123,12 | 2.1.22 | 2           | Paul | Schmidt |
| ...  | ...    |        | ...         | ...  | ...     |

## Renaming of tables
Instead of calling all columns from tables by 'tablename.column' we can abbreviate tablenames and make it more compact - this is especially important for complex queries!

Example: Get the all IDs of 'Orders' and their corresponding amount of orders

	SELECT DISTINCT(O.customer_id),
		(SELECT COUNT(*) FROM Orders AS O2
			WHERE 02.customer_id = 0.customer_id)
	FROM Orders AS O

## NAME SUBSELECT COLUMNS (& use them to filter with WHERE)
Added Columns can be renamed - if we need multiple cols pasted in a single col: `SELECT (id, time) FROM orders` // `SELECT CONCAT(id, time) FROM orders`

	SELECT O.timestamp,
		(SELECT firstname FROM customers 
		 	WHERE customers.ID = o.ID) AS COLNAME_XY
	FROM Orders AS O
	WHERE COLNAME_XY LIKE A%

## SUBSELECTS over multiple rows
Einer ID können mehrere Zeitstemple zugeordnet werden, sodass verschiedene IDs eine verschiedene Anzahl an Zeilen bekommen würde.  
Führt zum Fehler, wenn `ORDER BY timestamp DESC LIMIT 1` fehlt!  

	SELECT *,
		(SELECT timestamp FROM Orders
			WHERE Orders.customer_ID = customer.ID
			ORDER BY timestamp DESC LIMIT 1)
	FROM Customers


## 6. Exercise SUBSELECTS - Versuche, alle Aufgaben jeweils mit exakt einer Query zu lösen!
Betrachte die Tabelle books. In der Spalte „language“ ist die jeweilige Sprache von einem jeden Buch notiert.

### (1) Wie viel % der Bücher sind in deutscher Sprache? Versuche dies mit einer Query zu lösen!
Tipp 1: Mit einem SELECT (SUBQUERY), (SUBQUERY) kannst du 2 komplett unterschiedliche Subqueries an die Datenbank schicken, sofern sie jeweils nur einen Wert aggregieren (z.B. die Anzahl ermitteln,…). Es wird hier nicht zwingend die Angabe einer Tabelle benötigt! <br/>
Tipp 2: Auch kannst du die Ergebnisse direkt miteinander verrechnen: SELECT (SUBQUERY) / (SUBQUERY). Wichtig: Funktioniert so nur in MySQL, unter PostgreSQL gibt es noch was zu beachten – siehe Musterlösung.

	SELECT
		(SELECT COUNT(*) from books WHERE language = 'de')::float /  / # Amount of german books - type conversion important!
		(SELECT COUNT(*) from books)::float /                          # Amount of all books


### (2) Erstelle eine Auflistung aller Bücher inkl. dem jeweiligen Thema!
Betrachte die Tabelle books. Jedes Buch hat ein Thema / eine Kategorie, die entsprechende Information hierzu findet sich in der Tabelle books_subjects. 

	SELECT title, 
	    (SELECT title FROM books_subjects 
	        	WHERE books.subject_id = books_subjects.id) AS Category
	FROM books

### (3) Zu welchem Thema gibt es am meisten Bücher, und wie viele Bücher sind das? 
Betrachte die Tabelle books_subjects, ein Thema kann von mehreren Büchern verwendet werden. Wie oft kommt das beliebteste Thema vor? 

	SELECT title,
	    (SELECT COUNT(*) FROM books 
	            WHERE books.subject_id = books_subjects.id) AS topic_freq
	FROM books_subjects ORDER BY topic_freq DESC

### (4) Betrachte die Tabelle books. Welcher Autor hat bisher am meisten Bücher veröffentlicht?
Tipp 1: Ermittle also zuerst alle unterschiedlichen Autoren, die es in der Tabelle gibt <br/> 
Tipp 2: Erweitere anschließend die Query, sodass für jeden gefundenen Autor eine Subquery gestartet wird, die zu diesem Autor die entsprechende Anzahl an Büchern ermittelt <br/>
Tipp 3: Beachte hierbei, dass hier das Subselect 2x auf der gleichen Tabelle ausgeführt wird – hier wirst du die Tabellen also u.U. mit einem AS benennen müssen! <br/> 

Hinweis: Das würde mit einem GROUP BY sehr viel effizienter gehen – das haben wir uns aber noch nicht angeschaut…

		SELECT DISTINCT(creator),
		    (SELECT COUNT(*) FROM books AS books_new 
		            WHERE books_new.creator = books_old.creator) AS amount_books
		FROM books AS books_old ORDER BY amount_books DESC

# (7) JOINS
`JOINS` are used to merge different dataframes to a single one.  
There are different types: 
- CROSSJOIN
- LEFTJOIN/ RIGHTJOIN
- INNERJOIN
- FULLJOIN

A: <br/>
| ID | Name   |  
|----|--------|  
| 1  | Max    |  
| 2  | Moritz |  
<br/>

B: <br/>
| C_ID | Course |   
|------|--------|   
| 1    | Eng    |   
| 2    | Esp    |   
<br/> 

## CROSSJOIN
Every entrance from A is comined with every entrance from B. <br/>
New DF has the dimensions `nrow(A) * nrow(B)`- get really big quite easily! <br/>

Example: Cross-Join of A & B basically get all possible row combinations:   

	SELECT * FROM A
	CROSS JOIN B
	WHERE A.ID = B.C_ID
  

| ID | Name   | C_ID | Course |  
|----|--------|------|--------|  
| 1  | Max    | 1    | Eng    |  
| 1  | Max    | 2    | Esp    |  
| 2  | Moritz | 1    | Eng    |  
| 2  | Moritz | 2    | Esp    |  
<br/>

We could also select only certain columns & merge the DFs based on 'ID' & 'C_ID':    

	SELECT A.ID,
		   A.Name,
		   B.Course
	FROM A
	CROSS JOIN B
	WHERE A.ID = B.C_ID
  

| ID | Name   | Course |  
|----|--------|--------|  
| 1  | Max    | Eng    |    
| 2  | Moritz | Esp    | 

## INNER JOIN 
Join DFs based on a certain column & do not even create all possible combinations as `CROSS JOIN`

Same effect as the `CROSS JOIN B WHERE A.ID = B.ID` as we merge the rows of a DF based on certain columns - better performance!  
It only keeps intersection of the two DFs within the selected column - only 'ID'/ 'C_IDs' in 'A' + 'B'.    
We can also add a further `WHERE` at the end of the query

	SELECT * FROM A
		INNER JOIN B ON A.ID = B.C_ID

## LEFT/ RIGHT/ FULL JOIN
#### LEFT
Match all rows of 'A' with the corresponding rows of 'B' that match in 'ID' & 'C_ID'.  
We keep all IDs of 'A' and merge the columns from 'B' - if an ID appears in 'A' but not 'B' the merged columns get NULL values.  
IDs that appear only in 'B' will not be in the joint table.  

	SELECT * FROM A
		LEFT JOIN B ON A.ID = B.C_ID

#### RIGHT 
Analog to left, but 'A' is changed with 'B'.  

#### FULL
Merge DFs based on a column, wherby no values are lost - if there is a value only in one of the DFs, there will be NULL values in the merged columns.  

	SELECT * FROM A
		FULL JOIN B ON A.ID = B.C_ID

## 7. Exercise JOINS
Hinweis: Diese Aufgaben ähneln sich u.U. den Aufgaben zum Abschnitt „Subselect“ – sie sind aber unterschiedlich!

### (1) Betrachte die Tabelle books. 
Jedes Buch hat ein Thema / eine Kategorie (Spalte: subject_id), die entsprechende Information hierzu findet sich in der Tabelle books_subjects.

#### 1.1 Erstelle eine Auflistung aus Büchern sowie den entsprechenden Themen, verwende hierzu einen JOIN
		SELECT * FROM books
		    LEFT JOIN books_subjects ON books.id = books_subjects.id

#### 1.2 Es gibt Bücher, bei denen die Spalte subject_id auf NULL gesetzt ist. 
Wenn du ein SELECT auf der Tabelle „books“ ausführst, und die Tabelle „books_subjects“ per JOIN vernüpfst – welcher/welche JOIN-Typ(en) sorgt dafür, dass alle Bücher übersprungen werden,  wo die Spalte subject_id NULL ist?

		SELECT * FROM books
    		LEFT JOIN books_subjects ON books.subject_id = books_subjects.id

#### 1.3 Wie viele deutschsprachige Liebesgeschichten (Thema: „Love stories“) gibt es? 
Löse diese Frage – sofern möglich - mit einer einzigen Datenbankabfrage, ohne zuvor die ID des Themas „Love stories“ zu ermitteln!

		SELECT COUNT(*) FROM books
		    LEFT JOIN books_subjects ON books.subject_id = books_subjects.id
		    WHERE books.language = 'de' 
		    AND books_subjects.title LIKE '%Love stories%'

# (8) GROUP BY
Group the data according to a certain column - faster than SUBSELECT & can be combined with functions.  
All columns that are used in `GROUP BY` must be in the `SELECT`!  
<br/>

Example: Get the various titles & their corresponding amount fo occurences.  

	SELECT title, COUNT(*),
		FROM A
		GROUP BY title

Example: Get the average & total sum of spent money by each customer.  

	SELECT customer_id, SUM(amount), AVERAGE(amount)
		FROM A
		GROUP BY customer_id

## Filter
- `WHERE` is used to filter the data, AFTER the data has been grouped  
- `HAVING` is used to filter the data, BEFORE the data has been grouped  
- Grouping with multiple columns is possible as well: `GROUP BY col1, col2`
- Group by the result of a function is possible as well: `GROUP BY DATE_PART('year', date_col)`

Example: Get the total amount of all bills > 200 for each year  

	SELECT DATE_PART('year', date), SUM(amount)
		FROM Orders
		GROUP BY DATE_PART('year', date)
		HAVING SUM(amount) > 200          # Only rows with sum amount > 200, after we have already filtered

Example: Get the customers with the maximum spendings

	SELECT customer_id, SUM(amount)
		FROM Orders
		WHERE customer_id IS NOT NULL     # Filter out the rows without customer ID
		GROUP BY customer_id
		ORDER BY SUM(amount)
		LIMIT 1

## 8. Exercise GROUP BY
### (1) In der Tabelle „baby_names“ finden sich Geburtsstatistiken aus den USA. 
#### 1.1 Welcher Vorname wurde insgesamt am häufigsten vergeben? Das Geschlecht spielt hierbei keine Rolle
		SELECT name, SUM(count) FROM baby_names
		    GROUP BY name 
		    ORDER BY SUM(count) DESC

#### 1.2 Welcher Vorname wurde im Jahr 1950 am häufigsten vergeben? Das Geschlecht spielt hierbei keine Rolle
		SELECT name, count FROM baby_names
		    WHERE year = 1950
		    GROUP BY name, count
		    ORDER BY count DESC 

#### 1.3 Erstelle eine Auflistung von allen Vornamen, welche insgesamt mehr als 5 Millionen mal vergeben wurden. 
Versuche, diese Auflistung mit nur einer Query zu generieren. Wie viele Einträge erscheinen hier in der Auflistung?

		SELECT name, SUM(count) FROM baby_names
		    GROUP BY name 
		    HAVING SUM(count) > 5000000
		    ORDER BY SUM(count) DESC

#### 1.4 In welchem Jahr wurden am meisten verschiedene Vornamen vergeben?
		SELECT year, COUNT(DISTINCT(name)) FROM baby_names
		    GROUP BY year
		    ORDER BY COUNT(DISTINCT(name)) DESC

#### 1.5 Gibt es insgesamt mehr weibliche oder mehr männliche Babys in der Statistik?
		SELECT gender, SUM(count) FROM baby_names
		    GROUP BY gender
		    ORDER BY SUM(count) DESC

### 1.6 Mit welchem Buchstaben begann im Jahr 2010 der Name der meisten Babys? 
Den ersten Buchstaben kannst du über SUBSTR(spalte, 1, 1) ermitteln.

		SELECT SUBSTR(name, 1, 1), SUM(count) FROM baby_names
		    WHERE year = 2010
		    GROUP BY SUBSTR(name, 1, 1)
		    ORDER BY COUNT(*) DESC

#### 1.7 Bonus (nicht zwingend GROUP BY): Wie viele Vornamen aus dem Jahr 1880 gibt es im Jahr 2010 nicht mehr?  
		SELECT name FROM baby_names
		    WHERE year = 1880 AND
		    (SELECT COUNT(*) FROM baby_names as b2 WHERE b2.name = baby_names.name AND b2.year = 2010) = 0

### (2) Betrachte die Tabelle „books“, in dieser sind diverse Daten zu Büchern gespeichert. 
Fast jedes Buch hat ein verknüpftes Thema (Spalte: subject_id), dieses Thema wird in der Tabelle „books_subjects“ abgespeichert.

#### 2.1 Zu welchem Thema gibt es am meisten Bücher? Löse diese Frage mit einem JOIN + GROUP BY
		SELECT books_subjects.title, COUNT(books_subjects.title) FROM books
		    LEFT JOIN books_subjects ON books.subject_id = books_subjects.id
		    GROUP BY books_subjects.title
		    ORDER BY COUNT(books_subjects.title) DESC # --> 1.750 Fiction

#### 2.2 Welcher Autor hat am meisten Liebesromane (books_subjects.title = 'Love stories') geschrieben? 
Löse diese Frage mit einem JOIN + GROUP BY

		SELECT books.creator, COUNT(books.creator) FROM books
		    LEFT JOIN books_subjects ON books.subject_id = books_subjects.id
		    WHERE books_subjects.title LIKE '%Love stories%'
		    GROUP BY books.creator 
		    ORDER BY COUNT(books.creator) DESC # --> Bar Amelia & Bacon Josephine: 5x LoveStories

#### 2.3 Welcher Autor hat am meisten Downloads? 
Beachte, dass ein Autor mehrere Bücher haben kann, die entsprechenden Downloads müssen aufsummiert werden <br/>
 Wichtig: „Various“, NULL, Anonymous,… zählen hierbei nicht als Autor

		SELECT books.creator, SUM(books.downloads) FROM books
		    GROUP BY books.creator 
		    ORDER BY SUM(books.downloads) DESC # --> Austen, Jane: 44.177x

#### 2.4 Schreibe eine Query, die alle Autoren ausgibt, die mehr als 30.000 Downloads mit ihren Büchern erreicht haben. 
Frage: Wie viele Autoren sind in dieser Auflistung enthalten? - Wichtig: „Various“, NULL, Anonymous,… zählen hierbei nicht als Autor

		SELECT books.creator, SUM(books.downloads) FROM books
		    GROUP BY books.creator 
		    HAVING SUM(books.downloads) > 30000
		    ORDER BY SUM(books.downloads) DESC # --> 4 authors

#### 2.5 Wir möchten ein neues Buch veröffentlichen, dieses soll sich aber so gut wie möglich verkaufen. 
In welcher Sprache sollten wir dieses Buch schreiben? Bzw. anders ausgedrückt: Für welche Sprache gibt es aktuell durchschnittlich die meisten Downloads pro Buch?

		SELECT language, SUM(books.downloads) / COUNT(*) FROM books
		    GROUP BY books.language 
		    ORDER BY SUM(books.downloads) / COUNT(*) DESC #--> KO 455 sales per book#

# (9) Time & Date
Important & very common date formats.  

## UNIX-TimeStamp
- Represent a date & time as an integer    
- 01.01.1970 is the start time-point & we count the seconds from there - e.g. 1571657687 equals 21.10.2019 11:34:17 UTC *'(UTC is time-zone)*  
- Can be used for calculations
- **Atttention:** With 32-Bytes the possible values are limited to 1901 - 2038  
<br/>

**Formats _(Postgre)_:** 
- **Attention:** Formats are different between MySQL & Postgre 
- Time: `TIME`
- Time + TimeZone: `TIME WITH TIMEZONE`
- Date: `DATE`
- Date + Time: `TIMESTAMP`
- Date + Timet + TimeZone: `TIMESTAMP WITH TIMEZONE`
<br/>

**TIMEZONE:** The value is converted to `UTC` *(common world-time)* & back to the original time-zone when quieried.  
<br/>
Example on how to create a DF with time-columns & how to fill it:  

	CREATE TABLE table_name (
		id serial,
		c_timestamp TIMESTAMP NULL,
		c_timestamp_tz TIMESTAMP WITH TIMEZONE NULL,
		c_date DATE NULL
		PRIMARY KEY id
		)
<br/>

	INSERT INTO table_name (c_timestamp, c_timestamp_tz, c_date)
		VALUES ('2020-08-12 12:00:00', '2020-08-12 12:00:00', '2020-08-12')

- Get the possible time-zones: `SELECT * FROM py_timezone_names`  
- Adjust time-zone: `SET TIME ZONE 'Europe/Berlin'`
- Get current time-zone: `SHOW TIMEZONE`  
<br/>

## Calculate with Date- & Time-Values
- Current time w/o timezone: `LOCAL TIMESTAMP`
- Current time w/ timezone: `CURRENT_TIMESTAMP`
- Extract parts: `DATE_PART(part, TimeStamp)` 
	- part: 'year', 'month', 'day', 'hour', ...  

#### Calculate

	SELECT timestamp `2020-01-01 00:00:00` - timestamp `2019-01-01 00:00:00`
<br/>

	SELECT timestamp `2020-01-01 00:00:00` + interval '2 days' # add 2 days to the current time  
<br/>

	SELECT DATE_PART('year', timestamp), 
		   timestamp + interval '2 hours'
	FROM Orders

## Format time & date
Adjust the format of a timestamp to a character with `TO_CHAR(timestamp, EXTRACTOR)`.  
<br/>

EXTRACTOR:  
- HH24 = 0-24 hours
- MI = 0-59 miuutes
- SS = 0-59 seconds
- YYYY = year
- Month = Month as 'Jan', 'Feb', ... 
- MM = Month as 01, 02, ...
- day = Mon, Tue, ...
- DD = day as 01, 02, ...

Example:

	SELECT timestamp, 
		   TO_CHAR(timestamp, 'DD.MM.YYYY HH24:MM:SS') # Reformat the 'timestamp' column
	FROM Orders

## 9. Exercise - DATUMSWERTE
### 1 Betrachte die Tabelle „books“, in dieser sind diverse Daten zu Büchern gespeichert.
#### 1.1 Wie viele Bücher wurden im Jahr 2005 herausgegeben?
		SELECT COUNT(*) FROM books
		    WHERE DATE_PART('year', issued) = '2005'

#### 1.2 Betrachte die Spalte „issued“ - in welchem Monat werden im Schnitt am meisten neue Bücher herausgegeben?
		SELECT DATE_PART('month', issued), COUNT(*) AS counts FROM books
		    GROUP BY DATE_PART('month', issued)
		    ORDER BY counts DESC

#### 1.3 Schwer: Welcher Autor war am längsten aktiv? 
Anders ausgedrückt: Bei welchem Autor ist die Zeitdifferenz zwischen dem Herausgabedatum seines ersten Buches und seines letzten Buches am größten?

		SELECT creator, MIN(issued), MAX(issued), MAX(issued) - MIN(issued) AS DIFF from books
		    GROUP BY creator
		    ORDER BY DIFF DESC

# (10) Index
Used to speed up queries - reduce the search time from `O(n) to O(log(n))` *(calc.-time from depending linear on n, to log(n))*.  
With an Index, SQL can speed up the search with a 'binary search tree'.  

## CREATE INDEX
Example - a regular query that checks every row:   

	SELECT * FROM orders
		WHERE timestamp > '2010-01-01 00:00:00' AND timestamp < '2011-01-01 00:00:00'

Now we add an index called 'index_col_name' to the column 'timestamp' in orders:  

	CREATE INDEX index_col_name ON orders(timestamp, ASC)

The same query is faster now, as SQL automatically uses the index!  

## INDEX over multiple columns
Create an index over multiple columns to speed up more complex queries - e.g. with `WHER firstname = 'Dave' AND lastname = 'Paul'`.  

	CREATE INDEX customer_full_name ON orders(
		firstname ASC,
		lastname DESC
		)

## UNIQUE INDEX
Create a unique index based on the value of a column - addind a value to the DF that already exists will throw an error then!  

	CREATE UNIQUE INDEX customer_mail IN orders(email)
<br/>
Alternativly:  

	ALTER TABLE customers ADD CONSTRAINT customer_email UNIQUE(email)

## 10. Exercise INDEXE
### (1) Betrachte die Tabelle „baby_names“.
#### 1-1 Sortiere die Tabelle nach dem Namen. 
		SELECT * FROM baby_names
    		ORDER BY name ASC # --> 00:00:01.493

#### 1-2 Wie lange dauert dies im Vergleich zu einer Sortierung nach einer anderen Spalte? 
		SELECT * FROM baby_names
    		ORDER BY year ASC # --> 00:00:01.392

    	SELECT * FROM baby_names
    		ORDER BY gender ASC # --> 00:00:01.302

    	SELECT * FROM baby_names
    		ORDER BY id ASC # --> 00:00:01.669

    	SELECT * FROM baby_names
    		ORDER BY count ASC # --> 00:00:01.210

#### 1-3 Wie könntest du diese Sortierung beschleunigen?
		CREATE INDEX name_id ON baby_names (
    		name ASC
		)
<br/>

		SELECT * FROM baby_names
		    ORDER BY name ASC # --> 00:00:00.782

OBACHT: Andere Ordnung als IDX -> langsamer

		SELECT * FROM baby_names
    		ORDER BY name DESC # -->  00:00:02.167

# (11) FOREIGN KEY
Used to validate the relation between variables.  
'customer' has an ID-column, such that each customer has a unique ID *(ID)*.  
'orders' also has ID-column for the customer *(customer-ID)*.  
These IDs should be uniquly linkable & we don't want these links to be destroyed - both need the same data-type!    

Example when you create a table - `customers(id)` has to be unique:

	CREATE TABLE orders (
		..., 
		customer_id = big int,
		FOREIGN KEY (customer_id) REFERENCES customers(id)
		)

Alternativly add it to exisiting tables

	ALTER TABLE orders ADD FOREIGN KEY (customer_id)
		REFERENCES customer(id)

## ON UPDATE
Decide what happens to the FOREIGN ID, when an `UPDATE` is applied to it.  

- Can not be changed: `ON UPDATE RESTRITCT`
- Set it to NULL if changed: `ON UPDATE SET NULL`
- Change the primary key in both DFs: `ON UPDATE CASCADE`

## ON DELETE
Decide what happens to the FOREIGN ID, when an `DELETE` is applied to it.  

- Must not be deleted: `ON DELETE RESTRICT`
- If deleted set to NULL: `ON DELETE SET NULL`
- If deleted in one table, delete in both: `ON DELETE CASCADE`

Example 1:

	ALTER TABLE orders 
		ADD FOREIGN KEY (customer_id) REFERENCES customers(id)
		ON UPDATE CASCADE
		ON DELETE SET NULL

Example 2:

	CREATE TABLE orders2 (
		id BIGSERIAL,
		customer_id int, 
		FOREIGN KEY (customer_id) REFERENCES customers(id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
		)
<br/>
Now we add an new 'customer_id' to 'orders2' -> automatically adds 'id' in 'customers'

	INSERT INTO orders2 (customer_id) VALUES(162)
<br/>
Can not change the value of the reference ID

	UPDATE customers SET id = 1620 WHERE id = 162


# (12) VIEW
A `VIEW` can save a query as a virtual table - if something changes in the data, the results of the query in the virtual table change aswell!  
It is like a function for a query & cery handy for complex queries, but `UPDATES` & `INSERT` are limited, as well as index can't be used!  

## CREATE VIEW

Example for a complex query:

	SELECT firstname, lastname,
		SELECT (timestamp FROM orders WHERE orders.customer_id = customers.ID)
	FROM customers

This query can now be saved into a VIEW:

	CREATE VIEW customer_view AS 
		SELECT firstname, lastname,
			SELECT (timestamp FROM orders WHERE orders.customer_id = customers.ID)
		FROM customers

Call this view & optionally add further filters: 

	SELECT customer_view WHERE last_order IS NOT NULL

## CREATE MATERIALIZED VIEW
Similiar to `CREATE VIEW`, but with this the data of the query is actually saved as data.  
Hence a MATERIALIZED VIEW is faster than a regular VIEW, but needs more memory!  
In case the original data change, MATERIALIZED VIEW needs to refreshed to get the results on the changed data.  

	CREATE MATERIALIZED VIEW customer_view_m AS
		SELECT firstname, lastname,
			SELECT (timestamp FROM orders WHERE orders.customer_id = customers.ID)
		FROM customers

# (13) COLLACTION
When ordering data according to a text, we can change the language specific ABC for that.  
In the german ABC, the letter 'Ä' is treated as an 'A' & with english 'Ä' is not equal to 'A'.  
Can be changed within the GUI.  

# (14) TRANSACTION
## START TRANSACTION 
Used when sending multiple queries to a single databank - e.g. A sends 50€ to B: A - 50€ & B + 50€  
Two `UPDATE` commands are needed in this scenario & it could happen that something crashes wihtin the two commands.  
Either update both or none with `TRANSACTION`:

	START TRANSACTION
		UPDATE A ...
		UPDATE B ...
	COMMIT // ROLLBACK

All commands below `START TRANSACTION` are temporary wait for `COMMIT` to run // `ROLLBACK` to abort!  


Account:  

| ID | Name   | Balance |  
|----|--------|---------|  
| 1  | Max    | 100     |  
| 2  | Moritz | 150     |  

Max sends Moritz 50€  

Oldschool - could happen that only one query is succesful:    

	UPDATE Account SET Balance = Balance + 50 WHERE name = 'Moritz'   
	UPDATE Account SET Balance = Balance - 50 WHERE name = 'Max'  
  
Newschool - ensure both commands run at the same time:  

	START TRANSACTION
		UPDATE Account SET Balance = Balance + 50 WHERE name = 'Moritz'
		UPDATE Account SET Balance = Balance - 50 WHERE name = 'Max'
	COMMIT

## Locking
When Max sends his 75€ to Moritz & hit 'send money' twice then this could be run twice then... - prevent this with `FOR UPDATE`.  
`FOR UPDATE` ensures that the query only runs again after `COMMIT` - so if there are multiple transactions from 'Max', they have to queue & wait for the previous transactions to be commited!  

	START TRANSACTION 
		UPDATE Account SET Balance = Balance - 75 WHERE name = 'Max' FOR UPDATE
		UPDATE Account SET Balance = Balance + 75 WHERE name = 'Moritz'
	COMMIT

There are many more nuancen for locking - e.g. Write-Lock, Read-Lock, Table-Lock, ... - google this with 'DeadLocks postgre SQL'.  

# (15) Modeling databases
## 1st Normalform
Every attribute of the relation needs an atomic value range and the relation has to be free of repeating groups - this basically means **no composite values**!  

| Name            | Semester | Subjects              |  
|-----------------|----------|-----------------------|  
| Max Mauer       | 3        | Algebra 1, Analysis 3 |  
| Paul Mustermann | 1        | Math 1, CS2           |  
<br/>
This table violates the 1st normalform, as the columns 'Name' & 'Subjects' contain multiple values & hence it's no atomic value range!  
The corrected version splits up 'Name' into first- & lastname + generates a seperate row for every subject:  

ID | Firstname | Lastname   | Semester | Subjects   |  
---|-----------|------------|----------|------------|  
1  | Max       | Mauer      | 3        | Algebra 1  |  
1  | Max       | Mauer      | 3        | Analysis 3 |  
2  | Paul      | Mustermann | 1        | Math1      |  
2  | Paul      | Mustermann | 1        | CS2        |  
<br/> 

## 2nd Normalform  
A relation is in 2nd normal form if the first normal form exists & no non-primary attribute depends functionally on a true subset of a key candidate.  
- key candidate: Primary key - must not repeat *(e.g. ID + Subjects)*  
- non-primary attribute: All columns that are no primary keys *(e.g. Semester, first- & lastname)*  
<br/>

**Non-primary attributes only depend on the ID & not any other colum -> depend only on a part of the primary keys**  
*(e.g. 'Max', 'Mauer' & '3' only depend on the ID and not on 'Subjects')*   
<br/>

Example: Split the DF from '1st Normalform' into two seperate DFs:

| ID | Firstname | Lastname   | Semester | Start      |  
|----|-----------|------------|----------|------------|  
| 1  | Max       | Mauer      | 3        | 01.01.2020 |  
| 2  | Paul      | Mustermann | 1        | 01.01.2021 |  
<br/>

| ID | Subject    |  
|----|------------|  
| 1  | Algebra 1  |  
| 1  | Analysis 3 |  
| 2  | Math 1     |  
| 2  | CS2        |  
<br/>

Now none of the tables contain repated values, while we loose no information!  

## 3rd Normalform  
3rd normal form exists if the relation schema is in 2nd normal form and no non-primary attribute is transitively dependent on a key candidate.  
- transitively dependent: a column is not the result of an other column (redundancy)
<br/> 

Example: From 'Start' we can know the 'Semester' & do not actually need it to get this information!   

| ID | Firstname | Lastname   | Semester-Start-ID|   
|----|-----------|------------|------------------|  
| 1  | Max       | Mauer      | 1                |  
| 2  | Paul      | Mustermann | 2                |   
<br/>

| ID | Subject    |  
|----|------------|  
| 1  | Algebra 1  |  
| 1  | Analysis 3 |  
| 2  | Math 1     |  
| 2  | CS2        |  
<br/>

| Semester-ID | Start      |  
|-------------|------------|  
| 1           | 01.01.2020 |  
| 2           | 01.01.2021 |  
<br/>

==> Now the data contains no repetative information & everything is clear - Normalform is not always handy..!  

## Alternatives to Normalform  
3 tables for the orginaisation of a university:   
- Student: ID, Firstname, Lastname, Title  
- Lecture: Title, Desc, When  
- Instructor: Firstname, Lastname  
<br/> 

**'Student' &harr; 'Lecture'**: [0,n] &harr; [0,n]   
Many-to-Many relation, as a student can go to multiple lectures!  
<br/> 

**'Lecture' &harr; 'Instructor'**: [0,n] &harr; 1   
One-to-Many relation, as a prof can have multiple lectures, but every lecture only has one prof!   
<br/>

This could also be done differently as well with an additonal table 'Lecture_Studtens' mapping the student-ID and the Lecture-Title.  
<br/>

#### Basic Concept:
- Every object has a seperate table *(one for students, one for lecture, ...)*  
- How are the relations between the objects:  
	- Many-to-Many  
	- Many-to-One  
  
## Postgre Example:
### 1) Create the tables
	CREATE TABLE students (
		id bigserial NOT NULL,
		firstname character varying(100) NOT NULL,
		lastname character varying(100) NOT NULL,
		title character varying(100) DEFAULT '',
		PRIMARY KEY (id)
		)
<br/>

	CREATE TABLE instructors ( id, firstname, lastname, PRIMARY KEY (id) )
<br/> 

	CREATE TABLE lectures ( id, title, desc, when, instructor_id,  PRIMARY KEY (id))
<br/>

### 2) Connect the tables

	ALTER TABLE lectures 
		ADD CONTRAINT lectures_instructores_id FOREIGN KEY (instructor_id)
		REFERENCES instructors (id)
	ON UPDATE restrict  
	ON DELETE restrict
  
Connect the column 'instructor_id' from 'lectures' to the 'id' in 'instructors'!  

# (16) Permissions  
Up to now, we have used it as administrator & have access to everything in PostgreSQL.  
We can restrict permissions of users *(& hackers)*, such that they can not:  
- Modify tables afterwards  
- Have access to all tables  
- see sensitive data  
  
To improve security, an application should only have access to the tables it actually needs!  
Big differences between MySQL & PostgreSQL!  

## PostgreSQL
### Add new user
*SERVERS* &rarr; *Login / Group Rules* &rarr; *right-click* &rarr; *CREATE* &rarr; *Login / Group Rule*  
<br/> 

Create a new user with name, password & privileges:  
- Login possible?
- Super User? *(= Admin)*  
- Create users?  
- Create databases?  
- Inherit rights?  

### Grant access to tables
The newly created user has still no acccess to the data! We need to grant access first:  
*Select Table on left side* &rarr; *right-click* &rarr; *Security* &rarr; *Priviliges* &rarr; *select user* &rarr; *grant rights* (ALL/ SELECT/ INSERT/ DELETE/ UPDATE/ ...)  <br/>
'WITH GRANDOPTION': User can allow same access he has!  
<br/> 

### Column authorization
We can also stop access to sensitive columns:  
- Remove the user from the current table: *right-click on DF* &rarr; *Properties* &rarr; *Securities* &rarr; *Remove user*  
- Access to single columns: *Opem the DF* &rarr; *right-click on a column* &rarr; *Priviliges* &rarr; *select user* &rarr; *select rights*  

# (17) Stored Functions & Procedures
Create your own programms & directly run complex queries.  
A stored procedure is basically like a stored function but doesn't return any values and is called via `CALL procedure` and not like `SELECT function`.   

Example create function 'select_one' that doesn't take arguments, runs SQL queries & returns '1' as bigint:  

	CREATE FUNCTION select_one() RETURNS bigint AS $$
		SELECT 1 AS Result
	$$ LANGUAGE SQL;
<br/>

To run the function now: 

	SELECT select_one()
<br/>

## Return multiple values
To return multiple values from a function add `SET OF` after `RETURN` - in the example, the function returns a list of 'bigint' values instead of a single one.  

	CREATE FUNCTION get_ids() RETURNS SET OF bigint AS $$
		SELECT id FROM customers
	$$ LANGUAGE SQL;
<br/> 

	SELECT get_ids()
<br/>

## Return a table
To return a table add `TABLE` after `RETURN` and assign the colnames & their corresponding types *(TABLE(col, coltype, col, coltype, ...))*.  

	CREATE FUNCTION table_() RETURN TABLE (id, bigint, email, varchar) AS $$
		SELECT id, email FROM customers
	$$ LANGUAGE SQL;
<br/> 

	SELECT * FROM table_()
<br/> 

## Pass parameters to a function  
A function can also recieve a set of values as parameters - e.g. take to character values and paste them together *($1 = 1st argument, $2 = 2nd argument, ...)*:    

	CREATE FUNCTION get_name(varchar, varchar) RETURN varchar AS $$
		CONCAT($2, ', ', $1)
<br/> 

	get_name("LOL", "xD")
<br/>

## Optimize functions  
### IMMUTABLE
Function doesn't change the original data & result only depends on the parameters - same parameters, same results!  

	CREATE FUNCTION get_name(varchar, varchar) RETURNS VARCHAR IMMUTABLE AS $$ ... $$
<br/>

### STABLE
Can't change values in the original data and only look them up.  

	CREATE FUNCTION get_customers(bigint) RETURNS TABLE (...) STABLE AS $$
		SELECT * FROM customers WHERE id = $1
	$$ LANGUAGE SQL;
<br/>

### VOLATILE
Result of a function can change & hence the function is executed separately each time - not really optimizable..!  

	CREATE FUNCTION ... RETURN ... VOLATILE AS $$ ... $$ 
<br/>

## Function privileges
Decide if a function runs with the rights of the function creater *(`SECURITY DEFINER`)* or the function caller *(`SECURITY INVOKER`)*!  

	CREATE FUNCTION get_customers 
		RETURNS TABLE (...) 
		SECURITY DEFINER
		VOLATILE AS $$
			SELECT * FROM customers WHERE id = $1
		$$ LANGUAGE SQL;
<br/>

## Log-Files
There is a databank 'logg' existing with 'ID' & 'TimeStamp' as columns.  
Everytime a function is called, we can add data to the logging databank *(ID is set automatically to every new entrance, so we only need to add the time)*.    

	CREATE FUNCTION c_w_logg() RETURNS TABLE(id, bigint, email, varchar) VOLATILEN AS $$
		INSERT INTO logg('timestamp') VALUES(CURRENT_TIMESTAMP);
		SELECT id, email FROM customers
	$$ LANGUAGE SQL;
<br/>

## DrawBacks
- Tests are more complicated  
- Functions & Procedures depend on the databanksystem
- SQL is actually only a databank and hence not optimal to write applications...  

## 11. Exercise 
Schreibe eine Funktion, die - anhand einer ID - einen einzelnen Kunden von customers zurück gibt & tracked wann welche ID angefragt wurde.

### (1) Erstelle eine 'Logg'-Tabelle, um die Daten zu speichern
	CREATE TABLE loggs (
	    ID SERIAL PRIMARY KEY,
	    time_stamp TIMESTAMP WITH TIME ZONE,
	    queried_ID BIGINT
	)

### (2) Erstelle eine Funktion, die anhand der ID einen customers-Eintrag zurück gibt & die Anfrage, sowie die angefragte ID loggt
	CREATE FUNCTION customer_info_w_logg(bigint) RETURNS table(id bigint, email varchar, name_full varchar) AS $$
	    INSERT INTO loggs("time_stamp", "queried_id") VALUES(CURRENT_TIMESTAMP, $1);
	    SELECT id, email, concat(firstname, lastname) FROM customers
	        WHERE ID = $1
	    $$ LANGUAGE SQL

### (3) Erstelle eine Anfrage & vergleich die Ergebnisse + check ob es gelogged wurde
#### (3-1) Orginal ID
	SELECT id, email, concat(firstname, lastname) FROM customers
	    WHERE ID = 23

#### (3-2) Original loggs
	SELECT * FROM loggs

#### (3-3) Run the request + check the loggs table
	SELECT * FROM customer_info_w_logg(23)
<br/>

	SELECT * FROM loggs
<br/>

# (18) Full text search
- We have learned to use `.. WHERE text LIKE '%..%'` to search a column for text, but there is not much space for optimization...  
- Text columns often contain useless words / too much information   
- Stemming: Go from plural to singluar *(Bücher -> Buch, ...)*  
- Full-text search is not trivial and we can use 'Hadoop', 'Spark' or 'Elastic Search' for optimization.  

Example: 'shakespeare' contains all sentences of 'Romeo & Julia' and we search for sentences with 'Romeo' in it:  

	SELECT * FROM shakespeare WHERE contents LIKE '%Romeo%'  
<br/>
&rarr; This is pretty slow + doesn't apply any processing as stemming/ to lower / ...  

## to_tsvector
Function to process text data *(stemming, to lower, rm stopwords, ...)* & optimize it for search *(words get indices)* - has the form of `to_tsvector(Languane, Text)`:  

	SELECT to_tsvector('english', 'world berlin germany')
<br/>
&rarr; This returns a mapping of: 'world': 1, 'berlin': 2, 'german': 3    
<br/> 

	SELECT to_tsvector('german', 'Das Smartphone ist bestes')
<br/>
&rarr; This returns a mapping of: 'smartphone': 2, 'beste': 4  
<br/> 

## Querying
`@@` is used as search symobl - the first argument 

	SELECT to_tsvector('german', 'Buch Smartphone') @@ 'buch' -> Returns True
<br/>

	SELECT to_tsvector('german', 'Buch Smartphone') @@ 'BUCH' -> Returns False
<br/>

It's important to apply the same processing to the data we query with `to_tsquery` & so we can avoid such issues.  

	SELECT to_tsvector('german', 'Buch Smartphone') @@ to_tsquery('german', 'BUCH') -> Returns True
<br/>

Instead of direct values, we can also pass a column as second argument - e.g. get all rows where 'char_col_1' contains 'Romeo'.  

	SELECT * FROM data
		to_tsvector('english', char_col_1) @@ to_tsquery('english', 'Romeo')
<br/>

This query is quite slow, as all values in 'char_col_1' have to be processed... to speed it up, we can create an index for it:  

	SELECT * FROM data
		to_tsvector('english', char_col_1) @@ to_tsquery('english', 'Romeo')
		CREATE INDEX index_col_name ON data
			USING GIN(to_tsvector('english', char_col_1))
<br/>

We can also pass multiple words into `to_tsquery`:  

	@@ to_tsquery('egnlish', 'Romeo & Julia') # -> Texts that contain 'Romeo' & 'Julia'
<br/>

	@@ to_tsquery('egnlish', 'Romeo | Julia') # -> Texts that contain either 'Romeo', 'Julia' or both
<br/>

	@@ to_tsquery('egnlish', '(Romeo | Julia) & Gutenberg') # -> Texts that contain either 'Romeo', 'Julia' or both AND 'Gutenberg'  
<br/>	

### Ranking search results
Find the book of shakespeare that contains the word 'love' the most with `ts_rank`:  

	SELECT *, ts_rank(to_tsvector('english', book_texts), plain_tsquery('enlgish', 'love')) AS score
	FROM shakespeare
	WHERE to_tsvector('english', book_texts)  @@ plain_tsquery('enlgish', 'love')
	ORDER BY score DESC
<br/> 

We can use `plain_tsquery` multiple times *(as 'search_query')* to only show us the relevant text-passages with `ts_headline`:  

	SELECT *, 
		ts_rank(to_tsvector('english', book_texts), search_query) AS score, 
		ts_headline('english', book_texts, search_query) AS headline, 
	FROM shakespeare, plain_tsquery('enlgish', 'love') AS search_query
	WHERE to_tsvector('english', book_texts, search_query)
	ORDER BY score DESC
<br/>

### Saving ts_vector
`ts_rank(...)` is slow and is exectued once per search hit, to speed it up *(& search in general)*, we can add `ts_vector(...)` permanently to a DF:

	UPDATE shakespeare SET ts_vec = to_tsvector('english', book_texts)
<br/>

This takes quite a while & has to be upated, when the values in 'book_texts' change! Queries are sped up:  

	SELECT * FROM shakespeare
		WHERE ts_vec @@ plainto_tsquery('english', 'Romeo')
<br/>

# (19) Execute functions automatically
## Trigger
Automatically run operations, after/ before a UPDATE/ DELETE/ INSERT/ TRUNCATE - e.g. adjust account balances during a transfer.  
The code to run automatically after certain operations, can be combined with 'stored procedures'!  

'Blog-Post' example: Everytime we UPDATE an title or content, we want to save the old entrance to 'blog_post_history'.  

	CREATE FUNCTION blog_post_update()
		RETURN trigger
		LANGUAGE 'plpgsql'
		VOLATILE AS $CODE$ BEGIN
			INSERT INTO blog_post_history (title) VALUE ('Trigger happend');
			RETURN NEW;
		END $CODE$
<br/>

Create the actual trigger now *(AFTER could also be BEFORE; UPDATE could also be INSERT / DELETE)*

	CREATE TRIGGER blog_post_update_trigger()
		AFTER UPDATE ON blog_post
			FOR EACH ROW EXECUTE blog_post_update()
<br/>

Update a title in 'blog_post' --> trigger runs automatically, as UPDATE is applied to 'blog_post' - write 'Trigger happend' to 'blog_post_update_trigger':  

	UPDATE blog_post SET title = "test" WHERE id = 1
<br/> 

## Meaninful values
Set meaningful values instead of 'Trigger happend' - w/ NEW.title *(new value after UPDATE was applied)* // OLD.title *(old value before UPDATE was applied)*   

	CREATE FUNCTION blog_post_update()
		RETURN trigger
		LANGUAGE 'plpgsql'
		VOLATILE AS $CODE$ BEGIN
			INSERT INTO blog_post_history (title) VALUES (NEW.title)
		END $CODE$
<br/>

## VIEW / MATERIALIED VIEW
**VIEW**:  
- Save a query as a single call - e.g. SELECT * FROM VIEW_CALL  
- Everytime we call the VIEW, we need to do the calculations again and hence it can be quite slow!  
<br/>

**MATERIALIED VIEW**: 
- Syntax as with 'VIEW' but with 'MATERIALIED VIEW' instead
- Saves the results of the query as an actual table, which makes it faster than VIEW
- Needs to be updated when the original data changes *(else it will show the old results ;-))*
<br/>
Example:

	CREATE VIEW customer.orders_view AS
		SELECT *,
			(SELECT SUM(amount) FROM orders WHERE orders.customer_id = customers.id) AS sum_all
		FROM customers
<br/>

Now we can call this 'VIEW': `SELECT * FROM customer.orders_view` - analog with 'MATERIALIED VIEW'.  

## 12. Exercise
customers' hat alle Kunden & für eine Anwendung brauchen wir für jeden Kunden den gesamtem Umsatz - füge dies als extra Spalte zu 'customers' hinzu (Umsatz berechnet sich über 'amount' in 'orders' --> Löse dieses Problem über verschiedene Wege

### (1) Über einen normal VIEW lösen

	CREATE VIEW customers_spent_1 AS 
	SELECT *,
	    (SELECT SUM(amount) FROM orders WHERE customers.id = orders.customer_id) AS Totally_Spent
	FROM customers
<br/>

	SELECT * FROM customers_spent_1
<br/>

### (2) Über einen materialized VIEW

	CREATE MATERIALIZED VIEW customers_spent AS 
	    SELECT *, 
	        (SELECT SUM(amount) FROM orders WHERE customers.id = orders.customer_id) AS Totally_Spent
	    FROM customers
<br/>

	SELECT * FROM customers_spent
<br/>

### (3) Über einen Trigger - neue Spalte erstellen & immer updaten, wenn sich was bei 'orders' ändert
#### 3-1 Add a column 'spent_all' to customers 

	ALTER TABLE customers
	    ADD COLUMN spent_all DECIMAL(10, 2)
    
#### 3-2 Fill the values to 'spent_all'

	UPDATE customers 
	    SET spent_all = (SELECT SUM(amount) FROM orders 
	                        WHERE orders.customer_id = customers.id)
    
#### 3-3 Delete triggers, so we can run the code again 

	DROP TRIGGER IF EXISTS orders_after_insert_trigger ON orders;
	DROP FUNCTION IF EXISTS orders_after_insert();

#### 3-4 Write a Trigger-Function for when something is inserted in orders

	CREATE FUNCTION orders_after_insert() # -> Must not take any arguments 
	    RETURNS TRIGGER
	    LANGUAGE 'plpgsql'
	    VOLATILE AS $CODE$ BEGIN
	        UPDATE customers SET spent_all = 
	            (SELECT SUM(amount) FROM orders 
	                WHERE orders.customer_id = customers.id)
	                WHERE customers.id = NEW.customer_id;
	        RETURN NEW;
	    END $CODE$;

#### 3-5 Write the trigger itself

	CREATE TRIGGER orders_after_insert_trigger
	    AFTER INSERT ON orders
	    FOR EACH ROW EXECUTE PROCEDURE orders_after_insert();

#### 3-6 Check the Trigger-Function

	SELECT * FROM customers WHERE ID = 1
<br/>

	SELECT * FROM orders WHERE customer_id = 1
<br/>

	INSERT INTO orders (timestamp, amount, customer_id) 
    	VALUES (CURRENT_TIMESTAMP, 100, 1)
<br/>

	SELECT * FROM customers WHERE ID = 1


#### 3-7 Delete triggers, so we can run the code again

	DROP TRIGGER IF EXISTS orders_after_delete_trigger ON orders
<br/>

	DROP FUNCTION IF EXISTS orders_after_delete()


#### 3-8 Write a Trigger-Function for when something is deleted in orders

	CREATE FUNCTION orders_after_delete() 
	    RETURNS TRIGGER
	    LANGUAGE 'plpgsql'
	    VOLATILE AS $CODE$ BEGIN
	        UPDATE customers SET spent_all = 
	            (SELECT SUM(amount) FROM orders 
	                WHERE orders.customer_id = customers.id)
	                WHERE customers.id = OLD.customer_id;
	        RETURN NEW;
	    END $CODE$;
  
#### 3-9 Write the trigger itself

	CREATE TRIGGER orders_after_delete_trigger
	    AFTER DELETE ON orders
	    FOR EACH ROW EXECUTE PROCEDURE orders_after_delete()
 
#### 3-10 Check the Trigger-Function 

	SELECT * FROM customers WHERE ID = 1
<br/>

	SELECT * FROM orders WHERE customer_id = 1
<br/>

	DELETE FROM orders WHERE id = 1053
<br/>

	SELECT * FROM customers WHERE ID = 1
<br/>

	SELECT * FROM orders WHERE customer_id = 1


#### 3-11 Delete triggers, so we can run the code again

	DROP TRIGGER IF EXISTS orders_after_update_trigger ON orders
<br/>

	DROP FUNCTION IF EXISTS orders_after_update();

#### 3-12 Write a Trigger-Function for when something is updated in orders
Can be tricky, as there the 'id' in customers could be changed - ensure to cover this scenario with ` WHERE customers.id = NEW.customer_id OR customers.id = OLD.customer_id;`
<br/>

	CREATE FUNCTION orders_after_update() 
	    RETURNS TRIGGER
	    LANGUAGE 'plpgsql'
	    VOLATILE AS $CODE$ BEGIN
	        UPDATE customers SET spent_all = 
	            (SELECT SUM(amount) FROM orders 
	                WHERE orders.customer_id = customers.id)
	                WHERE customers.id = NEW.customer_id OR
	                      customers.id = OLD.customer_id;
	        RETURN NEW;
	    END $CODE$;

#### 3-13 Write the trigger itself 

	CREATE TRIGGER orders_after_update_trigger
	    AFTER UPDATE ON orders
	    FOR EACH ROW EXECUTE PROCEDURE orders_after_update()

#### 3-14 Check the Trigger-Function 
	SELECT * FROM customers WHERE ID = 1
<br/>

	SELECT * FROM orders WHERE customer_id = 1
<br/>

	UPDATE orders SET amount = 100 WHERE customer_id = 1 
<br/>

	SELECT * FROM orders WHERE customer_id = 1 
<br/>

	SELECT * FROM customers WHERE ID = 1
<br/>

	SELECT * FROM customers WHERE ID in (1, 2)
<br/>

	UPDATE orders SET customer_id = 2 WHERE customer_id = 1
<br/>

	SELECT * FROM orders WHERE customer_id in (1,2)
<br/>

	SELECT * FROM customers WHERE ID in (1, 2) 

# (20) Constraints
We can use 'Constraints' to validate values - e.g. 'title' must contain at least three letter.  
'Constraints' can be part of a 'databank' *(complicated)* // 'application logic' *(better suited)*.  

Example: Ensure that 'title' contains at least 3 characters.  

	ALTER databank
		ADD constraint title_length_const
		CHECK (LENGTH(title) > 2);
<br/>

The following UPDATE leads to an error now, as we want to add a title with < 3 characters & violate the constraint

	UPDATE databank SET title 'L' WHERE id = 1  
<br/>