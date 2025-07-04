SELECT ProductID, ProductName, Price, 
       CASE WHEN Price<50 THEN 'Low'
       WHEN Price between 50 AND 250 THEN 'Medium'
       ELSE 'High'
       END AS PriceCategory
       FROM business.`dbo.products`;