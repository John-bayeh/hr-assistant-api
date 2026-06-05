name: str="Yohannes"
salary: int=1000
is_employee: bool=True
score: float=90.2
def get_employee_summary(name:str,salary:int,is_employee:bool,score:float)->str:
    return f"{name} earns {salary} per month. Active:{is_employee}. Score:{score} "
print(get_employee_summary(name,salary,is_employee,score))