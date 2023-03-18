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

**Example:**  
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

**Example:**  
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

**Example:**  
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
Wie viele Einträge gibt es insgesamt in der Tabelle baby_names?

	SELECT COUNT(*) FROM baby_names

Wie viele männliche Personen (gender = M) wurden im Jahr 2010 geboren, die „Alex“ heißen?

	SELECT COUNT(*) FROM baby_names 
	WHERE ("name" = 'Alex' AND "gender" = 'M' AND "year" = 2010)

Wie viele unterschiedliche Namen gibt es in unserer Tabelle, wenn das Geschlecht egal ist *(d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählt als der gleiche Name)*

	SELECT COUNT(DISTINCT("name")) FROM baby_names 

Wie viele unterschiedliche Namen gibt es in unserer Tabelle, wenn das Geschlecht nicht egal ist *(d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählen als 2 unterschiedliche Namen)*
	
	SELECT COUNT(DISTINCT("name", "gender")) FROM baby_names 

Welcher Baby-Name wurde in einem bestimmten Jahr exakt 19250 mal vergeben?
	
	SELECT * FROM baby_names 
	WHERE count = 19250

Gibt es das Geschlecht „divers“ in unserer Tabelle? 

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