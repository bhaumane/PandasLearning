# The between method
# The 'between' method returns True if a Series value is found within its range.

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Employees whos salary between 60000 and 70000
print("Employees whos salary between 60000 and 70000:")
print(employees[employees["Salary"].between(60000, 70000)])

# Employees whos bonus between 2.0 and 5.0
print("\nEmployees whos bonus between 2.0 and 5.0:")
print(employees[employees["Bonus %"].between(2.0, 5.0)])

# Employees whos start date between 2012-01-01 and 2013-01-01
print("\nEmployees whos start date between 2012-01-01 and 2013-01-01:")
print(employees[employees["Start Date"].between("2012-01-01", "2013-01-01")])

# Employees whos Login time between 8:30 AM and 12:00 AM
print("\nEmployees whos Last Login time between 8:30 AM and 12:00 AM:")
print(employees[employees["Last Login Time"].between(dt.time(8,30), dt.time(12,0))])

