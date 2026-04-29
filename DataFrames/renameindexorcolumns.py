# Rename Index Labels or columns in a DataFrame
# The rename method accepts a dictionary for either its columns or index parameter. The keys of the dictionary are the current labels, and the values are the new labels
# We can replace all columns by overwriting the DataFramse's columns attribute with a list of new column names. The list must be the same length as the number of columns in the DataFrame.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()
print(bond)
bond.columns = bond.columns.str.strip()

# Rename index labels example
print("\n Before renaming index labels:")
print(bond)
bond.rename(index={"Diamonds Are Forever": "DAF", "Moonraker": "MR"}, inplace=True)
print("\n After renaming index labels:")
print(bond)

swaps = {
    "A view to a kill": "AVTAK",
    "The Living Daylights": "TLD",
    "The Spy Who Loved Me": "TSWLM",
    "For Your Eyes Only": "FYEO"
    }
print("\n Before renaming index labels:")
print(bond)
bond.rename(index=swaps, inplace=True)
print("\n After renaming index labels:")
print(bond)

# Rename column labels example
print("\n Before renaming column labels:")
print(bond)
bond.rename(columns={"Actor": "Lead Actor", "Bond Actor Salary": "Salary"}, inplace=True)
print("\n After renaming column labels:")
print(bond)

print("\n Before overwriting column labels:")
print(bond)
new_columns = ["Relaease Year", "Bond Guy", "Camera Director", "Revenue", "Film Budget", "Lead Actor Salary"]
bond.columns = new_columns
print("\n After overwriting column labels:")
print(bond)