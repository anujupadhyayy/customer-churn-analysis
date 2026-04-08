USE churn_db;

-- Q1: Overall churn rate
SELECT
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn;

-- Q2: Churn rate by geography
SELECT
    geography,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY geography
ORDER BY churn_rate_pct DESC;

-- Q3: Churn rate by age group
SELECT
    CASE
        WHEN age < 30 THEN '<30'
        WHEN age BETWEEN 30 AND 45 THEN '30-45'
        WHEN age BETWEEN 46 AND 60 THEN '45-60'
        ELSE '60+'
    END AS age_group,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY age_group
ORDER BY churn_rate_pct DESC;

-- Q4: Churn rate by number of products
SELECT
    numofproducts,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY numofproducts
ORDER BY numofproducts;

-- Q5: Active vs inactive member churn
SELECT
    CASE WHEN isactivemember = 1 THEN 'Active' ELSE 'Inactive' END AS member_status,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY isactivemember;

-- Q6: Complaint impact on churn
SELECT
    CASE WHEN complain = 1 THEN 'Complained' ELSE 'No Complaint' END AS complaint_status,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY complain;

-- Q7: Avg balance and credit score — churned vs retained
SELECT
    CASE WHEN exited = 1 THEN 'Churned' ELSE 'Retained' END AS status,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(AVG(creditscore), 1) AS avg_credit_score
FROM customer_churn
GROUP BY exited;

-- Q8: Churn by satisfaction score
SELECT
    satisfaction_score,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY satisfaction_score
ORDER BY satisfaction_score;

-- Q9: Churn by card type
SELECT
    card_type,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY card_type
ORDER BY churn_rate_pct DESC;

-- Q10: High-value vs standard customers churn rate (top 25% balance)
SELECT
    CASE
        WHEN balance >= (
            SELECT balance FROM customer_churn
            ORDER BY balance DESC
            LIMIT 1 OFFSET 2499
        ) THEN 'High Value'
        ELSE 'Standard'
    END AS segment,
    COUNT(*) AS total,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM customer_churn
GROUP BY segment;