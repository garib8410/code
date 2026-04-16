# Histogram
import matplotlib.pyplot as plt

# Sample data (Student Marks)
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 
         55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Create Histogram
plt.hist(marks, bins=5, edgecolor='black')

# Add labels and title
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Display grid
plt.grid(True)

# Show the plot
plt.show()