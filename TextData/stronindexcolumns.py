# String Methods on Index and Columns
# Use the index and columns attributes to access the DataFrame index/column labels.
# These objects support string methods via their own str attribute.

import pandas as pd

chicgo = pd.read_csv("chicago.csv", index_col="Name").dropna(how="all").sort_index()
chicgo["Department"] = chicgo["Department"].astype("category")
print(chicgo)

print("String method on Index:")
chicgo.index = chicgo.index.str.strip().str.title()
print(chicgo.head())

print("String method on Column:")
chicgo.columns = chicgo.columns.str.upper()
print(chicgo.head())