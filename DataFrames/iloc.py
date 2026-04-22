# Retrive Rows by index Position with iloc Accessor
# The iloc accessor retrives one or more rows by index position.
# Provide a pair of square brackets after the accessor.
# iloc accepts single values, lists and slices.

import pandas as pd

bond = pd.read_csv("jamesbond.csv")
print("James bond movie list:")
print(bond)
 
single_bond_movie = bond.iloc[5]
print("\n iloc with single value position example output:")
print(single_bond_movie)

multiple_bond_movie = bond.iloc[[15, 20]]
print("\n iloc with multiple value position example output:")
print(multiple_bond_movie)

range_bond_movies = bond.iloc[4:8]
print("\n iloc with range position example output:")
print(range_bond_movies)

range_bond_movies_1 = bond.iloc[:8]
print("\n iloc with range position example 2 output:")
print(range_bond_movies_1)