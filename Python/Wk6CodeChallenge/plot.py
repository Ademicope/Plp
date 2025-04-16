import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
# plt.plot(x, y)
#plt.title("Simple Line Plot")
#plt.xlabel("X-axis")
#plt.ylabel("Y-axis")
#plt.show()

# Sample data
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

plt.bar(names, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()