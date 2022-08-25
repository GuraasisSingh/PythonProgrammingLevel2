'''
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
'''
'''
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
'''

# import pandas as pd
# print(pd.__version__)

# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# Create a simple Pandas Series from a list

'''
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
'''
# Labels
# If nothing else is specified, the values are labeled with their index number.
#  First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.


# Return the first value of the Series:
# print(myvar[0])
'''
Create Labels
With the index argument, you can name your own labels.

Example
Create you own labels:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)'''
# When you have created labels, you can access an item by referring to the label.

# Example
# Return the value of "y":
# print(myvar["y"])


# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.
# Example
# Create a simple Pandas Series from a dictionary:
# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

'''Note: The keys of the dictionary become the labels.

To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

Example
Create a Series using only data from "day1" and "day2":'''

'''import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)'''
# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.

# Example
# Create a DataFrame from two Series:

import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)


'''
# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.

# Pandas use the loc attribute to return one or more specified row(s)

# Example
# Return row 0:

#refer to the row index:
# print(df.loc[0])




# Note: When using [], the result is a Pandas DataFrame

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
# Note: This example returns a Pandas Series
# Example
# Return row 0 and 1:

#use a list of indexes:
print(df.loc[[0, 1]])
'''

# Named Indexes
# With the index argument, you can name your own indexes.

# Example
# Add a list of names to give each row a name:

'''import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).

# Example
# Return "day2":

#refer to the named index:
print(df.loc["day2"])'''



# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# Example
# Load a comma separated file (CSV file) into a DataFrame:

'''import pandas as pd

df = pd.read_csv('auto-mpg (1).csv')

print(df)'''


'''# Load the CSV into a DataFrame:

import pandas as pd

df = pd.read_csv('auto-mpg (1).csv')

print(df.to_string())'''

'''Tip: use to_string() to print the entire DataFrame.

If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

Example
Print the DataFrame without the to_string() method:

import pandas as pd

df = pd.read_csv('auto-mpg (1).csv')

print(df)'''


# max_rows
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows with the pd.options.display.max_rows statement.

# Example
# Check the number of maximum returned rows:

'''import pandas as pd

print(pd.options.display.max_rows)'''

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# 
# You can change the maximum rows number with the same statement.


# Example
# Increase the maximum number of rows to display the entire DataFrame:

'''import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('auto-mpg (1).csv')

print(df)'''


# Pandas - Analyzing DataFrames
# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

# Example
# Get a quick overview by printing the first 10 rows of the DataFrame:

'''import pandas as pd

df = pd.read_csv('auto-mpg (1).csv')

print(df.head(10))'''


'''# Note: if the number of rows is not specified, the head() method will return the top 5 rows.

# Example
# Print the first 5 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('auto-mpg (1).csv')

print(df.head())'''

# There is also a tail() method for viewing the last rows of the DataFrame.

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

# Example
# Print the last 5 rows of the DataFrame:
import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
print(df.tail())


# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.

# Example
# Print information about the data:

print(df.info())


# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, 
# and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with
#  empty values. This is a step towards what is called cleaning data
# 
# Data Cleaning
# Python Json File Read