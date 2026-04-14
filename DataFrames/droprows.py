# Drop row with missing values
# Pandas used a NaN designation for cells that hava a missing value.
# The 'dropna' method deletes rows with missing values. Its default behavior is to remove a row if it has any missing values.
# Pass the 'how' parameter an argument of "all" to delete rows where all the values are NaN.
# The subset parameters customizes/limits the columns that pandas will use to drop rows with missing values.

import pandas as pd

nba = pd.read_csv("nba.csv")
print(nba)

# Drop all rows with missing values. Drop row if any column have missing or no vlaue.
drop_all = nba.dropna()
print("Drop all rows with missing values.")
print(drop_all)

# Drop row with any missing value.
drop_all_None = nba.dropna(how="any")
print("\nDrop all rows with any missing values.")
print(drop_all_None)

# Drop all rows where all the columns have NaN value or missing values.
drop_all_row = nba.dropna(how="all")
print("\nDrop all rows where all the columns have NaN value: ")
print(drop_all_row)

# Checking spacific column to drop the row with missing values.
drop_spacific_col = nba.dropna(subset=["College", "Salary"])
print("\nCheck spacific row to drop the missing values ")
print(drop_spacific_col) 