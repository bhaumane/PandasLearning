# Methods and Attributes between DataFrame and Series
# A DataFrame is a 2-dimensional labeled data structure, while a Series is a 1-dimensional labeled data structure.
# Pandas uses NaN (Not a Number) to represent missing data in both DataFrames and Series.
# Like with a Series, Pandas assigns an index position/lable to each row in a DataFrame. This index can be used to access and manipulate the data in the DataFrame.
# DataFrame and Series have many methods and attributes in common. 
# This is because they both inherit from the same base class, which provides a lot of functionality that is shared between the two types of objects.
# The DataFrame and series have common and exclusive methods and attributes.
# The hasnans attribute only exists for Series, while the isna() method exists for both DataFrames and Series.
# Some methods and attributes will return different types of data.
# The info method returns a summary of the DataFrame, including the number of non-null values and the data types of each column.

import pandas as pd

# Create a DataFrame
nba = pd.read_csv('nba.csv')
# Display the first few rows of the DataFrame
print(nba.head())
# Display the last few rows of the DataFrame
print(nba.tail())
# Display the index of the DataFrame
print(nba.index)
# Display the columns of the DataFrame
print(nba.columns)
# Display the data types of each column in the DataFrame
print(nba.dtypes)
# Display the shape of the DataFrame
print(nba.shape)
# Display the info of the DataFrame
print(nba.info())

# The axes attribute returns the index and columns of the DataFrame as a list.
print(nba.axes)

