# Create Random Sample with the sample Method
# The sample method returns a specified one or more random rows from the DataFrame.
# Customize the axis parameter to extract random columns.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()
bond.columns = bond.columns.str.strip()

# select random row 
print("Selecting Random row using sample method:")
print(bond.sample())
print("\nSelecting Random number of rows using sample method:")
print(bond.sample(n=5))
print("\nSelecting random rows using axis parameter:")
print(bond.sample(n=3, axis="index"))
print("\nSelecting random columns using axis parameter:")
print(bond.sample(n=3, axis="columns"))


