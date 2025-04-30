import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Akshay Soni/Downloads/archive (3)/flipkart_com-ecommerce_sample.csv")

# Extract category (first-level)
df['category'] = df['product_category_tree'].apply(lambda x: x.split(">>")[0].replace('["','').strip() if isinstance(x, str) else None)

# Clean ratings
def clean_rating(rating):
    try:
        if "no rating" in rating.lower():
            return None
        return float(rating)
    except:
        return None

df['product_rating_clean'] = df['product_rating'].apply(clean_rating)

# Prepare Products table
products = df[['pid', 'product_name', 'brand', 'category']].dropna()
products.columns = ['product_id', 'product_name', 'brand', 'category']
products.to_csv("products.csv", index=False)

# Prepare Pricing table
pricing = df[['pid', 'retail_price', 'discounted_price']].dropna()
pricing.columns = ['product_id', 'retail_price', 'discounted_price']
pricing.to_csv("pricing.csv", index=False)

# Prepare Ratings table
ratings = df[['pid', 'product_rating_clean']].dropna()
ratings.columns = ['product_id', 'product_rating']
ratings.to_csv("ratings.csv", index=False)
