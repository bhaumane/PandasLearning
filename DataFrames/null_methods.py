# The isnull and notnull Methods
# The 'isnull' method returns True for 'NaN' values in a Series.
# The 'notnull' method returns True for present values in a Series.

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Employees whos First name is not null and Team is null.
name_not_null = employees["First Name"].notnull()
team_is_null = employees["Team"].isnull()
print("Employees whos First name is not null and Team is null:")
print(employees[name_not_null & team_is_null])