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

"""import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
new_df = df.dropna()
print(new_df.to_string())"""

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:

# Example
# Remove all rows with NULL values:

"""import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
df.dropna(inplace = True)
print(df.to_string())"""

# Replace Empty Values :

# inplace: It is a boolean which makes the changes in data frame itself if True.
# The dropna() function is used to remove missing values.

# Pandas DataFrame dropna() function is used to remove rows and columns with Null/NaN values. 
# By default, this function returns a new DataFrame and the source DataFrame remains unchanged.

# inplace: a boolean value. If True, the source DataFrame is changed and None is returned.

# dropna(self, axis=0, how="any", thresh=None, subset=None, inplace=False)

# axis: possible values are {0 or ‘index’, 1 or ‘columns’}, default 0. If 0, drop rows with null values. 
# If 1, drop columns with missing values.

# how: possible values are {‘any’, ‘all’}, default ‘any’. If ‘any’, drop the row/column if any of the values is null. If ‘all’, 
# drop the row/column if all the values are missing.

# thresh: an int value to specify the threshold for the drop operation.
# subset: specifies the rows/columns to look for null values.

# axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String.
# how: how takes string value of two kinds only (‘any’ or ‘all’). ‘any’ drops the row/column if ANY value is Null and ‘all’ drops only if ALL values are null.
# thresh: thresh takes integer value which tells minimum amount of na values to drop.
# subset: It’s an array which limits the dropping process to passed rows/columns through list.
# inplace: It is a boolean which makes the changes in data frame itself if True.

# DataFrameName.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

'''import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
d= df.dropna(axis=0, how='any')
print("Old dataframe length",len(df),"New dataframe Length",len(d),'\n',"Number of rows with atleast one null value",(len(df)-len(d)))'''

#Hw-> 
# Use dropna(), 
# drop all rows with any null values,
# drop all the columns with any missing value,
# drop row/column only if all the vaalues are null
# drop all the rows/columns when threshhold of null values is crossed
# define the labels to look for null values
# dropping rows with null in place


# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

# Example
# Replace NULL values with the number 130:

# import pandas as pd
# df = pd.read_csv('data.csv')
# df.fillna(130, inplace = True)



'''import pandas as pd 
data = { 
    "One": { 
        "0": 60, 
        "1": 60, 
        "2": 60, 
        "3": 45, 
        "4": 45, 
        "5": 60
    }, 
    "Two": { 
        "0": 110, 
        "1": 117, 
        "2": 103, 
        "3": 109, 
        "4": 117, 
        "5": 102
    } 
} 
df = pd.DataFrame(data)
print(df)'''