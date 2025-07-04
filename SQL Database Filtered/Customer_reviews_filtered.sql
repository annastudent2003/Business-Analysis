SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, 
REPLACE(ReviewText, '  ', ' ') AS ReviewText
FROM business.`dbo.customer_reviews`;