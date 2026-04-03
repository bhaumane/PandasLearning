# Extract Series values based on index positions using the .iloc[] method
# The .iloc[] method in Pandas Series is used to access values based on their integer position in the Series. This method allows you to retrieve values by specifying their index positions, which can be particularly useful when you want to access data without knowing the actual index labels.
# The .iloc[] method accepts integer-based indexing, where the first position is 0, the second position is 1, and so on. You can use this method to access a single value, a range of values, or even specific positions in the Series.
# When using .iloc[], you can specify the index positions in various ways, such as using a single integer, a list of integers, or a slice object. This flexibility allows you to easily extract the desired values from the Series based on their position.
import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name']).squeeze("columns")

# Extract a single value based on index position
single_value = pokemon.iloc[0]  # This will retrieve the value at index position 0
# Extract a range of values based on index positions
range_of_values = pokemon.iloc[0:5]  # This will retrieve values from index positions 0 to 4
# Extract specific index positions using a list of integers
specific_values = pokemon.iloc[[0, 2, 4]]  # This will retrieve values at index positions 0, 2, and 4
# Extract last value using negative indexing
last_value = pokemon.iloc[-1]  # This will retrieve the last value in the Series
# Extract values from the end using negative indexing
last_five_values = pokemon.iloc[-5:]  # This will retrieve the last five values in the Series

# Display the extracted values
print("Single value at index position 0:")
print(single_value)
print("\nRange of values from index positions 0 to 4:")
print(range_of_values)
print("\nSpecific values at index positions 0, 2, and 4:")
print(specific_values)
print("\nLast value in the Series:")
print(last_value)
print("\nLast five values in the Series:")
print(last_five_values)
