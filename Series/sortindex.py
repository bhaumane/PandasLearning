# The sort_index Method in Pandas Series
# The sort_index method in Pandas Series is used to sort the Series based on its index labels. This method is particularly useful when you want to organize your data according to the index rather than the values.
# By default, sort_index sorts the index in ascending order, but you can specify the ascending parameter to sort in descending order. Similar to sort_values, the sort_index method also has an inplace parameter that allows you to modify the original Series without creating a new one.
# When sorting a Series using sort_index, the values will be rearranged according to the sorted index labels. This means that the original values will be preserved, but they will be reordered based on the new index arrangement.
# The sort_index method can be used with various data types for the index, including numeric, string, and datetime values. It is a powerful tool for data manipulation and can help you quickly organize your Series based on the index labels.
import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', index_col='Name').squeeze("columns")

# Sort the Series by index in ascending order
sorted_pokemon_index_asc = pokemon.sort_index()

# Sort the Series by index in descending order
sorted_pokemon_index_desc = pokemon.sort_index(ascending=False)

# Display the sorted Series
print("Pokemon sorted by index in ascending order:")
print(sorted_pokemon_index_asc)
print("\nPokemon sorted by index in descending order:")
print(sorted_pokemon_index_desc)