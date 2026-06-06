-- Attrition Summary

SELECT
    Attrition_Flag,
    COUNT(*) AS Total_Customers
FROM Customer_Risk_Analytics
GROUP BY Attrition_Flag;