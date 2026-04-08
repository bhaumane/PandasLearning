# Select one or more columns from a DataFrame
# We can use attribute syntax (df.column_name) to select a single column from a DataFrame. 
# The syntax will not work if the column name has spaces or special characters, or if the column name is the same as a DataFrame method.
# We can also use the indexing operator (df['column_name']) to select a single column from a DataFrame.
# Pandas extracts a column from a DataFrame as a Series. The resulting Series will have the same name as the column and the same index as the DataFrame.
# The Series is a view, so changes to the Series will affect the original DataFrame. To avoid this, we can use the copy() method to create a copy of the Series.
# Pandas will display a warning if you mutate the Series. This is because it can lead to unexpected behavior if you are not aware that the Series is a view of the original DataFrame.
# Use square brackets to select multiple columns from a DataFrame. The syntax is df[['column_name1', 'column_name2', ...]].
# Pandas will return a new DataFrame containing only the selected columns. The resulting DataFrame will have the same index as the original DataFrame and the selected columns as its columns.

import pandas as pd

# Create a DataFrame
nba = pd.read_csv('nba.csv')
# Select a single column using attribute syntax
team = nba.Team
print(team)
# Select a single column using indexing operator
team = nba['Team']
print('Display the team column:')
print(team)
# Select multiple columns using indexing operator
team_and_position = nba[['Team', 'Position']]
print('Display the team and position columns:')
print(team_and_position)
# Select a single column and create a copy of the Series
team_copy = nba['Team'].copy()
print('Display the copied team column:')
print(team_copy)
# Mutate the Series and see the warning
team_copy[0] = 'New Team Name'
print('Display the mutated team column:')
print(team_copy)
# Display the original team column to see if it has been affected by the mutation
print('Display the original team column to see if it has been affected by the mutation:')
print(nba['Team'])
