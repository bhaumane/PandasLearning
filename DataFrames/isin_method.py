# The isin Method
# The isin Series method accepts a collection object like a list, tuple or Series.
# The method returns True for a row if its value is found in the collection.

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Employees who work in 'Client Services' or 'Finance' or 'Human Resources' Team.
target_teams = employees["Team"].isin(['Client Services', 'Finance', 'Human Resources'])
print("Employees who work in 'Client Services' or 'Finance' or 'Human Resources' Team.:")
print(employees[target_teams])