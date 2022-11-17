# CUSTOM FUNCTION :

# We might want to make certain changes to a certain column or the entire dataframe. To do the same set of operations, we will first define the function just like any normal python function.

# To apply the function to a particular column, we use the .apply() method
# To apply the function to the entire dataframe, we use the applymap() method

# Example : 

# def profit(s):
#     return s*0.5 

# # we have created a function to calculate profits, assuming a 50% markup...
# df8['sales'].apply(profit)

'''
map works element-wise on a series, and is optimized for mapping values to a series (e.g. one column of a DataFrame).

applymap works element-wise on a DataFrame, and is optimized for mapping values to a DataFrame.

apply works on both series and DataFrames, but it’s relatively slow and should only be used if you’re running out of other options.
'''
# Map :
'''import pandas as pd
import numpy as np
df = pd.DataFrame([[1, 2, 'cat', []]
    ,[3, 4, 'dog', [1,2,3]]
    ,[5, 1, np.nan, [3,5,5]]], columns=['A', 'B', 'C', 'D'])
print(df)
df['C'] = df['C'].map({'cat': 'kitten', 'dog': 'puppy'})
print(df)'''

# import pandas as pd
# import numpy as np
# df = pd.DataFrame([[1, 2, 'cat', []]
#     ,[3, 4, 'dog', [1,2,3]]
#     ,[5, 1, np.nan, [3,5,5]]], columns=['A', 'B', 'C', 'D'])
# print(df)
# df['C'] = df['C'].map({'cat': 'kitten', 'dog': 'puppy'})
# df['C'] = df['C'].map(lambda x: 'unknown' if x is np.NaN else x.upper())
# print(df)
'''
import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 'cat', []]
     ,[3, 4, 'dog', [1,2,3]]
     ,[5, 1, np.nan, [3,5,5]]], columns=['A', 'B', 'C', 'D'])
print(df)

def get_avg_rating(lst):
    if len(lst) == 0:
        return np.nan
    else:
        return round(sum(lst) / len(lst), 1)

df['D'] = df['D'].map(get_avg_rating)      
print(df)
'''

# Applymap :

# applymap only applies in the rare cases where you’d like to perform an element-wise mapping 
# operation to an entire DataFrame (or select columns of a DataFrame).
'''
import pandas as pd
df = pd.DataFrame([[2, 3.12], [4.356, 5.567]])
df.applymap(lambda x: len(str(x)))
print(df)
df.applymap(lambda x: x**2)
print(df**2)
'''
# Apply :

# apply comes in handy when you’d like to apply custom mapping/logic among multiple columns or rows of a dataset. 
# Again, let’s start with a simple lambda function where we subtract column B from column A if column C is not unknown:


# axis=1 tells apply to work column-wise. We can also use apply row-wise to get things like column max values:

# 

# apply is very flexible and it can help us apply built-in functions such as tuple:

# df['T'] = df[['A', 'B']].apply(tuple, axis=1)


# import pandas as pd
# import numpy as np
# df = pd.DataFrame([[1, 2, 'cat', []]
#     ,[3, 4, 'dog', [1,2,3]]
#     ,[5, 1, np.nan, [3,5,5]]], columns=['A', 'B', 'C', 'D'])
# df[['A', 'B']].apply(lambda x: x.max(), axis=0)
# print(df)
# df['A-B'] = df.apply(lambda x: x.A - x.B if x.C != 'unknown' else np.nan, axis=1)
# print(df)


# Lastly, let’s apply a predefined custom function (note that x within the lambda function refers to the DataFrame df):

def task_helper(a, b):
    d = {}
    d[a] = b
    return d
df['task'] = df.apply(lambda x: task_helper(x['C'], x['T']), axis=1)