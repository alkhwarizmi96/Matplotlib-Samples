import matplotlib.pyplot as plt
import math

def f(x):
    # log base 4 of (2x - 3)
    # log₄(a) = log(a) / log(4)
    return math.log(2*x - 3) / math.log(4)

# Generate x values (must be > 1.5 because 2x-3 > 0)
x = []
step = 0.01
i = 1.51  # Start just above the vertical asymptote
while i <= 10:
    x.append(i)
    i += step

y = [f(val) for val in x]

plt.clf()
plt.plot(x, y, linewidth=2, color='blue')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = log₄(2x - 3)')

# Add vertical asymptote at x = 1.5
plt.axvline(x=1.5, color='red', linestyle='--', alpha=0.5, label='Vertical asymptote at x=1.5')

# Add horizontal axis
plt.axhline(y=0, color='black', linewidth=0.8)

plt.legend()
plt.xlim(1.4, 10)
plt.ylim(-5, 5)
plt.show()
