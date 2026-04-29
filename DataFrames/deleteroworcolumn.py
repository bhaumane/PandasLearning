# Delete Rows or Columns from a DataFrame
# The drop method deletes rows or columns from a DataFrame. 
# Pass the index or columns parameters a list of column names to remove.
# The pop method removes and returns a single Series from a DataFrame. Pass the name of the column to remove as an argument to the pop method.
# Python's del keyword can also be used to remove a column from a DataFrame. Pass the name of the column to remove as an argument to the del keyword.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()
print(bond)
bond.columns = bond.columns.str.strip()

# Delete rows example
print("\n Before deleting rows:")
print(bond)
bond.drop(index=["Diamonds Are Forever", "Moonraker"], inplace=True)
print("\n After deleting rows:")
print(bond)

# Delete columns example with drop method
print("\n Before deleting columns:")
print(bond)
bond.drop(columns=["Director", "Box Office"], inplace=True)
print("\n After deleting columns:")
print(bond)

# Delete columns and index example with drop method
print("\n Before deleting columns and index:")
print(bond)
bond.drop(index=["Octopussy", "A View to a Kill"], columns=["Actor", "Bond Actor Salary"], inplace=True)
print("\n After deleting columns and index:")
print(bond)

# Delete columns example with pop method
print("\n Before deleting column with pop method:")
print(bond)
year_pop = bond.pop("Year")
print("\n After deleting column with pop method:")
print(year_pop)

# Delete columns example with del keyword
print("\n Before deleting column with del keyword:")
print(bond)
del bond["Budget"]
print("\n After deleting column with del keyword:")
print(bond)
