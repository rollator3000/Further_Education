-- Get the current date (can also substract, add, ...)
SELECT GETDATE()
SELECT GETDATE() - 2

-- Extract parts of the dates
SELECT DATEPART(yyyy, GETDATE()) AS YEARNUMBER
SELECT DATEPART(mm, GETDATE()) AS MONTHNUMBER
SELECT DATEPART(dd, GETDATE()) AS DAYNUMBER

-- Add dates
SELECT DATEADD(day, 4, GETDATE())
SELECT DATEADD(month, 4, GETDATE())
SELECT DATEADD(year, 4, GETDATE())

-- Differences between dates
SELECT DATEDIFF(day, GETDATE(), DATEADD(month, 4, GETDATE()))
SELECT DATEDIFF(month, GETDATE(), DATEADD(month, 4, GETDATE()))
SELECT DATEDIFF(year, GETDATE(), DATEADD(month, 123, GETDATE()))

-- Sample Data
SELECT TOP 10 * FROM [Production].[WorkOrder]

-- Add the difference of Start & EndDate
SELECT WorkOrderID, ProductID, StartDate, EndDate, DATEDIFF(day, StartDate, EndDate)
FROM [Production].[WorkOrder]

