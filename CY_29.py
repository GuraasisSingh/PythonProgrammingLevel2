# Json 

# import pandas as pd
# df = pd.read_json('H:/GURAASIS/Python Codeyoung/Level 2/data1.json')
# print(df.to_string())

# Dictionary as JSON
# JSON = Python Dictionary

# JSON objects have the same format as Python dictionaries

# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

# Load a Python Dictionary into a DataFrame:

'''import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)'''


# Data Cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# Example : 
# Return a new Data Frame with no empty cells:

import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
new_df = df.dropna()
print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:

# Example
# Remove all rows with NULL values:

import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
df.dropna(inplace = True)
print(df.to_string())