'''# Example 4: using size attribute, we can see data points having different size.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", 
            y="tip",
            hue="day",
            size="size",
            data=tips)
plt.show()


# Example 1: Using relplot() to visualize tips dataset
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill", y ="tip", data = tips)
plt.show()

# Example 2: Using relplot() with kind=”scatter”.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill",
            y ="tip",
            kind ="scatter",
            data = tips)
plt.show()

# Example 3: Using relplot() with kind=”line”.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill",
            y ="tip",
            kind ="line",
            data = tips)
plt.show()'''

# Though both these plots can be drawn using relplot(),
# seaborn also have separate functions for visualizing these kind of plots. 
# These functions do provides some other functionalities too, compared to relplot().


# Seaborn.lineplot()
# Scatter plots are highly effective, but there is no universally optimal type of visualization. 
# For certain datasets, you may want to consider changes as a function of time in one variable, or as a similarly continuous variable.
#  In this case, drawing a line-plot is a better option.

# Syntax :  

# seaborn.lineplot(x=None, y=None, data=None, **kwargs)
'''
# # Example 1: Basic visualization of “fmri” dataset using lineplot()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'whitegrid')
fmri = sns.load_dataset("fmri")
sns.lineplot(x ="timepoint",
             y ="signal",
             data = fmri)
plt.show()

# Example 2: Grouping data points on the basis of category, here as region and event. 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'whitegrid')
fmri = sns.load_dataset("fmri")
sns.lineplot(x ="timepoint",
             y ="signal",
             hue ="region",
             style ="event",
             data = fmri)
plt.show()
'''
# Example 3: A complex plot visualizing “dots” dataset, to show the power of seaborn. Here, in this example, quantitative color mapping is used. 
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(style = 'whitegrid')
# dots = sns.load_dataset("dots").query("align == 'dots'")
# sns.lineplot(x ="time", 
#              y ="firing_rate",
#              hue ="coherence",
#              style ="choice",
#              data = dots)
# plt.show()


#  Categorial Plots: 
# Barplot
# A barplot is basically used to aggregate the categorical data according to some methods and by default its the mean. It can also be understood a
# s a visualization of the group by action. To use this plot we choose a categorical column for the x axis and a numerical column for the y axis and 
# we see that it creates a plot taking a mean per categorical column. 

# Syntax:  

# barplot([x, y, hue, data, order, hue_order, …])


import matplotlib.pyplot as plt
import seaborn as sns
#import done to avoid warnings 
from warnings import filterwarnings
# reading the dataset
df = sns.load_dataset('tips')
# first five entries if the dataset
df.head()
# set the background style of the plot
sns.set_style('darkgrid')
# plot the graph using the default estimator mean
sns.barplot(x ='sex', y ='total_bill', data = df, palette ='plasma')
# or
import numpy as np
# change the estimator from mean to standard deviation
sns.barplot(x ='sex', y ='total_bill', data = df, 
            palette ='plasma', estimator = np.std)
plt.show()