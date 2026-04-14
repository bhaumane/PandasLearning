# The value_count Method
# The value_count method counts the number of times that each unique vlaue occures in a Series.

import pandas as pd

nba = pd.read_csv("nba.csv")
print(nba.head())

position_count = nba["Position"].value_counts()
print(position_count)

Team_count = nba["Team"].value_counts()
print(Team_count)

Team_count_normalize = nba["Team"].value_counts(normalize=True) * 100
print(Team_count_normalize)
