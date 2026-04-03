# Extract Series values by index labels using the .loc[] method
# The .loc[] method in Pandas Series is used to access values based on their index labels. 
# This method allows you to retrieve values by specifying their index labels, which can be particularly useful when you want to access data using meaningful labels rather than integer positions.
# The .loc[] method accepts label-based indexing, where you can specify the index labels directly to access the corresponding values. You can use this method to access a single value, a range of values, or even specific labels in the Series.
import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', index_col='Name').squeeze("columns")

# Extract a single value based on index label
single_value = pokemon.loc['Jennifer Robinson'] # This will retrieve the value at index label 'Jennifer Robinson'
# Extract a range of values based on index labels
range_of_values = pokemon.loc['Jennifer Robinson':'Sharon Evans']  # This will retrieve values from index labels 'Jennifer Robinson' to 'Sharon Evans'
# Extract specific index labels using a list of labels
specific_values = pokemon.loc[['Carol Turner', 'Jennifer Robinson', 'Sharon Evans']]  # This will retrieve values at index labels 'Carol Turner', 'Jennifer Robinson', and 'Sharon Evans'   
# Extract values using boolean indexing
boolean_values = pokemon.loc[pokemon.index.str.startswith('B')]  # This will retrieve values where the index label starts with 'B'
# Display the extracted values
print("Single value at index label 'Jennifer Robinson':")
print(single_value)
print("\nRange of values from index labels 'Jennifer Robinson' to 'Sharon Evans':")
print(range_of_values)
print("\nSpecific values at index labels 'Carol Turner', 'Jennifer Robinson', and 'Sharon Evans':")
print(specific_values)
print("\nValues where the index label starts with 'B':")
print(boolean_values)