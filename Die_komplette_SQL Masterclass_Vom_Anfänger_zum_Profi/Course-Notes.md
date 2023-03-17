# COMPLETE SQL-MASTERCLASS

Notes to the Online-Course 'Die komplette SQL Masterclass: Vom Anfänger zum Profi' - https://www.udemy.com/course/sql-komplett/learn/lecture/17350952?start=0#overview

## (1) Introduction
This course covers the two databank-systems 'MySQL' & 'PostgreSQL' - both are commonly used frameworks that only have smaller differences.   

	- MySQL:
		- Less Features than PostgreSQL 
		- often part of WebHosters

	- PostgreSQL:
		- more features than MySQL 
		- ideal for complex queries


There is SQL-Tool available online: https://downloads.codingcoursestv.eu/043%20-%20sql/online-sql/dist/index.html

Exemplary Query:

		SELECT id, creator, title, downloads    # -> Columns we need
		FROM books 								# -> DataSource with corresponding columns
		WHERE creator = 'Niemann, August'       # -> Condition applied to the selected data

## (2) Installation of PostgreSQL
As MySQL doesn't work on MacOS, I've only set-up PostgreSQL. <br/> 

	- Download of a databank *(s. 'data/')*
	- Configuration of PostgreSQL
		- PGAdmin4 
		- Servers
		- Creation of new data-base

## (3) Databank Queries
#### SELECT
Used to select columns from a data-base. <br/> 

	- Optimally, put colnames in " " *(' ' doesn't work)*
	- Case-Sensitive

**Example**
Select all columns from data-base// only columns A, B from TABLE 

	SELECT * FROM TABLE			
	SELECT "A", "B" FROM TABLE		# -> 

#### WHERE 
Select rows that full-fill a condition. <br/> 

**Possible Conditions**  

	- Mathematically: >, <, >=, <=
	- Equal/ Unequal: =, <>
	- AND, OR
		- in brackets: ... WHERE ("name" = 'Alex' AND "gender" = 'M' AND "year" = 2010)
	- NOT:
		- in brackets: ... WHERE NOT("age" > 20) 

**Example**
Get all columns for the rows, where title = 'Hr. Dr'// 'Fr. Dr' & where AGE > 30

	SELECT * 
	FROM TABLE
	WHERE (TITLE = 'Fr. Dr.' OR TITLE = 'Hr. Dr') AND	
		  AGE > 30  							

#### COUNT & DISTINCT





