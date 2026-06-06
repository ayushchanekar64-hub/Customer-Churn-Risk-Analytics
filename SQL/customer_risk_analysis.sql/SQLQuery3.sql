-- Top 10 Customers by Transaction Amount

SELECT TOP 10
    CLIENTNUM,
    Total_Trans_Amt
FROM Customer_Risk_Analytics
ORDER BY Total_Trans_Amt DESC;