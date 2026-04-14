# The astype Method
# The 'astype' method converts a Series's values to a spacified type.
# Pass in the specified type as either a string or the core Pythod data type.
# Pandas cannot convert 'NaN' values to numeric types, so we need to eliminate/replace them before we perform the conversion.
# The 'dtypes' attribute returns a Series with the DataFrame's columns and their types.

# The 'category' type is ideal for columns with a limited number of unique values.
# The 'nunique' method will return a Series with the number of unique values in each column.
# With categories, pandas does not create a separate value in memory for each "cell". Rather, the cells point to a single copy for each unique value.

import pandas as pd

nba = pd.read_csv("nba.csv").dropna(how="all")
print("Original List")
print(nba)
print("\n Data Type")
print(nba.dtypes)

# Replace salary column missing values with 0 and change its type to int
nba["Salary"] = nba["Salary"].fillna(0)
nba["Salary"] = nba["Salary"].astype("int")
print("\nList after salary column data type changed to int: ")
print(nba)
print("\n Data Type after type changed to int")
print(nba.dtypes)

print("\n Number of unique value for column Team")
print(nba["Team"].nunique())
print("\n Number of unique value for each column in nba list:")
print(nba.nunique())
print("\n nba list information with memory usage:")
print(nba.info())

nba["Position"] = nba["Position"].astype("category")
print("\n nba list information with memory usage after appling category for Position column:")
print(nba.info())

nba["Team"] = nba["Team"].astype("category")
print("\n nba list information with memory usage after appling category for Team column:")
print(nba.info())