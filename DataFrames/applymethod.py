# The apply Method with DataFrames
# The apply method invokes a function on every column or every row in the DataFrame.
# Pass the uninvoked function as the first argument to apply method.
# Pass the axis parameter an argument of "Columns" to invoke the function every row.
# Pandas will pass in the row's values as a Series object. We can use accessors like loc and iloc to extract the column's values for that row.

import pandas as pd

bond = pd.read_csv("jamesbond.csv", index_col="Film").sort_index()


bond.columns = bond.columns.str.strip()
print(bond)



# MOVIE RANKING SYSTEM
#
# COMDITION         -> DESIGNATION
# 80's movie        -> "Great 80's flick"
# pierce Brosnan    -> "The best Bond ever"
# Budget > 100      -> "Expensive movie, fun"
# other             -> "No comment"

def rank_movie(row):
    year = row.loc["Year"]
    actor = row.loc["Actor"].strip()
    budget = row.loc["Budget"]

    if year >= 1980 and year < 1990:
        return "Great 80's flick"
    
    if actor == "Pierce Brosnan":
        return "The best Bond ever"
    
    if budget > 100:
        return "Expensive movie, fun"
    
    return "No comment"

print("Movie list after applying rank_movie funtion:")
print(bond.apply(rank_movie, axis="columns"))