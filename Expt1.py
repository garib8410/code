import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Mean:", np.mean(arr))

data = {"Name": ["A", "B", "C"], "Marks": [85, 90, 88]}
df = pd.DataFrame(data)
print(df)

plt.plot([1,2,3,4], [10,20,25,30])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()