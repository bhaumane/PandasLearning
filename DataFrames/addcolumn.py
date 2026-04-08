# Add a new column to a DataFrame
# We can add a new column to a DataFrame by assigning a value to a new column name. The syntax is df['new_column_name'] = value.
# The insert method allows us to add a new column at a specific position in the DataFrame. The syntax is df.insert(loc, column_name, value).
# On the right-hand side, we can reference an existing column in the DataFrame, perform a calculation, or assign a constant value to the new column.
import pandas as pd

# Create a DataFrame
nba = pd.read_csv('nba.csv')
# Add a new column to the DataFrame by assigning a value to a new column name
nba['New Column'] = 'New Value'
print('Display the DataFrame with the new column:')
print(nba.head())

# Add a new column to the DataFrame using the insert method
nba.insert(1, 'Inserted Column', 'Inserted Value')
print('Display the DataFrame with the inserted column:')
print(nba.head())

nba.insert(loc=2, column='Another Column', value='Another Value')
print('Display the DataFrame with another inserted column at position 2:')
print(nba.head())

# Add a new column to the DataFrame by referencing an existing column and performing a calculation
nba['Salary in USD'] = nba['Salary'] * 1.1  # Example calculation
print('Display the DataFrame with the new column:')
print(nba.head())