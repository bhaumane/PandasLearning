# The split Method
# The str.split method splits a string by the occurence of a delimiter. Pandas return a Series of lists.
# Use the str.get method to access a nested list element by its indes postion.

import pandas as pd

chicgo = pd.read_csv("chicago.csv").dropna(how="all")
chicgo["Department"] = chicgo["Department"].astype("category")
print(chicgo.head())

chicgo.columns = chicgo.columns.str.strip()

print("The most common first word in our job position/title:")
print(chicgo["Position Title"].str.split(" ").str.get(0).value_counts())

print("\n Finding the most common first name among the employees:")
print(chicgo["Name"].str.split(", ").str.get(1).str.split(" ").str.get(0).value_counts())