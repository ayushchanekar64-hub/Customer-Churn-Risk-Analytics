SELECT
    Risk_Level,
    COUNT(*) AS Customers
FROM Customer_Risk_Analytics
GROUP BY Risk_Level;