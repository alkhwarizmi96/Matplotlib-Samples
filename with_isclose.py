import numpy as np
import matplotlib.pyplot as plt

# Define multiple functions
def f1(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        result = x
        result[np.isclose(x, 2, 0.001953125)] = np.nan
        return result

def f2(x):
    return abs(x-2) / (x - 2)

def f3(x):
    return 1 / ((x - 2)**2)


# Create x values
x = np.linspace(-5, 5, 1000)

# Calculate y values
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

# Create the plot
plt.figure(figsize=(10, 10))
plt.plot(x, y1, linewidth=2, color='blue', label='(x² - 4)/(x-2)')
plt.plot(x, y2, linewidth=2, color='red', label='abs(x-2)/(x-2)')
plt.plot(x, y3, linewidth=2, color='green', label='1/(x-2)²')

# Add grid and labels
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Multiple Functions', fontsize=14)

# Add x and y axes
plt.axhline(y=0, color='black', linewidth=0.8)
plt.axvline(x=0, color='black', linewidth=0.8)

# Set limits and ticks
plt.ylim(-10, 10)
plt.yticks(np.arange(-10, 10, 1))
plt.xticks(np.arange(-10, 10, 1))

plt.legend()
plt.show()
