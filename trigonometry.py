import numpy as np
import matplotlib.pyplot as plt

# Create x values from 0 to 2π
x = np.linspace(0, 2*np.pi, 1000)

# Calculate trigonometric functions
y_sin = np.sin(x) + np.sin(2*x)
y_cos = 2 * np.cos(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', linewidth=2)
plt.plot(x, y_cos, label='cos(x)', linewidth=2)
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid(True)
plt.show()
