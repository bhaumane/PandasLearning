# The sort_values Method in Pandas Series
# The sort_values method in Pandas Series is used to sort the values in a Series in either ascending or descending order. This method is particularly useful for organizing data and making it easier to analyze.
# By default, sort_values sorts the values in ascending order, but you can specify the ascending parameter to sort in descending order. The method also has an inplace parameter that allows you to modify the original Series without creating a new one.
# When sorting a Series, the index labels are also rearranged to maintain the association between the values and their corresponding indices. This means that the original index labels will be preserved, but they will be reordered according to the sorted values.
# The sort_values method can be used with various data types, including numeric, string, and datetime values. It is a powerful tool for data manipulation and can help you quickly identify trends, outliers, or specific values in your Series.
import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', usecols=['Name']).squeeze("columns")
stock = pd.read_csv('stocksinfo.csv', usecols=['StockName']).squeeze("columns")
# Sort the Series in ascending order
sorted_pokemon_asc = pokemon.sort_values()
sorted_pokemon_asc = pokemon.sort_values(ascending=True) # This is the same as the default behavior of sort_values
sorted_stock_asc = stock.sort_values()
# Sort the Series in descending order
sorted_pokemon_desc = pokemon.sort_values(ascending=False)
sorted_stock_desc = stock.sort_values(ascending=False)

# Display the sorted Series
print("Pokemon sorted in ascending order:")
print(sorted_pokemon_asc)
# print("\nPokemon sorted in descending order:")
# print(sorted_pokemon_desc)
# print("\nStock sorted in ascending order:")
# print(sorted_stock_asc)
# print("\nStock sorted in descending order:")
# print(sorted_stock_desc)