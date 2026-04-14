# Fill in Missing values with fillna Method
# The 'fillna' method replaces missing 'NaN' values with its argument.
# The 'fillna' method is available on both DataFrames and Series.
# An extracted Series is a view on the original DataFrame, but the 'fillna' method returns a copy.

import pandas as pd

nba = pd.read_csv("nba.csv").dropna(how="all")
print("Original List")
print(nba)

# Replace all missing 'NaN' values with '0'.
print("\nList with all NaN values replaced with 0:")
print(nba.fillna(0))

# Replace Salary column missing values with 0
nba["Salary"] = nba["Salary"].fillna(0)
print("\n List where Salary column values replaced with 0: ")
print(nba["Salary"])
print("\n Updated original List")
print(nba)

# Replace College column missing value with "Unknown".
nba["College"] = nba["College"].fillna(value="Unknown")
print("\n List where College column values replaced with Unknown: ")
print(nba["College"])
print("\n Updated original List")
print(nba)
