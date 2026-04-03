# Broadcasting utilities for Series.
# Broadcasting describes the process of applying an arthmetic operations to an array i.e. Series.
# We can combine mathematical operations with a Series to apply the mathematical operation to every value.
# There are also methods to accomplish this, such as add, sub, mul, div, etc. 

import pandas as pd
# Create a sample Series
stock_prices = pd.read_csv('stocksinfo.csv', usecols=['Value']).squeeze("columns")

# Add a constant value to each element in the Series
# added_series = stock_prices + 10
added_series = stock_prices.add(10)

# Subtract a constant value from each element in the Series
subtracted_series = stock_prices.sub(5)

# Multiply each element in the Series by a constant value
multiplied_series = stock_prices.mul(2)

# Divide each element in the Series by a constant value
divided_series = stock_prices.div(2)

# Display the original Series and the modified Series
print("Original Series:")
print(stock_prices)
print("\nSeries after adding 10:")
print(added_series)
print("\nSeries after subtracting 5:")
print(subtracted_series)
print("\nSeries after multiplying by 2:")
print(multiplied_series)
print("\nSeries after dividing by 2:")
print(divided_series)