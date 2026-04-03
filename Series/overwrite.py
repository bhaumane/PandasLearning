# Overwrite a Series value in Pandas
# Use the loc/iloc indexers to overwrite values in a Series based on their index labels or integer positions, respectively.

import pandas as pd

# Create a sample Series
pokemon = pd.read_csv('pokemon.csv', index_col="Name").squeeze("columns")

# Overwrite a value using loc
pokemon.loc['Michael Brown'] = 'Mic'

# Overwrite a value using iloc
pokemon.iloc[1] = 'Bhaurao'

# Display the modified Series
print(pokemon)

