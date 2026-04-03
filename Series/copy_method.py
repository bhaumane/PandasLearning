# The copy Method in Pandas Series
# The copy method in Pandas Series is used to create a new Series that is a copy of the original Series. 
# This method is particularly useful when you want to create a new Series that is independent of the original Series, 
# allowing you to modify the new Series without affecting the original one.
# When you use the copy method, it creates a new Series object with the same data and index as the original Series. 
# However, the new Series is a separate object in memory, so changes made to the new Series will not affect the original Series. 
# This is important to keep in mind when working with data, as it allows you to avoid unintended side effects when modifying your data.

# A view is a different way of looking at the same data in memory, while a copy is a completely separate object with its own data.
# Changes to veiw will affect the original data, while changes to a copy will not affect the original data.

import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name'])

# Create a view of the original Series
pokemon_view = pokemon.squeeze("columns")  # This creates a view of the original Series
pokemon_view[0] = 'Whatever'  # Modifying the view will affect the original Series

# Display the original Series and the view
print("\nView of the original Series:")
print(pokemon_view)
print("Original Series after modifying the view:")
print(pokemon)  

# Create a copy of the original Series
pokemon_copy = pokemon.copy()
pokemon_copy.iloc[1] = 'Whatever'  # Modifying the copy will not affect the original Series

# Display the original Series and the copy
print("\nOriginal Series after modifying the copy:")
print(pokemon)
print("\nCopy of the original Series:")
print(pokemon_copy)