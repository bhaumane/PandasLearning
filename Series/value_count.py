# The value_count method counts the number of occurrences of each unique value in a Series. 
# It returns a Series containing counts of unique values. The resulting Series is sorted by the values in descending order.
# The normalize parameter, if set to True, will return the relative frequencies of the unique values instead of their counts.
import pandas as pd

# Example usage:
data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
value_counts = data.value_counts()
print(value_counts)

# Output:
# apple     3
# banana    2
# orange    1

# Example with normalize=True:
relative_frequencies = data.value_counts(normalize=True)
print(relative_frequencies)
# Output:
# apple     0.5
# banana    0.333333
# orange    0.166667