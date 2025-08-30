import numpy as np
import pandas as pd

# Fixing random seed for reproducibility
np.random.seed(42)

# Generate employee IDs from 1 to 100
employee_ids = np.arange(1, 101)

# Generate random years of experience (0 to 30 years)
years_exp = np.random.randint(0, 31, size=100)

# Generate random salaries ($30,000 to $120,000)
salaries = np.random.randint(30000, 120001, size=100)

# Create a DataFrame
df = pd.DataFrame({
    'EmployeeID': employee_ids,
    'YearsExperience': years_exp,
    'Salary': salaries
})

# Print first 5 rows
print(df.head())

# Save to CSV file
df.to_csv('employee_data.csv', index=False)
