"""
Generate a complex sample dataset to test the Universal Data Analyzer.
Run this script once, then open Universal_Data_Analyzer.ipynb and set:
    FILE_PATH = "sample_company_data.csv"
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n = 500

# Categories
departments = ["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations", "Support", "R&D"]
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad"]
levels = ["Junior", "Mid", "Senior", "Lead", "Manager", "Director"]
ratings = ["A", "B", "C", "D", "E"]

# Generate random dates
start = datetime(2018, 1, 1)
dates = [start + timedelta(days=int(np.random.randint(0, 2500))) for _ in range(n)]

# Build the dataframe
df = pd.DataFrame({
    "Employee_ID": range(1001, 1001 + n),
    "Join_Date": [d.strftime("%Y-%m-%d") for d in dates],
    "Department": np.random.choice(departments, n),
    "City": np.random.choice(cities, n),
    "Level": np.random.choice(levels, n, p=[0.3, 0.25, 0.2, 0.12, 0.08, 0.05]),
    "Age": np.random.randint(22, 58, n),
    "Salary": np.round(np.random.normal(75000, 25000, n), 2),
    "Experience_Years": np.random.randint(0, 25, n),
    "Projects_Completed": np.random.randint(1, 40, n),
    "Performance_Rating": np.random.choice(ratings, n, p=[0.15, 0.30, 0.30, 0.15, 0.10]),
    "Satisfaction_Score": np.round(np.random.uniform(1.0, 10.0, n), 1),
    "Training_Hours": np.round(np.random.exponential(40, n), 1),
    "Monthly_Overtime": np.round(np.random.gamma(2, 5, n), 1),
    "Left_Company": np.random.choice([True, False], n, p=[0.2, 0.8])
})

# Inject missing values (5% in numeric, 3% in categorical)
for col in ["Salary", "Training_Hours", "Satisfaction_Score"]:
    mask = np.random.choice(n, size=int(n * 0.05), replace=False)
    df.loc[mask, col] = np.nan

for col in ["City", "Performance_Rating"]:
    mask = np.random.choice(n, size=int(n * 0.03), replace=False)
    df.loc[mask, col] = np.nan

# Add 10 duplicate rows to test duplicate removal
dupes = df.sample(10)
df = pd.concat([df, dupes], ignore_index=True)

# Save
df.to_csv("sample_company_data.csv", index=False)
print(f"Dataset created: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Total missing values: {df.isnull().sum().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"\nColumns: {list(df.columns)}")
print("\nDone! Now open Universal_Data_Analyzer.ipynb and set FILE_PATH = 'sample_company_data.csv'")
