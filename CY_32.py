#Data Wrong Format

'''
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
'''

'''
Convert Into a Correct Format :

In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:

Let's try to convert all cells in the 'Date' column into dates.

Pandas has a to_datetime() method for this:
'''

'''One way to deal with empty values is simply removing the entire row.

Removing Rows :

The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.'''
# import pandas as pd
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())

'''
Remove rows with a NULL value in the "Date" column:

df.dropna(subset=['Date'], inplace = True)
'''

# import pandas as pd
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace = True)
# print(df.to_string())

# import pandas as pd
# df = pd.read_csv('Samplecsvdatafile.csv')
# print(df.duplicated())

# import pandas as pd
# df = pd.read_csv('Samplecsvdatafile.csv')
# df.drop_duplicates(inplace = True)
# print(df.to_string())

'''Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame,
 but it will remove all duplicates from the original DataFrame.'''

#  Finding Relationships
# A great aspect of the Pandas module is the corr() method.

# The corr() method calculates the relationship between each column in your data set.

'''
import pandas as pd
df = pd.read_csv('data (3).csv')
print(df.corr())

# Note: The corr() method ignores "not numeric" columns.

import pandas as pd
df = {
  "Array_1": [30, 70, 100],

  "Array_2": [65.1, 49.50, 30.7]
}

data = pd.DataFrame(df)
print(data.corr())

'''
'''
Result Explained
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will
'''

'''
What is a good correlation? It depends on the use, 
but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation
'''
'''
Perfect Correlation:
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, 
each column always has a perfect relationship with itself.'''

'''
Good Correlation:
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation,
 and we can predict that the longer you work out, the more calories you burn, 
 and the other way around: if you burned a lot of calories,
 you probably had a long work out.
'''

'''
Bad Correlation:
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse 
by just looking at the duration of the work out, and vice versa.'''

'''
The correlation coefficient is calculated by first determining the covariance 
of the variables and then dividing that quantity by the product of those variables' 
standard deviations
'''
# In statistical terms we use correlation to denote association between two quantitative variables.


'''
Find the correlation (relationship) between each column in the DataFrame:

import pandas as pd

data = {
  "Duration": [50, 40, 45],
  "Pulse": [109, 117, 110],
  "Calories": [409.1, 479.5, 340.8]
}

df = pd.DataFrame(data)

print(df.corr())'''

# method	'kendall'
# 'pearson'
# 'spearman'
# func	Optional, Default pearson. Specifies which method to use, or a callable function.

# min_periods	Number	Optional.
# Specifies the minimum number of observations required to return a good enough result





#Matplotlib

#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()