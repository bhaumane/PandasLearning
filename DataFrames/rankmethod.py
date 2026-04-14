# Rank values with the rank Method.
# The 'rank' method assigns a numeric ranking to each Series value.
# Pandas will assign the same rank to equal values and create a "gap" in the dataset for the ranks.

import pandas as pd

nba = pd.read_csv("nba.csv").dropna(how="all")
# Fill or replace 'NaN' values with 0 and change the type to int.
nba["Salary"] = nba["Salary"].fillna(0).astype(int)

# Add new 'Salary Rank' column with highest salary as rank 1 and in that order and convert it to int type
nba["Salary Rank"] = nba["Salary"].rank(ascending=False).astype(int)
nba = nba.sort_values("Salary", ascending=False)
print(nba)