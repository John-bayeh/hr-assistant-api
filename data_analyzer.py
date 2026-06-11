import pandas as pd

def get_company_summary() -> str:
    data = {
        "name": ["Yohannes", "Sara", "Mike", "Hana", "Abel", "Meron", "David", "Tigist"],
        "department": ["Engineering", "HR", "Engineering", "HR", "Sales", "Sales", "Engineering", "HR"],
        "salary": [25000, 18000, 30000, 16000, 20000, 22000, 28000, 17000],
        "years_experience": [3, 2, 5, 1, 4, 6, 4, 2],
        "performance_score": [8.5, 7.2, 9.1, 6.8, 7.5, 8.8, 8.0, 7.0]
    }

    df = pd.DataFrame(data)

    avg_salary = df.groupby("department")["salary"].mean().to_dict()
    top_performer = df.loc[df["performance_score"].idxmax(), "name"]
    total_employees = len(df)
    avg_performance = df["performance_score"].mean()

    top_performer_row = df.loc[df["performance_score"].idxmax()]
    top_performer_salary = top_performer_row["salary"]
    top_performer_dept = top_performer_row["department"]

    summary = f"""
    Company Data Summary:
    - Total employees: {total_employees}
    - Average performance score: {avg_performance:.1f}
    - Top performer: {top_performer} (Department: {top_performer_dept}, Salary: {top_performer_salary})
    - Average salary by department: {avg_salary}
    - All employees: {df[["name", "department", "salary", "performance_score"]].to_dict("records")}
    """
    return summary

if __name__ == "__main__":
    print(get_company_summary())