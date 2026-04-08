# The map Method
# The map method is used to map values of a Series according to an input mapping or a function.
# It is often used for substituting each value in a Series with another value, which may be derived from a function, a dictionary, or a Series.
import pandas as pd
# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name']).squeeze("columns")

# Create a mapping dictionary to map Pokemon names to their types
type_mapping = {
    'John Doe': 'Grass/Poison',
    'Jane Smith': 'Fire',
    'Michael Brown': 'Water',
    'Emily Davis': 'Electric',
    'Chris Wilson': 'Normal'
}

# Use the map method to map Pokemon names to their types
pokemon_types = pokemon.map(type_mapping)

# Display the results
print("Pokemon names:")
print(pokemon)
print("\nMapped Pokemon types:")
print(pokemon_types)

# Example with a function
def get_type(name):
    return type_mapping.get(name, 'Unknown')
pokemon_types_function = pokemon.map(get_type)
print("\nMapped Pokemon types using a function:")
print(pokemon_types_function)

# Example with a lambda function
pokemon_types_lambda = pokemon.map(lambda name: type_mapping.get(name, 'Unknown'))
print("\nMapped Pokemon types using a lambda function:")
print(pokemon_types_lambda)