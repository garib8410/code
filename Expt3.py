import numpy as np
import matplotlib.pyplot as plt

# Input data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculate slope (m) and intercept (c)
m, c = np.polyfit(x, y, 1)
print("Slope (m):", m)
print("Intercept (c):", c)

# Predicted values
y_pred = m * x + c
print("Predicted Output:", y_pred)

# Plot graph
plt.scatter(x, y)
plt.plot(x, y_pred)
plt.xlabel("Independent Variable (X)")
plt.ylabel("Dependent Variable (Y)")
plt.title("Linear Regression Graph")
plt.show()