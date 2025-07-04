
SELECT c.CustomerID, c.CustomerName, c.Email, c.Gender, c.Age, g.Country, g.City 
FROM business.`dbo.customers` as c  
LEFT JOIN business.`dbo.geography` g
ON 
    c.GeographyID = g.GeographyID;  