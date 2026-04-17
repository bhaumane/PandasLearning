# Filter with more than one condition (OR)
# Use the '|' operator in between two boolean Series to filter by either condition

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Employeees who are either senior management OR started before January 1st 2012
is_senior_management = employees["Senior Management"]
is_started_over_jan90 = employees["Start Date"] < "2012-01-01"
print("Employeees who are either senior management OR started before January 1st 2015:")
print(employees[is_senior_management | is_started_over_jan90])

# First Name is Mark who work in Finance OR start date before January 1st 2012
is_mark = employees["First Name"] == "Mark"
is_in_finance = employees["Team"] == "Finance"
is_started_before2012 = employees["Start Date"] < "2012-01-01"
print("\n First Name is Mark who work in Finance OR start date before January 1st 2012:")
print(employees[(is_mark & is_in_finance) | is_started_before2012])