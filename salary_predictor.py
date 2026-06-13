import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Prepare data
# [years_experience, performance_score]
X = np.array([
    [3, 8.5],
    [2, 7.2],
    [5, 9.1],
    [1, 6.8],
    [4, 7.5],
    [6, 8.8],
    [4, 8.0],
    [2, 7.0]
])

# Salaries (what we want to predict)
y = np.array([25000, 18000, 30000, 16000, 20000, 22000, 28000, 17000])

# Step 2: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Check accuracy
score = model.score(X, y)
print(f"Model accuracy: {score:.2%}")

# Step 4: Predict new employee salary
new_employee = np.array([[4, 8.0]])
predicted = model.predict(new_employee)
print(f"Predicted salary for 4 years exp, score 8.0: {predicted[0]:,.0f} ETB")
new_employee2 = np.array([[6, 9.5]])
predicted2 = model.predict(new_employee2)
print(f"Senior employee prediction: {predicted2[0]:,.0f} ETB")
print(f"Experience weight: {model.coef_[0]:,.0f}")
print(f"Performance weight: {model.coef_[1]:,.0f}")
print(f"Base salary: {model.intercept_:,.0f}")