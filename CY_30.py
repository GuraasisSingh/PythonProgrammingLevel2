# import pandas as pd
# import numpy as np

# d1={"Name":["Guraasis","Aryaansh","Dinesh",pd.NaT],
# 'ID':[1,2,pd.NaT,pd.NaT],
# "Salary":[100,200,np.nan,pd.NaT],
# "Role":[np.nan,np.nan,pd.NaT,pd.NaT]}

# df=pd.DataFrame(d1)

# print(df)
# df1=df.dropna(thresh=2)
# print(df1)

'''NaT
If a column is a DateTime and you have a missing value, then that value will be a NaT. NaT stands for Not a Time.

None
A pandas object dtype column - the dtype for strings as of this writing - can hold None, NaN, NaT or all three at the same time!'''
'''

What are these NaN values anyway?
NaN is a NumPy value. np.NaN
NaT is a Pandas value. pd.NaT
None is a vanilla Python value. None

'''
'''
NaN, NaT, and None
NaN
If a column is numeric and you have a missing value that value will be a NaN. NaN stands for Not a Number.

NaNs are always floats. So if you have an integer column and it has a NaN added to it, the column is upcasted to become a float column. 
This behavior may seem strange, but it is based on NumPy's capabilities as of this writing.
 In general, floats take up very little space in memory, so pandas decided to treat them this way.'''

# import pandas as pd
# import numpy as np
# # S=pd.Series([np.NaN, pd.NaT, None]).astype('object')
# # print(S)



# import pandas as pd
# import numpy as np
# d1=(np.nan,pd.NaT,None)
# df=pd.DataFrame(d1)
# print(df)


# import pandas as pd
# import numpy as np
# s = pd.Series(['1.0', '2', -3])
# print(pd.to_numeric(s))

# format:
# pandas.to_numeric(arg, errors='raise', downcast=None)


# import pandas as pd
# import numpy as np
# s = pd.Series(['1.0', '2', -3])
# print(pd.to_numeric(s, downcast='float'))
# print(pd.to_numeric(s, downcast='signed'))#->int
# print(pd.to_numeric(s, downcast='integer'))

# import pandas as pd
# import numpy as np
# s = pd.Series(['apple', '1.0', '2', -3])
# print(pd.to_numeric(s, errors='ignore'))
# print(pd.to_numeric(s, errors='coerce'))
# # print(pd.to_numeric(s, errors='raise'))->returns error


# errors{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
# If ‘raise’, then invalid parsing will raise an exception.

# If ‘coerce’, then invalid parsing will be set as NaN.

# If ‘ignore’, then invalid parsing will return the input.


import pandas as pd
s = pd.Series(['apple', '1.0', '2', -3])
pd.to_numeric(s,errors='ignore')