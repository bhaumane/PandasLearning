# The apply method applies a function to each element in a Series.
import pandas as pd

# Create a sample Series
data = pd.Series([1, 2, 3, 4, 5])

# Define a function to apply
def square(x):
    return x ** 2

# Apply the function to each element in the Series
squared_data = data.apply(square)

# Alternatively, you can use a lambda function for simple operations
squared_data_lambda = data.apply(lambda x: x ** 2)

# Display the results
print("Original data:")
print(data)
print("\nSquared data using the square function:")
print(squared_data)
print("\nSquared data using a lambda function:")
print(squared_data_lambda)

# Example with a more complex function
def categorize(x):
    if x < 3:
        return 'Low'
    elif x < 5:
        return 'Medium'
    else:
        return 'High'
    
categories = data.apply(categorize)
print("\nCategorized data:")
print(categories)