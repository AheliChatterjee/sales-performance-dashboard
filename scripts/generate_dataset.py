import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and random seed for consistency
fake = Faker()
random.seed(42)

# Define constants
NUM_ROWS = 5000  # You can change this to 500 for quick testing
CATEGORIES = ['Electronics', 'Furniture', 'Office Supplies', 'Clothing']
REGIONS = ['North', 'South', 'East', 'West']
CUSTOMER_SEGMENTS = ['Consumer', 'Corporate', 'Home Office']

# Helper function to generate random sales data
def generate_sales_data(n=NUM_ROWS):
    data = []
    for _ in range(n):
        order_date = fake.date_between(start_date='-2y', end_date='today')
        category = random.choice(CATEGORIES)
        product = fake.word().capitalize() + " " + category[:-1]  # e.g., 'Smart Electronic'
        quantity = random.randint(1, 10)
        sales = round(random.uniform(50, 1000) * quantity, 2)
        discount = round(random.uniform(0, 0.3), 2)
        profit = round(sales * (0.1 + random.uniform(-0.05, 0.1)), 2)  # Variable profit margin
        region = random.choice(REGIONS)
        segment = random.choice(CUSTOMER_SEGMENTS)
        data.append([
            fake.uuid4(),
            order_date,
            product,
            category,
            quantity,
            sales,
            discount,
            profit,
            region,
            segment
        ])
    return pd.DataFrame(data, columns=[
        'Order_ID', 'Date', 'Product', 'Category', 'Quantity',
        'Sales', 'Discount', 'Profit', 'Region', 'Customer_Segment'
    ])

# Generate dataset
df = generate_sales_data()

# Save to CSV
output_path = '../data/raw_sales_data.csv'
df.to_csv(output_path, index=False)

print(f"✅ Dataset generated successfully! Saved to: {output_path}")
print(df.head())
