import matplotlib.pyplot as plt

# Sample data: x values (e.g., years) and y values (e.g., sales)
x = [2018, 2019, 2020, 2021, 2022]
y = [100, 150, 200, 250, 300]

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add title to the plot
plt.title('Sales Trend Over Years')

# Add x-axis label
plt.xlabel('Year')

# Add y-axis label
plt.ylabel('Sales (in units)')

# Display grid for better readability
plt.grid(True)

# Show the plot
plt.show()
