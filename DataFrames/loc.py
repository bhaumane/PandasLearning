# Retrive Rows by Index Lable with loc Accessor
# The 'loc' accessor retrives one or more rows by index label.
# Provide a pair of square brackets after the accessor.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film")
print(bond)
print("loc with single row index:")
print(bond.loc["Goldfinger"])
print("\n loc with for duplicate index column vlaues:")
print(bond.loc["Casino Royale"])
print("\n loc with for multiple column vlaues:")
print(bond.loc[["Octopussy", "Moonraker"]])
print("\n loc with for range column vlaues:")
print(bond.loc["Diamonds Are Forever":"Moonraker"])
print("\n loc with for range column vlaues:")
print(bond.loc["Diamonds Are Forever":])