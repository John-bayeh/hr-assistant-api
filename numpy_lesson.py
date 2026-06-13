import numpy as np
import pandas as pd
salaries=np.array([25000, 18000, 30000, 16000, 20000, 22000, 28000, 17000])
print("salaries",salaries)
print("Sum of the salaries",salaries.sum())
print("Average salaries",salaries.mean())
print("Max salaries",salaries.max())
print("Min salaries",salaries.min())
print("std",salaries.std())
raise_salary=salaries*1.10
print("raise salaries",raise_salary)
above_average=salaries[salaries>=salaries.mean()]
print("Above Average",above_average)
