# The nsmallest and nlargest Methods
# The nlargest method returns a specified number of rows with the largest values from a given column.
# The nsmallest method returns rows with the smallest values from a given column.
# The nlargest and nsmallest methods are more efficient than sorting the entire DataFrame.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()
bond.columns = bond.columns.str.strip()
print(bond)

print("Select 4 largest rows where box office collection is high:")
print(bond.nlargest(n=4, columns="Box Office"))

print("Select 3 smallest rows where Bond Actor Salary collection is low:")
print(bond.nsmallest(n=3, columns="Bond Actor Salary"))
