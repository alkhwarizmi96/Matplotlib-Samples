import matplotlib.pyplot as plt

# Data
years_1 = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003]
values_1 = [12.69, 16.35, 20.29, 25.08, 30.81, 38.75, 45.00, 49.16, 55.15]

years_2 = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
values_2 = [62.852, 68.63, 76.64, 82.47, 85.68, 89.14, 91.86, 95.28, 98.17]

# Combine all years and values
all_years = years_1 + years_2
all_values = values_1 + values_2

# Create scatter plot
plt.figure(figsize=(12, 6))

# Basic scatter plot
plt.scatter(all_years, all_values, color='blue', s=100, alpha=0.7,
            edgecolors='black', linewidth=1.5)

# Add labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Scatter Plot of Data (1995-2012)', fontsize=14, fontweight='bold')

# Add grid
plt.grid(True, alpha=0.3)

# Format x-axis
plt.xticks(all_years, rotation=45)

# Add value labels on points
for i, (x, y) in enumerate(zip(all_years, all_values)):
    plt.annotate(f'{y:.2f}', (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center', fontsize=9)

plt.tight_layout()
plt.show()
