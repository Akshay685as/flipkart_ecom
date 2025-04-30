# 📊 Flipkart SQL Business Intelligence Dashboard

A full-stack data analytics project using Flipkart's product dataset. This project includes data cleaning in Python, SQL data modeling, insight extraction, and Python-based dashboard visualizations.

---

## 🧩 Project Overview

- Cleaned raw Flipkart e-commerce data using Python
- Normalized into SQL tables (`products`, `pricing`, `ratings`)
- Ran SQL queries to extract business insights
- Created dashboards using Seaborn and Matplotlib

---

## 🛠️ Tech Stack

- **Python (Pandas, Seaborn, Matplotlib)** – Data cleaning + visualizations
- **MySQL 9.1** – Database setup + query engine
- **Workbench** – For SQL scripting and import
- **GitHub** – Project portfolio + documentation

---

## 📁 Folder Structure


---

## 🧹 Data Cleaning

Used `scripts/ecom.py` to:
- Extract main product category from nested tree
- Clean missing brand values
- Normalize rating column (convert "No rating available" → `NULL`)
- Output 3 normalized files for SQL:
  - `products.csv`
  - `pricing.csv`
  - `ratings.csv`

> 📎 Raw dataset used: `flipkart_com-ecommerce_sample.csv` (from Kaggle)

---

## 🗃️ Database Tables

| Table     | Description                      |
|-----------|----------------------------------|
| `products`  | Product ID, name, brand, category |
| `pricing`   | Retail and discounted prices     |
| `ratings`   | Customer rating (cleaned float)  |

---

## 📈 Business KPIs

- 🏷️ Top 10 Brands by Product Count  
- 💸 Top 10 Brands by Average Discount %  
- ⭐ Top Categories by Average Product Rating  
- 🔥 Most Discounted Products

---

## 📊 Visualizations

Created in Python using Seaborn:
- 3 stacked bar charts in one dashboard window:
  1. Brand-wise product count
  2. Brand-wise avg discount %
  3. Category-wise avg rating

📸 Screenshot:
![Dashboard Preview](screenshots/charts_preview.png)

---

## 🚀 How to Run the Project

1. Run `scripts/ecom.py` to clean and export data
2. Import cleaned CSVs into MySQL using `sql/flipkart_full.sql`
3. Run `visualizations/flipkart_dashboard.py` to generate insights
4. (Optional) Upload to Power BI or convert to Streamlit dashboard

---

## 👤 Author

**Akshay Soni**  
📍 Udaipur, India | MBA (IIM Amritsar)  
📧 [akshaysoni685.as@gmail.com](mailto:akshaysoni685.as@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/akshay-soni-1a047)

---

## 🌟
