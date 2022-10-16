'''
#Isnull method
import pandas as pd
df = pd.read_csv('data (3).csv')
newdf=df.isnull()
print(newdf.to_string())'''
'''#Not null
import pandas as pd
d=pd.read_csv('data (3).csv')
nd=d.notnull()
print(nd.to_string())'''

'''
- unique()
- value_counts
- mean, sum, min, max
- sorting
- selecting rows based on multiple conditions
columns and index
- info, describe
-dtypes
-astype
'''

# The unique() function is used to get unique values of Series object.

# Uniques are returned in order of appearance. Hash table-based unique, therefore does NOT sort.

# The unique() function returns :


# The unique values returned as a NumPy array
# The value_counts() function is used to get a Series containing counts of unique values.
# The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.
# The value_count() function returns :
# series

'''
import numpy as np
arr = np.array(42)
print(arr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
'''


'''import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
'''
#Unique

# import numpy as np
# a=[1,23,3,5,7,1,23]
# an=np.unique(a)
# print(an)

# import pandas as pd
# a=pd.Index(['aman', "dhanush","rohit","rohan","aman","rohit","rohan"],name="student")
# print(a)
# print(a.value_counts())

#####Hw-> Do the same for numbers......//


# Mean, Median, and Mode:

# Mean - The average value
# Median - The mid point value
# Mode - The most common value
'''
import pandas as pd
data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.mean())

import pandas as pd
data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.mode())

import pandas as pd
data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.median())

import pandas as pd
data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.max())

import pandas as pd 
df = pd.DataFrame({"A":[12, 4, 5, 44, 1], 
                   "B":[5, 2, 54, 3, 2],  

                   "C":[20, 16, 7, 3, 8], 

                   "D":[14, 3, 17, 2, 6]}) 
print(df)
'''
'''
# Get the first element from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])



# Get the second element from the following array.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])



# Get third and fourth elements from the following array and add them.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


# Access the element on the first row, second column:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])



# Access the element on the 2nd row, 5th column:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])



# Access the third element of the second array of the first array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])



 Print the last element from the 2nd dim:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
 We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

Slicing arrays.
Slice elements from index 1 to index 5 from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

Note: The result includes the start index, but excludes the end index.
 Slice elements from index 4 to the end of the array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])
 Slice elements from the beginning to index 4 (not included):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])
 Slice from the index 3 from the end to index 1 from the end:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
 Use the step value to determine the step of the slicing:

Example
Return every other element from index 1 to index 5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
 Return every other element from the entire array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

'''


# You can check dimensions of array.

# mean() function:
# Just like the name suggests, the mean method will return the mean value of each column

# sum() function:
# the sum method will reflect the sum of all the values in the specified column

# min() function:
# the min method will reflect the min of all the values in the specified column

# max() function:
# the max method will reflect the max of all the values in the specified column


# To sort a dataframe, we use the .sort_values() method. It is important to specify the column by which we have to sort.

# Don’t forget to use inplace attribute

# Example :
# df8.sort_values(by='distance',inplace=True)
# df8




# We can select rows based on multiple conditions by passing them inside the data frame as shown below.

# For example, lets select all rows that are not green and which don’t belong to customer 105
# new_df = df8[(df8['customer']!='105') & (df8['color']!='green')]
# new_df




# .columns will return all the names of the columns in the dataframe

# df8.columns

# Index(['customer', 'color', 'distance', 'sales'], dtype='object')

# .index will return the label/ values of the index column

# df8.index

# Int64Index([4, 5, 6, 7], dtype='int64')




# CUSTOM FUNCTION :

# We might want to make certain changes to a certain column or the entire dataframe. To do the same set of operations, we will first define the function just like any normal python function.

# To apply the function to a particular column, we use the .apply() method
# To apply the function to the entire dataframe, we use the applymap() method

# Example : 

# def profit(s):
#     return s*0.5 

# # we have created a function to calculate profits, assuming a 50% markup...
# df8['sales'].apply(profit)