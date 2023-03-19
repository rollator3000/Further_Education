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
#### (1) Wie viele Einträge gibt es insgesamt in der Tabelle baby_names?

	SELECT COUNT(*) FROM baby_names

#### (2) Wie viele männliche Personen (gender = M) wurden im Jahr 2010 geboren, die „Alex“ heißen?

	SELECT COUNT(*) FROM baby_names 
	WHERE ("name" = 'Alex' AND "gender" = 'M' AND "year" = 2010)

#### (3) Wie viele unterschiedliche Namen gibt es in unserer Tabelle, wenn das Geschlecht egal ist *(d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählt als der gleiche Name)*

	SELECT COUNT(DISTINCT("name")) FROM baby_names 

#### (4) Wie viele unterschiedliche Namen gibt es in unserer Tabelle, wenn das Geschlecht nicht egal ist *(d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählen als 2 unterschiedliche Namen)*
	
	SELECT COUNT(DISTINCT("name", "gender")) FROM baby_names 

#### (5) Welcher Baby-Name wurde in einem bestimmten Jahr exakt 19250 mal vergeben?

	SELECT * FROM baby_names 
	WHERE count = 19250

#### (6) Gibt es das Geschlecht „divers“ in unserer Tabelle? 

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
#### (1) Wie viele unterschiedliche Vornamen gibt es, die mit „Alex“ anfangen, „Alex“ eingeschlossen? Hierbei spielt das Geschlecht keine Rolle.

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE 'Alex%' 

#### (2) Wie viele unterschiedliche Vornamen gibt es, in denen im Vornamen ein „m“ enthalten ist? Das „m“ darf auch an erster Stelle stehen. 

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE '%m%' OR "name" LIKE 'M%' 	

#### (3) Wie viele Zeilen gibt es in der Tabelle, bei denen das Jahr im 20. Jahrhundert (1900 bis einschließlich 1999) ist?  
-> einmal mit BETWEEN einmal ohne

	SELECT COUNT("year") FROM baby_names WHERE "year" BETWEEN 1900 AND 1999     

	SELECT COUNT("year") FROM baby_names WHERE "year" >= 1900 AND "year" <= 1999 

#### (4) Wie viele Zeilen gibt es in der Tabelle, bei denen das Jahr im 20. Jahrhundert (1900 bis einschließlich 1999) ist, und durch 10 Teilbar ist?  
-> Löse diese Aufgabe mit vielen ORs  
-> Löse diese Aufgabe mit einem WHERE IN()  
-> Löse die Aufgabe mit einem LIKE  
-> Löse diese Aufgabe mit einem Modulo

	SELECT COUNT("year") FROM baby_names WHERE 
		"year" = 1900 OR "year" = 1910 OR "year" = 1920 OR "year" = 1930 OR
	    "year" = 1940 OR "year" = 1950 OR "year" = 1960 OR "year" = 1970 OR
	    "year" = 1980 OR "year" = 1990           							   # -> 15307

	SELECT COUNT("year") FROM baby_names WHERE 
		"year" IN (1990, 1980, 1970, 1960, 1950, 1940, 1930, 1920, 1910, 1900) # -> 15307

	SELECT COUNT("year") FROM baby_names WHERE year::varchar LIKE '19_0'       # -> 15307

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

Can also be combined + take care that they return the same amount of rows.  
Use 'AS' to name columns.

	SELECT CONCAT(UPPER(name), ' - ', LOWER(lastname)) AS last_name FROM TABLE

	SELECT AVG(MIN(age), MAX(age)) AS LOL FROM TABLE

## 3. Exercise - 'baby_names'




