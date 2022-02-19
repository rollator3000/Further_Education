-- Create a new data-base with the name 'mytestdb'
-- -> new folder in 'Databases'
 create database mytestdb
 
 -- activate the database
 use mytestdb

 -- create a table with 1 numeric & 2 char columns
 create table mytesttable 
 (
 rollno int,
 firstname varchar(50),
 lastname varchar(50)
 )

 -- add data to the created table
  insert into mytesttable(rollno, firstname, lastname)
  values(1, 'Fred', 'Lud') 

  -- Inspect the data
  select rollno, firstname, lastname from mytesttable
