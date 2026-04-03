-- Final Business Mart for Analytics teams
SELECT
    sale_date,
    COUNT(sale_id) AS total_sales_count,
    SUM(price) AS total_revenue
FROM 
    {{ ref('stg_sales') }}
GROUP BY 1
ORDER BY 1 DESC