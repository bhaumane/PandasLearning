# DataFrame : Filtering Data
# The pd.to_datetime method converts a Series to hold datetime values.
# The 'format' parameter informs pandas of the format that the time are stored in.
# We pass symbols designating the segments of the string. For example %m means 'month' and %d means day.
# The dt attribute reveals an object with many datetime-related attributes and methods.
# The dt.time attribute extracts only the time from each value in a datetime Series.
# Use the 'astype' method to convert the values in a Series to another type.
# The parse_dates parameter of 'read_csv' is an alternate way to parse strings as datetimes.

import pandas as pd

employees = pd.read_csv("employees.csv")
print("Employees Details:")
print(employees)
print(employees.info())

# employees["Start Date"] = pd.to_datetime(employees["Start Date"], format='%m/%d/%Y')
employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

print("Employee List after converting columns to their spacific format:")
print(employees)
print(employees.info()) 