# Sort a DataFrame with the sort_values Method
# The 'sort_values' method sorts a DataFrame by the values in one or more columns. The default sort is an ascending one (alphabetical for string).
# The first parameter (by) expect the column(s) to sort by.
# If sorting by a single column, pass a string with its name.
# The 'ascending' parameter customized the sort order.
# The 'na_position' paramter customize where pandas places 'NaN' values.

# To sort by multiple columns, pass the 'by' parameter a list of column names. Pandas will sort in the specified column order (first to last).
# Pass the 'ascending' parameter a Boolean to sort all columns in a consistent order (all ascending or all descending).
# Pass 'ascending' a list to customize the sort order per column. The ascending list length must match by 'by' list.

import pandas as pd

nba = pd.read_csv("nba.csv")
print(nba)

print("Sort on column Name")
print(nba.sort_values("Name"))
print("\nSort on column Name using by gives same reslut as above")
print(nba.sort_values(by="Name"))
print("\nSort on column Name using ascending = True")
print(nba.sort_values(by="Name", ascending=True))
print("\nSort on column Name in decending order using ascending = False")
print(nba.sort_values(by="Name", ascending=False))

print("\nSort on column Salary by placing 'NaN' columns at last")
print(nba.sort_values("Salary", na_position="last"))

print("\nSort on column Salary by placing 'NaN' columns at first")
print(nba.sort_values("Salary", na_position="first"))

print("\nSort on column Salary by placing 'NaN' columns at first and in decending order")
print(nba.sort_values("Salary", na_position="first", ascending=False))

print("\nSort on multiple columns")
print(nba.sort_values(by=["Team", "Name"]))
print("\nSort on multiple columns in decending order")
print(nba.sort_values(by=["Team", "Name"], ascending=False))
print("\nSort on multiple columns in different order")
print(nba.sort_values(by=["Team", "Name"], ascending=[True, False]))

# The 'sort_index' method sorts thd DataFrame by its index position/labels.
print("\nSort using sort_index method")
print(nba.sort_index()) 
print("\nSort using sort_index method and in decending order")
print(nba.sort_index(ascending=False))