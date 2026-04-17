# The drop_duplicates Method
# The 'drop_duplicates' method deletes rows with duplicate values.
# By default, it will remove a row if all of its values are shared with another row.
# The 'subset' parameter configures the columns to look for duplicate values within.
# Pass a list to 'subset' parameter to look for duplicates across multiple columns.

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Drop duplicates if all row value matches
print("Drop duplicates if all row value matches:")
print(employees.drop_duplicates())

# Drop duplicates in Team column. Keeps first occurence found.
print("\n Drop duplicates in Team column:")
print(employees.drop_duplicates("Team"))
print("\n Drop duplicates in Team column with Keep:")
print(employees.drop_duplicates("Team", keep="first"))

print("\n Drop duplicates in Team column with Keep last found:")
print(employees.drop_duplicates("Team", keep="last"))

print("\n Drop duplicates in Team column with Keep false:")
print(employees.drop_duplicates("Team", keep=False))

print("\n Drop duplicates in First Name column with Keep false:")
print(employees.drop_duplicates("First Name", keep=False))

print("\n Drop duplicates in multiple columns :")
print(employees.drop_duplicates(["Senior Management", "Team"], keep="last").sort_values("Team"))