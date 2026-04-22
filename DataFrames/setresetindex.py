# The set_index and reset_index Methods
# The index serves as the collection of primary identifiers/lables/entrypoints of the rows.
# The fastest way to extract a row is from a sorted index by position/label.
# Pandas uses index labels/values when merging different objects together.
# The 'set_index' method sets an existing column as the index of the DataFrame.
# The 'reset_index' method sets the standard ascending numeric index as the index of the DataFrame.

import pandas as pd

bond = pd.read_csv("jamesbond.csv") 
print("Orignal Jamesbond films list:")
print(bond)

bond = bond.set_index("Film")  
print("\nAfter set index method applied:")
print(bond)

bond = bond.reset_index("Film")
print("\nAfter reset index method applied:")
print(bond)