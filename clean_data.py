import pandas as pd
import numpy as np
df=pd.read_csv("hr_data.csv")
print("before cleaning")
print(df)
print("\nMissing values:\n",df.isnull().sum())
# Step 1 — Fix department casing
# Replace this
df["department"] = df["department"].str.title()

# With this
df["department"] = df["department"].str.upper()
print("\nDepartments fixed:", df["department"].unique())

# Step 2 — Fix salary (convert text to NaN)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Step 3 — Fix performance_score (convert invalid to NaN)
df["performance_score"] = pd.to_numeric(df["performance_score"], errors="coerce")

# Step 4 — Fill missing salaries with department average
df["salary"] = df.groupby("department")["salary"].transform(
    lambda x: x.fillna(x.mean())
)

# Step 5 — Fill missing performance with overall average
df["performance_score"] = df["performance_score"].fillna(df["performance_score"].mean())

# Step 6 — Drop rows with no name
df = df.dropna(subset=["name"])

print("\nAFTER CLEANING:")
print(df)
df.to_csv("hr_data_cleaned.csv", index=False)
print("\nCleaned data saved to hr_data_cleaned.csv")

