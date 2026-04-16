# Simple Linear Regression Implementation
x = [1, 2, 3, 4, 5]
y = [1,2,3,4,5]

n = len(x)
x_mean = sum(x) / n
y_mean = sum(y) / n

num = 0
den = 0

for i in range(n):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    den += (x[i] - x_mean) ** 2

m = num / den
c = y_mean - m * x_mean

print("Slope (m):", m)
print("Intercept (c):", c)

x_new = 6
y_pred = m * x_new + c
print("Predicted value for x=6:", y_pred)