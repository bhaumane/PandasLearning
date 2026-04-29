# Filtering with the where Method
# Similar to square bracketes or loc, the where method filters the original DataFrame with a Boolean Series.
# Pandas will populate rows that do not match the criteria with NaN values.
# Leaving in the NaN values can be advantageous for certain merge and visualiaztion opearations.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()
print(bond)
bond.columns = bond.columns.str.strip()

print("\n Filter rows where Actor is Sean Connery:")
actor_is_sean_connnery = bond["Actor"].str.strip() == "Sean Connery"
print(bond.where(actor_is_sean_connnery))
