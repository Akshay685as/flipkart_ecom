CREATE database ecom_flipkart;
use ecom_flipkart;
create table products(
product_id varchar(50) primary key,
product_name text,
brand varchar(50),
category varchar(100)
);


create table pricing(
product_id varchar(50),
  retail_price DECIMAL(10,2),
  discounted_price DECIMAL(10,2),
 foreign key (product_id) references products(product_id) 
);

create table ratings(
product_id varchar(50),
  product_ratings DECIMAL(3,2),
foreign key (product_id) references products(product_id) 
);

load data local infile "C:/Users/Akshay Soni/Python Data Analysis/E commerce/products.csv"
into table products
fields terminated by ','
enclosed by '"'
lines terminated by '/n'
ignore 1 rows;
SHOW VARIABLES LIKE 'local_infile';



