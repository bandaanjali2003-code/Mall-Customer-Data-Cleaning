# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 18:45:16 2025

@author: banda
"""

import pandas as pd

# Step 1: Load dataset
df = pd.read_csv(r"C:\Users\banda\OneDrive\Desktop\Mall segmentation project\Mall_Customers.csv")

print(df.head())

# Step 2: Check for missing values
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Step 3: Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Step 4: Standardize text values
df['Gender'] = df['Gender'].str.strip().str.capitalize()

# Step 5: Rename columns (make them lowercase and underscore separated)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Step 6: Verify and fix data types (Age, Income, etc.)
df['age'] = df['age'].astype(int)
df['annual_income_k$'] = df['annual_income_k$'].astype(int)
df['spending_score_1-100'] = df['spending_score_1-100'].astype(int)

# Step 7: Save cleaned dataset
df.to_csv("Cleaned_Mall_Customers.csv", index=False)

print("\n Cleaned dataset saved as 'Cleaned_Mall_Customers.csv'")
print("\n Dataset Info After Cleaning:")
print(df.info())
print("\nFirst 5 rows after cleaning:\n", df.head())
