# The get method in pandas Series is used to retrieve a value from the series based on a specified index. 
# It is similar to using square brackets for indexing, but it provides additional functionality such as handling missing values gracefully. 
# The get method allows you to specify a default value that will be returned if the specified index is not found in the series, 
# preventing errors that would occur with direct indexing.
import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name']).squeeze("columns")

# Retrieve a value using the get method
pokemon_name = pokemon.get(0)  # Get the first element (index 0)

# Retrieve a value that does not exist, with a default value
non_existent_pokemon = pokemon.get(1000, "Unknown Pokemon")  # Get an element that does not exist, return "Unknown Pokemon"

pokemon.get(["Steven Nelson", "Ash Ketchum"])  # Get multiple elements using a list of indices
pokemon.get(["Steven Nelson", "Unknown Trainer"], "Unknown Pokemon")  # Get multiple elements with a default value for non-existent indices

# Display the results
print("Pokemon at index 0:", pokemon_name)
print("Pokemon at index 1000:", non_existent_pokemon)
print("Pokemon at indices ['Steven Nelson', 'Ash Ketchum']:", pokemon.get(["Steven Nelson", "Ash Ketchum"]))
print("Pokemon at indices ['Steven Nelson', 'Unknown Trainer'] with default value:", pokemon.get(["Steven Nelson", "Unknown Trainer"], "Unknown Pokemon"))