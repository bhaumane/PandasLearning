# Common String Methods
# A Series has a special str attribute that exposes an object with string methods.
# Access the str attribute, then invoke the string method on the nested object.
# Most method names will match their Python method equivalents (upper, lower, titel, etc).

import pandas as pd

chicgo = pd.read_csv("chicago.csv").dropna(how="all")
chicgo["Department"] = chicgo["Department"].astype("category")
print(chicgo)

# String method examples
print(chicgo["Position Title"].str.upper())
print(chicgo["Position Title"].str.lower())
print(chicgo["Position Title"].str.title())
print(chicgo["Position Title"].str.len())
print(chicgo["Position Title"].str.title().str.len())
print(chicgo["Position Title"].str.strip())
print(chicgo["Position Title"].str.lstrip())
print(chicgo["Position Title"].str.rstrip())

print(chicgo["Department"].str.replace("POLICE", "PD"))