# Difference between Shared Methods
# The sum method adds a Series values.
# On a DataFrame, the sum method adds the values in each column and returns a Series with the sum of each column.
# The axis parameter customized the direction that we add across. Pass "columns" or 0 to add across the columns, 
# and pass "index" or 1 to add across the rows.

import pandas as pd

# Create a DataFrame
revenue = pd.read_csv('revenue.csv', index_col='Date')

# Display the DataFrame
print(revenue)
# Add the values in each column and return a Series with the sum of each column
print('Sum of the values in each column:')
print(revenue.sum())
# or you can use the axis parameter to add across the columns
print('Sum of the values in each column:')
print(revenue.sum(axis='index'))
# Add the values in each row and return a Series with the sum of each row
print('Sum of the values in each row:')
print(revenue.sum(axis='columns'))

# Sum of the values in the DataFrame
print('Sum of the values in the DataFrame:')
print(revenue.sum(axis="columns").sum())