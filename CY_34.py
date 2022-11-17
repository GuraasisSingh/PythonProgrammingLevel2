# import pandas as pd      
# info = pd.DataFrame({"A":[8, 2, 7, 12, 6],   
#                    "B":[26, 19, 7, 5, 9],    
#                    "C":[10, 11, 15, 4, 3],   
#                    "D":[16, 24, 14, 22, 1]})     
# # Print the dataframe   
# print(info  )
# # If axis = 0 is not specified, then  by default method return the mean over  the index axis   
# print(info.mean(axis = 0))
'''
axis: {index (0), columns (1)}.
This refers to the axis for a function that is to be applied.

skipna: It excludes all the null values when computing result.

level: It counts along with a particular level and collapsing into a Series if the axis is a MultiIndex (hierarchical),
numeric_only: It includes only int, float, boolean columns. If None, it will attempt to use everything, then use only numeric data. Not implemented for Series.
'''

# import pandas as pd

# data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]

# df = pd.DataFrame(data)
# print(df)
# print(df.mean(axis=0))

# import pandas as pd

# data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]

# df = pd.DataFrame(data)
# print(df)
# print(df.sum(axis=0))

# Return the sum of each column:

# import pandas as pd

# data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]

# df = pd.DataFrame(data)

# print(df.sum())

'''
The sum() method adds all values in each column and returns the sum for each column.
By specifying the column axis (axis='columns'), the sum() method searches column-wise and returns the sum of each row.
dataframe.sum(axis, skipna, level, numeric_only, min_count, kwargs)
'''

'''
Parameters :
The axis, skipna, level, numeric_only, min_count, parameters are keyword arguments.

Parameter	Value	Description
axis

	0
1
'index'

'columns'	Optional, Which axis to check, default 0.

skip_na

	True
False
	Optional, default True. Set to False if the result should NOT skip NULL values

level	
Number
level name

	Optional, default None. Specifies which level ( in a hierarchical multi index) to check along

numeric_only

	None
True
False	

Optional. Specifies whether to only check numeric values. Default None

min_count	

None
True
False	

Optional. Specifies the minimum number of values that needs to be present to perform the action. Default 0

kwargs	 

	Optional, keyword arguments. These arguments has no effect, but could be accepted by a numpy function
'''
#args
# def adder(*num):
#     sum = 0
    
#     for n in num:
#         sum = sum + n

#     print("Sum:",sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)

#kwargs
# def intro(**data):
#     print("\nData type of argument:",type(data))

#     for key, value in data.items():
#         print("{} is {}".format(key,value))

# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

import pandas as pd

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]

df = pd.DataFrame(data)

print(df.min())