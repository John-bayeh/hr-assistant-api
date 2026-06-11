import pandas as pd
import numpy as np

# Realistic Ethiopian company dataset
data = {
    "name": ["Yohannes", "Sara", "Mike", "Hana", "Abel", "Meron", "David", "Tigist"],
    "department": ["Engineering", "HR", "Engineering", "HR", "Sales", "Sales", "Engineering", "HR"],
    "salary": [25000, 18000, 30000, 16000, 20000, 22000, 28000, 17000],
    "years_experience": [3, 2, 5, 1, 4, 6, 4, 2],
    "performance_score": [8.5, 7.2, 9.1, 6.8, 7.5, 8.8, 8.0, 7.0]
}
pd.set_option("display.max_columns", None)
df = pd.DataFrame(data)
print(df)
# 1. Department with highest average salary
print("Avg salary by dept:\n", df.groupby("department")["salary"].mean())

# 2. Top performer
print("\nTop performer:\n", df[df["performance_score"] == df["performance_score"].max()])

# 3. Employees with more than 3 years experience
print("\nSenior employees:\n", df[df["years_experience"] > 3])

# 4. Correlation between experience and salary
print("\nExperience vs Salary correlation:", df["years_experience"].corr(df["salary"]))