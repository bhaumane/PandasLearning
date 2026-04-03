# Inclusion and Exclusion Operations in Pandas Series
# The 'in' and 'not in' operators can be used to check for the presence or absence of values in a Pandas Series. 
# This is particularly useful for filtering data or validating the contents of a Series.
# The 'in' keyword checks if a value exists in the Series, while 'not in' checks if it does not exist.
# Use the index and values attributes of the Series to perform these checks effectively.
# Combine the in keyword with values to check for the presence of specific values in the Series, 
# and use not in to check for their absence.

import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name']).squeeze("columns")
stock = pd.read_csv('stocksinfo.csv', usecols=['StockName']).squeeze("columns")

# Check if 'Jane Smith' is in the pokemon Series
is_jane_smith_in_pokemon = 'Jane Smith' in pokemon.values
print(f"Is Jane Smith in the pokemon Series? {is_jane_smith_in_pokemon}")

# Check if 'Apple' is in the stock Series
is_apple_in_stock = 'Apple' in stock.values
print(f"Is Apple in the stock Series? {is_apple_in_stock}")

# Check if 'Bulbasaur' is not in the pokemon Series
is_bulbasaur_not_in_pokemon = 'Bulbasaur' not in pokemon.values
print(f"Is Bulbasaur not in the pokemon Series? {is_bulbasaur_not_in_pokemon}")
