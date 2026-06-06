SELECT
    Income_Category,
    AVG(Credit_Limit) AS Avg_Credit_Limit
FROM Customer_Risk_Analytics
GROUP BY Income_Category
ORDER BY Avg_Credit_Limit DESC;