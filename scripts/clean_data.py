import pandas as pd
import numpy as np
import os

# File paths
RAW_PATH = '../data/raw_sales_data.csv'
CLEAN_PATH = '../data/cleaned_sales_data.csv'

# Load dataset
df = pd.read_csv(RAW_PATH)
print(f"✅ Raw dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# -------------------- Data Cleaning --------------------
# 1. Drop duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values (if any)
df.fillna({
    'Discount': 0,
    'Profit': df['Profit'].mean() if 'Profit' in df.columns else 0
}, inplace=True)

# 3. Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 4. Remove any invalid or future dates
df = df[df['Date'] <= pd.Timestamp.today()]

# 5. Add derived columns
df['Revenue'] = df['Sales'] - (df['Sales'] * df['Discount'])
df['Profit Margin (%)'] = round((df['Profit'] / df['Revenue']) * 100, 2)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()

# 6. Remove negative profits or impossible margins
df = df[df['Profit'] >= 0]
df = df[df['Profit Margin (%)'] <= 100]

# -------------------- Summary Insights --------------------
print("\n📊 Cleaned Data Summary:")
print(df.describe(include='all'))
print("\nTop 5 cleaned records:")
print(df.head())

# -------------------- Save Cleaned Data --------------------
os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
df.to_csv(CLEAN_PATH, index=False)
print(f"\n✅ Cleaned dataset saved successfully at: {CLEAN_PATH}")
