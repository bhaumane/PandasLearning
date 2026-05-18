# Filtering with string method
# The str.contains method checks whether a substring exist anywhere in the string.
# The str.startswith method checks whether a substring exist at the beginning of the string.
# The str.endswith method checks whether a substring exist at the end of the string.


import pandas as pd

chicgo = pd.read_csv("chicago.csv").dropna(how="all")
chicgo["Department"] = chicgo["Department"].astype("category")
print(chicgo)

print("List of records containing word police in Department column:")
police_dept = chicgo["Department"].str.lower().str.contains("police")
print(chicgo[police_dept])

print("\n List of records starts with word chicago in Department column:")
police_dept_startwith = chicgo["Department"].str.lower().str.startswith("chicago")
print(chicgo[police_dept_startwith])

print("\n List of records ends with word finance in Department column:")
police_dept_endswith = chicgo["Department"].str.lower().str.endswith("finance")
print(chicgo[police_dept_endswith])