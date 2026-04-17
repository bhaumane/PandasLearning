# Filter with more than one condition (AND)
# Add the '&' operator in between two Boolean Series to filter by multiple conditions.
# We can assign the Series to variables to make the syntax more readable.

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Female employees who work in Markating
is_female = employees["Gender"] == "Female"
is_in_marketing = employees["Team"] == "Marketing"
print("Female employees who work in Marketing team:")
print(employees[is_female & is_in_marketing])

# Female employees who work in Markating and having salary grater than 100k
is_slary_over_100k = employees["Salary"] > 100000
print("\nFemale employees who work in Marketing team and having salary grater than 100k:")
print(employees[is_female & is_in_marketing & is_slary_over_100k])
