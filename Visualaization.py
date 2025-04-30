import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9828043990",
    database="ecom_flipkart"
)

# 1. Top Brands by Product Count
brands_df = pd.read_sql("""
    SELECT brand, COUNT(*) AS product_count
    FROM products
    GROUP BY brand
    ORDER BY product_count DESC
    LIMIT 10
""", conn)

# 2. Avg Discount % by Brand
discount_df = pd.read_sql("""
    SELECT p.brand,
           ROUND(AVG(1 - pr.discounted_price / pr.retail_price) * 100, 2) AS avg_discount_pct
    FROM products p
    JOIN pricing pr ON p.product_id = pr.product_id
    WHERE pr.retail_price > 0
    GROUP BY p.brand
    ORDER BY avg_discount_pct DESC
    LIMIT 10
""", conn)

# 3. Avg Rating by Category
rating_df = pd.read_sql("""
    SELECT p.category,
           ROUND(AVG(r.product_ratings), 2) AS avg_rating
    FROM products p
    JOIN ratings r ON p.product_id = r.product_id
    GROUP BY p.category
    ORDER BY avg_rating DESC
    LIMIT 10
""", conn)

conn.close()

# Set Seaborn style
sns.set(style="whitegrid")

# Plot 1: Top Brands by Product Count
plt.figure(figsize=(10,5))
sns.barplot(x='brand', y='product_count', data=brands_df, palette='Blues_d')
plt.title("Top 10 Brands by Product Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Average Discount % by Brand
plt.figure(figsize=(10,5))
sns.barplot(x='brand', y='avg_discount_pct', data=discount_df, palette='Greens_d')
plt.title("Top 10 Brands by Avg Discount %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Average Rating by Category
plt.figure(figsize=(10,5))
sns.barplot(x='category', y='avg_rating', data=rating_df, palette='Oranges_d')
plt.title("Top 10 Categories by Avg Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)

