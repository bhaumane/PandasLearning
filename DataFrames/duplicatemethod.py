# The duplicated method.
# The 'duplicated' method returns True if a Series value is duplicate.
# Pandas will mark one occurrence of a repeated value as non-duplicated.
# Use the keep parameter to designate whether the first or last occurrence of a repeated value should be considered the "non-duplicate".
# Pass False to the 'keep' parameter to mark all occurrences of repeated values as duplicates.
# Use the tilde symbol (~) to invert a Series values. Trues will become Falses, and Falses will become trues.


import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Employees with duplicate First Name
print(employees[employees["First Name"].duplicated()])
print("\n Keep first duplicated:")
print(employees[employees["First Name"].duplicated(keep="first")])
print("\n Keep last duplicated:")
print(employees[employees["First Name"].duplicated(keep="last")])
print("\n Mark all occurrences of repeated values as duplicates:")
print(employees[employees["First Name"].duplicated(keep=False)])
print("\n Mark all occurrences of not repeated values as duplicates:")
print(employees[~employees["First Name"].duplicated(keep=False)])