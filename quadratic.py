import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (1 / 30) * (x + 3) * (x - 2)**2 * (x - 5)

# Create x values from -6 to 7 (to see the important features)
x = np.linspace(-20, 20, 1000)

# Calculate y values
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, color='blue', label='f(x) = (1/30)(x+3)(x-2)²(x-5)')

# Add grid and labels
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Plot of f(x) = (1/30)(x+3)(x-2)²(x-5)', fontsize=14)

# Add x and y axes
plt.axhline(y=0, color='black', linewidth=0.8)
plt.axvline(x=0, color='black', linewidth=0.8)

# Mark the roots
plt.axvline(x=-3, color='red', linestyle='--', alpha=0.5, label='Root at x = -3 (double)')
plt.axvline(x=5, color='green', linestyle='--', alpha=0.5, label='Root at x = 5')

# Set y-axis limits to better see the shape
plt.ylim(-100, 50)

plt.legend()
plt.show()
