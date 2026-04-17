# Filter a DataFrame based on a condition
# Pandas needs a Series of Booleans to perform a filter.
# Pass the Boolean Series inside square brackets after the DataFrame.
# We can generate a Boolean Series using a wide variety of operations (equality, inequality, less than, inclusion etc)

import pandas as pd
import datetime as dt

employees = pd.read_csv("employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
employees["Last Login Time"] = pd.to_datetime(employees["Last Login Time"], format="%H:%M %p").dt.time
employees["Senior Management"] = employees["Senior Management"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")

# Filter the records to select only 'Male' employees.
Male_employees = employees["Gender"] == "Male"
print("List of Male employees:")
print(employees[Male_employees])

# Filter the records to select employees of perticular Team.
Distribution_team = employees["Team"] == "Distribution"
print("\nList of Distribution Team employees:")
print(employees[Distribution_team])

# Filter the list to select only 'Senior Managment' employee
Senior_Management = employees["Senior Management"]  # As columns has boolen values it only select 'True' value records
print("\nSenior Management employees list:")
print(employees[Senior_Management])

# Filter the employees whos salary > 100000
Salary_filter = employees["Salary"] > 100000
print("\nList of employees whos salary is > 100000:")
print(employees[Salary_filter])

# Filte list of employees whos Bonus < 3.5 %
less_bonous = employees["Bonus %"] < 3.5
print("\nList of employees whos bonus is less than 3.5 percent:")
print(employees[less_bonous])

# Filter the list of employees whos start date is less than 2020-01-01
start_date_filter = employees["Start Date"] < "2020-01-01"
print("\nList of employees whos Start Date is less than '2020-01-01':")
print(employees[start_date_filter])

# Filter on time field
time_filter = employees["Last Login Time"] < dt.time(12,0,0)
print("\nList of employees whos login time start after noon:")
print(employees[time_filter])

