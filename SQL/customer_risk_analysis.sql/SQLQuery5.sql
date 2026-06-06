SELECT
    Income_Category,
    COUNT(*) AS Customers
FROM Customer_Risk_Analytics
GROUP BY Income_Category
ORDER BY Customers DESC;