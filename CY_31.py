# If you want to change the original DataFrame, use the inplace = True argument:

# Example
# Remove all rows with NULL values:
'''
import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(inplace = True)
print(df.to_string())
'''
# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

# Example
# Replace NULL values with the number 130:

'''import pandas as pd
df = pd.read_csv('auto-mpg (1).csv')
df.fillna(130, inplace = True)
print(df.to_string())'''

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.

# To only replace empty values for one column, specify the column name for the DataFrame:

# Example
# Replace NULL values in the "Calories" columns with the number 130:
'''
import pandas as pd
df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)
df["Pulse"].fillna(10, inplace = True)
print(df.to_string())'''

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean,
#  median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Example
# Calculate the MEAN, and replace any empty values with it:

'''import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())'''

# Mean = the average value (the sum of all values divided by number of values).

# Example
# Calculate the MEDIAN, and replace any empty values with it:
'''
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())'''

# Median = the value in the middle, after you have sorted all values ascending.

# Example
# Calculate the MODE, and replace any empty values with it:
'''
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
'''
# Mode = the value that appears most frequently
'''
from os import access
import pandas as pd
df=pd.DataFrame({"A":[12,67,43,87,32],"B":[45,76,89,32,43],"C":[24,75,69,47,36]},"D":[32,65,48,92,43])
print(df)
print(df.median(axis=0))'''