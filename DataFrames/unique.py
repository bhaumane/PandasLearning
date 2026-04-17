# The unique and nuique methods
# The 'unique' method on a Series returns a collection of its unique values. The method does not exist on a DataFrame.
# The 'nunique' method returns a count of the number of unique values in the Series/DataFrame.
# The 'dropna' parameter configures whether to include or exclude missing ('NaN') values.


import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

print("Unique values in Gender column:")
print(employees["Gender"].unique())

print("\n Unique values in Team column:")
print(employees["Team"].unique())

print("\n Count of unique values in Teams column (excluding NaN):")
print(employees['Team'].nunique())

print("\n Count of unique values in Teams column with NaN included:")
print(employees['Team'].nunique(dropna=False))

print("\n Unique count in all columns:")
print(employees.nunique())