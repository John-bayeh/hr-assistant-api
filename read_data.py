import pandas as pd
df=pd.read_csv("employee.csv")
print(df)
print("\nTotal salary budget:", df["salary"].sum())
print("\navearge salary ",df["salary"].mean())
