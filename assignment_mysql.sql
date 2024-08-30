use ecommerce_dbs
show tables;
select * from ecommerce_data

/* check1 */

SELECT 
     COUNT(*) As null_count
	FROM
       ecommerce_data
WHERE 
    TransactionID IS NULL 
    OR ProductID IS NULL 
    OR ProductCategory IS NULL 
    OR ProductSubcategory IS NULL 
    OR ProductPrice IS NULL 
    OR QuantitySold IS NULL 
    OR TransactionDate IS NULL 
    OR CustomerID IS NULL 
    OR CustomerLocation IS NULL 
    OR PaymentMethod IS NULL;

/* check2 */
SELECT 
    COUNT(*) AS duplicate_count
FROM 
  ecommerce_data
GROUP BY 
    TransactionID, ProductID, ProductCategory, ProductSubcategory, ProductPrice, QuantitySold, TransactionDate, CustomerID, CustomerLocation, PaymentMethod
HAVING 
    COUNT(*) > 1;

/* check3 */
SELECT 
    COUNT(*) AS invalid_date_count
FROM 
    ecommerce_data
WHERE 
    TransactionDate < '1900-01-01' 
    OR TransactionDate > CURDATE();
    
/* check4 */
    SELECT 
    COUNT(*) AS invalid_price_count
FROM 
    ecommerce_data
WHERE 
    ProductPrice < 0;
    
/* check5 */
SELECT 
    COUNT(*) AS invalid_quantity_count
FROM 
    ecommerce_data
WHERE 
    QuantitySold < 0;

/* check6 */
SELECT 
    Customerid, 
    SUM(ProductPrice * QuantitySold) AS total_sales
FROM 
    ecommerce_data
GROUP BY 
    Customerid
ORDER BY 
    total_sales DESC
LIMIT 10;

/* check7 */
SELECT 
    Productid, 
    SUM(ProductPrice * QuantitySold) AS total_sales
FROM 
    ecommerce_data
GROUP BY 
    Productid
ORDER BY 
    total_sales DESC
LIMIT 10;