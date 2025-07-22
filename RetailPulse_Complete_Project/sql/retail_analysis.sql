
-- Top-selling product categories
SELECT ProductCategory, SUM(Price * Quantity) AS Revenue
FROM transactions
GROUP BY ProductCategory
ORDER BY Revenue DESC;

-- Churn-risk customers (no purchase in last 90 days)
SELECT CustomerID, MAX(TransactionDate) AS LastPurchase
FROM transactions
GROUP BY CustomerID
HAVING LastPurchase < CURDATE() - INTERVAL 90 DAY;

-- Average spend by gender
SELECT Gender, AVG(Price * Quantity) AS AvgSpend
FROM transactions
GROUP BY Gender;

-- Total revenue from all transactions
SELECT SUM(Price * Quantity) AS TotalRevenue FROM transactions;

--sales by location
SELECT Location, SUM(Price * Quantity) AS Revenue
FROM transactions
GROUP BY Location
ORDER BY Revenue DESC;

--age group analysis
SELECT
  CASE
    WHEN Age < 20 THEN 'Teen'
    WHEN Age BETWEEN 20 AND 30 THEN '20s'
    WHEN Age BETWEEN 31 AND 40 THEN '30s'
    WHEN Age BETWEEN 41 AND 50 THEN '40s'
    ELSE '50+'
  END AS AgeGroup,
  COUNT(*) AS Transactions
FROM transactions
GROUP BY AgeGroup;
-- gender distribution
SELECT Gender, COUNT(DISTINCT CustomerID) AS Count
FROM transactions
GROUP BY Gender;
