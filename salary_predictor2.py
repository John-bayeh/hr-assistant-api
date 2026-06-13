import numpy as np
from sklearn.linear_model import LinearRegression
X=np.array([
[3, 8.5],
    [2, 7.2],
    [5, 9.1],
    [1, 6.8],
    [4, 7.5],
    [6, 8.8],
    [4, 8.0],
    [2, 7.0]
])
y = np.array([25000, 18000, 30000, 16000, 20000, 22000, 28000, 17000])
model=LinearRegression()
model.fit(X,Y)
score=model.score(X,Y)
