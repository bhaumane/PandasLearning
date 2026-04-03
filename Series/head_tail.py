# The .head() and .tail() methods in Pandas Series are used to retrieve the first and last elements of the series, respectively.
# The .head() method returns the first n elements of the series, where n is specified as an argument (default is 5). This is useful for quickly inspecting the beginning of a series.
# The .tail() method returns the last n elements of the series, where n is specified as an argument (default is 5). This is helpful for examining the end of a series, especially when dealing with large datasets.
# Both methods are commonly used for data exploration and can provide insights into the structure and content of a series without having to print the entire dataset.
import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name']).squeeze("columns")
# Retrieve the first 5 elements of the series using .head()
first_five_pokemon = pokemon.head()

# Retrieve the last 5 elements of the series using .tail()
last_five_pokemon = pokemon.tail()

# Retrieve the first 10 elements of the series using .head()
first_ten_pokemon = pokemon.head(10)

# Retrieve the last 10 elements of the series using .tail()
last_ten_pokemon = pokemon.tail(10)

# Display the results
print("First 5 Pokemon:")
print(first_five_pokemon)
print("\nLast 5 Pokemon:")
print(last_five_pokemon)
print("\nFirst 10 Pokemon:")
print(first_ten_pokemon)
print("\nLast 10 Pokemon:")
print(last_ten_pokemon)