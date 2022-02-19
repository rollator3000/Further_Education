--Attach '.bak'-file via right-click 'Databases' -> 'Restore Database' -> 'Device' -> '...' -> add path to bak 
--Attach '.mdf'-file via right-click 'Databases' -> 'Attach' -> add path md
-- --> Add a new element to 'Databases'

-- Select the database
use [AdventureWorks2012]

-- Select all columns & rows from the 'HumanResources.Department'
SELECT * FROM [HumanResources].[Department]

-- Show all Department/ Group Names
SELECT NAME FROM [HumanResources].[Department]
SELECT GROUPNAME FROM [HumanResources].[Department]

-- Get unique/ disting values
SELECT DISTINCT NAME FROM [HumanResources].[Department]
SELECT DISTINCT GROUPNAME FROM [HumanResources].[Department]

-- GET NAMES that are Manufacturing
SELECT NAME, GROUPNAME FROM [HumanResources].[Department]
WHERE GROUPNAME LIKE 'Manufacturing'

-- All employees from Employee-Table
SELECT * FROM [HumanResources].[Employee]

-- List of all employees with OrgLevel = 2
SELECT * FROM [HumanResources].[Employee]
WHERE OrganizationLevel = 2

-- List of all employees with OrgLevel = 2 / 3
SELECT * FROM [HumanResources].[Employee]
WHERE OrganizationLevel in (2, 3)

-- LIKE is not case-sensitive
SELECT * FROM [HumanResources].[Employee]
WHERE JobTitle LIKE 'FACILITIES MANAGER'

-- All jobs that end with manager
SELECT * FROM [HumanResources].[Employee]
WHERE JobTitle LIKE '%MANAGER' 

-- All jobs that contain control
SELECT * FROM [HumanResources].[Employee]
WHERE JobTitle LIKE '%CONTROL%'

-- All employees born after 1. Jan 1990
 SELECT * FROM [HumanResources].[Employee]
 WHERE BirthDate > '1/1/1990'

 -- All employees born between 1.1.1970 + 1.1.1980
 SELECT * FROM [HumanResources].[Employee]
 WHERE BirthDate > '1/1/1970' AND  BirthDate < '1/1/1980' 