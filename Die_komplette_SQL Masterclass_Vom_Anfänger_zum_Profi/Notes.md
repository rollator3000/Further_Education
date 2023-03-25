# COMPLETE SQL-MASTERCLASS

Notes to the Online-Course 'Die komplette SQL Masterclass: Vom Anfänger zum Profi' - https://www.udemy.com/course/sql-komplett/

# (1) Introduction
This course covers the two databank-systems 'MySQL' & 'PostgreSQL' - both are commonly used frameworks with only small differences.  
- MySQL:  
	- Less Features than PostgreSQL   
	- often part of WebHosters  

- PostgreSQL:  
	- more features than MySQL   
	- ideal for complex queries  

There is SQL-Tool available online: https://downloads.codingcoursestv.eu/043%20-%20sql/online-sql/dist/index.html

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

	SELECT * FROM TABLE
	WHERE age BETWEEN 18 AND 25

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

# (4) MANAGE DATA
## INSERT INTO
Put new data permanently into existing data.  

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

	UPDATE categories SET title = REPLACE(title, '-', '--')

## DELETE 
Delete a whole dateset/ single rows e.g. with the value '5' in the column 'id'

	DELETE FROM TABLE

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
Create a new dataset


