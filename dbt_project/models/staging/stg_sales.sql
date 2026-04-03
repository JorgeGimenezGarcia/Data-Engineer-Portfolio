-- Select and clean raw data before transformation
SELECT
    id AS sale_id,
    product_name,
    price,
    -- Type casting is a key staging step
    CAST(sale_date AS DATE) AS sale_date
FROM 
    {{ source('DE_PORTFOLIO_DB', 'RAW_SALES_DATA') }}