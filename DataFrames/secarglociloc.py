# Second argument to loc and iloc Accessors
# The second value inside the square brackets targets the columns.
# The 'iloc' requires numeric positions for rows and columns.
# The 'loc' requires labels for rows and columns.

# Overwrite values in a DataFrame with loc and iloc Accessors
# Use the iloc or loc accessors to overwrite values in a DataFrame to target value, then provide the equal sign and the new value.

# Overwrite multiple values in a DataFrame with loc and iloc Accessors
# The replace method replaces all occurences of a series value with another value (think of it like "find and replace")
# To overwrite multiple values in a DataFrame, remember to use an accessor on the DataFrame itself.
# Accessores like loc and iloc can accept Boolean series. Use them to target the values to overwriete.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()
print(bond)

bond.columns = bond.columns.str.strip()
print(bond.loc["Diamonds Are Forever", "Director"])
print(bond.loc[["Diamonds Are Forever", "Moonraker"], "Director"])
print(bond.loc[["Diamonds Are Forever", "Moonraker"], "Director":"Budget"])
print(bond.loc["GoldenEye":"Spectre", "Director":"Budget"])
print(bond.loc["GoldenEye":"Spectre", ["Actor", "Bond Actor Salary", "Year"]])

print(bond.iloc[3, 1])
print(bond.iloc[3, 1:4])
print(bond.iloc[3:6, 1:4])
print(bond.iloc[3:6, [1, 2, 3]])
print(bond.iloc[[0,2], 3])

# Overwrite values example
print("\n Before overwriting value:")
print(bond.loc["Diamonds Are Forever", "Director"])
bond.loc["Diamonds Are Forever", "Director"] = "Sir Guy Hamilton"
print("\n After overwriting value:")
print(bond.loc["Diamonds Are Forever", "Director"])

# Overwrite multiple values example
print("\n Before overwriting values:")
print(bond.loc[["Diamonds Are Forever", "Moonraker"], "Director"])
bond.loc[["Diamonds Are Forever", "Moonraker"], "Director"] = ["Sir Guy Hamilton", "Sir  Lewis Gilbert"]
print("\n After overwriting values:")
print(bond.loc[["Diamonds Are Forever", "Moonraker"], "Director"])

# Replace values example
print("\n Before replacing values:")
print(bond["Actor"])
bond["Actor"] = bond["Actor"].str.strip().replace("Sean Connery", "Sir Sean Connery")
print("\n After replacing values:")
print(bond["Actor"])