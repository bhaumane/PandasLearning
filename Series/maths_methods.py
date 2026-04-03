# Math Methods of Series objects in Pandas
# Count: The count method in Pandas Series is used to count the number of non-null values in a Series. 
#        It excludes any missing values (NaN) from the count, providing an accurate count of valid entries in the Series.
# Sum: The sum method in Pandas Series is used to calculate the total sum of the values in a Series.
# Mean: The mean method in Pandas Series is used to calculate the average of the values in a Series.
# Median: The median method in Pandas Series is used to calculate the median (the middle value) of the values in a Series.
# Mode: The mode method in Pandas Series is used to calculate the mode (the most frequently occurring value) of the values in a Series.
# Min: The min method in Pandas Series is used to find the minimum value in a Series.
# Max: The max method in Pandas Series is used to find the maximum value in a Series.
# Std: The std method in Pandas Series is used to calculate the standard deviation of the values in a Series, which measures the amount of variation or dispersion in the data.
# Var: The var method in Pandas Series is used to calculate the variance of the values in a Series, which measures the average squared deviation from the mean.
# Describe: The describe method in Pandas Series is used to generate descriptive statistics of the values in a Series, including count, mean, standard deviation, minimum, maximum, and quartiles. It provides a summary of the distribution of the data in the Series.
# Product: The product method in Pandas Series is used to calculate the product of the values in a Series, which is the result of multiplying all the values together. This method can be useful for calculating the total product of a series of numbers, such as in financial calculations or when working with probabilities.
import pandas as pd

# Create a sample Series
stock_prices = pd.read_csv('stocksinfo.csv', usecols=['Value']).squeeze("columns")

# Calculate the count of non-null values in the Series
count_non_null = stock_prices.count()

# Calculate the sum of the values in the Series
sum_values = stock_prices.sum()

# Calculate the mean of the values in the Series
mean_value = stock_prices.mean()

# Calculate the median of the values in the Series
median_value = stock_prices.median()

# Calculate the mode of the values in the Series
mode_value = stock_prices.mode()

# Calculate the minimum value in the Series
min_value = stock_prices.min()

# Calculate the maximum value in the Series
max_value = stock_prices.max()

# Calculate the standard deviation of the values in the Series
std_value = stock_prices.std()

# Calculate the variance of the values in the Series
var_value = stock_prices.var()

# Generate descriptive statistics of the values in the Series
describe_stats = stock_prices.describe()

# Calculate the product of the values in the Series
product_value = stock_prices.product()

# Display the calculated values
print("Count of non-null values in the Series:", count_non_null)
print("Sum of the values in the Series:", sum_values)
print("Mean of the values in the Series:", mean_value)
print("Median of the values in the Series:", median_value)
print("Mode of the values in the Series:", mode_value)
print("Minimum value in the Series:", min_value)
print("Maximum value in the Series:", max_value)
print("Standard deviation of the values in the Series:", std_value)
print("Variance of the values in the Series:", var_value)
print("Descriptive statistics of the values in the Series:")
print(describe_stats)
print("Product of the values in the Series:", product_value)