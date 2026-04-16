# Linear Regression to plot
import matplotlib.pyplot as plt

# Given data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
n = len(x)

# Calculate mean
x_mean = sum(x)/n
y_mean = sum(y)/n

# Calculate slope (m)
num = 0
den = 0
for i in range(n):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    den += (x[i] - x_mean) ** 2
m = num / den

# Calculate intercept (c)
c = y_mean - m * x_mean

print("Slope (m):", m)
print("Intercept (c):", c)

# Predicted values
y_pred = [m * xi + c for xi in x]

# Plot graph
plt.scatter(x, y)
plt.plot(x, y_pred)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression Graph")
plt.show()