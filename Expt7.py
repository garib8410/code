import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    'Hours_Studied': [2, 4, 6, 8, 10],
    'Attendance': [60, 70, 75, 85, 90],
    'Marks': [45, 55, 65, 75, 85]
}

df = pd.DataFrame(data)
X = df[['Hours_Studied', 'Attendance']]
Y = df['Marks']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print("Regression Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predicted Marks:", Y_pred)