use ecom_flipkart;
LOAD DATA LOCAL INFILE 'C:/Users/Akshay Soni/Python Data Analysis/E commerce/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Akshay Soni/Python Data Analysis/E commerce/pricing.csv'
INTO TABLE pricing
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Akshay Soni/Python Data Analysis/E commerce/ratings.csv'
INTO TABLE ratings
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


select * from pricing;
select * from ratings;
select * from products;

select count(*) from pricing;
select count(*) from ratings;
select count(*) from products;

select brand, count(*) AS total_products from products
group by brand
order by total_products desc
limit 10;

SELECT p.brand,
ROUND(AVG(1 - pr.discounted_price / pr.retail_price) * 100, 2) AS avg_discount_pct
FROM products p
JOIN pricing pr ON p.product_id = pr.product_id
WHERE pr.retail_price > 0
GROUP BY p.brand
ORDER BY avg_discount_pct DESC
LIMIT 10;

SELECT p.category,
       ROUND(AVG(r.product_ratings), 2) AS avg_rating,
       COUNT(*) AS rated_products
FROM products p
JOIN ratings r ON p.product_id = r.product_id
GROUP BY p.category
ORDER BY avg_rating DESC
LIMIT 10;

SELECT p.product_name, p.brand, pr.retail_price, pr.discounted_price,
       ROUND((1 - pr.discounted_price / pr.retail_price) * 100, 2) AS discount_pct
FROM products p
JOIN pricing pr ON p.product_id = pr.product_id
WHERE pr.retail_price > 0
ORDER BY discount_pct DESC
LIMIT 10;



DESCRIBE ratings;

