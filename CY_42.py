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

# seaborn.barplot() method
# A barplot is basically used to aggregate the categorical data according to some methods and by default it’s the mean. 
# It can also be understood as a visualization of the group by action. To use this plot we choose a categorical column for the x-axis and 
# a numerical column for the y-axis,
# and we see that it creates a plot taking a mean per categorical column.


'''
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
'''
# import seaborn as sns
# import matplotlib.pyplot as plt
 
# # read a titanic.csv file
# # from seaborn library

# df = sns.load_dataset('titanic')
 
# # who v/s fare barplot 
# sns.barplot(x = 'who',
#             y = 'fare',
#             data = df) 
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# # read a titanic.csv file
# # from seaborn library
# df = sns.load_dataset('titanic')
# sns.barplot(x = 'who',
#             y = 'fare',
#             palette='Blues',
#             estimator=np.median,
#             hue = 'class',
#             data = df)
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
sns.barplot(x='who',
            y = 'fare',
            data=df)
plt.show()


'''
 Pairplot

# The Seaborn Pairplot function allows the users to create an axis grid via which each numerical variable stored 
# in data is shared across the X- and Y-axis in the structure of columns and rows.
# We can create the Scatter plots in order to display the pairwise relationships in addition to the distribution plot displaying the data distribution in the column diagonally.

# The pairplot() function can also be used to showcase the subset of variables, or we can plot different types of variables on rows and columns.

import seaborn as sbn  
import matplotlib.pyplot as plt  
# loading the dataset using the seaborn library  
mydata = sbn.load_dataset('penguins')  
# pairplot with the hue = gender parameter  
sbn.pairplot(mydata, hue = 'gender')  
# displaying the plot  
plt.show()

Parameters of Pairplot function:

# data: The data parameter accepts the data depending on the visualization to be plotted. The values can be in terms of DataFrame, Array, or List of Arrays.

# hue_order, order: The hue_order or simply order parameter is the order for categorical variables utilized in the plot. The values for this parameter can be the lists of strings.

# scale: The scale parameter is used for scaling the plot. This parameter takes more than values for usage, such as area, count, or width.

# scale_hue: The scale_hue parameter takes the Boolean value in order to determine whether the scale is estimated within each level of the major grouping variable for TRUE or across all the violins on the plot for FALSE.

# gridsize: The gridsize parameter takes the integer value to calculate the kernel density for the plot.
# inner: The inner parameter allows the users to define the inner points of a violin plot. This parameter takes the values such as box, point, quartile, stick, or None.
# orient: The orient parameter allows the user to determine the plot's orientation. The orientation can be either vertical, denoted by 'v' or horizontal, denoted by 'h', respectively.

# linewidth: The linewidth parameter takes the float integer as its value to determine the width of the grey lines utilized within the plot.

# color: The color parameter allows the user to specify the range of color for all the data elements of the plot. The value for this parameter can be matplotlib color.

# palette: The palette parameter is used to define the colors utilized for each level of the plot with a variety of hues.

# ax: The ax parameter is used to define the axes on which the plot will be constructed. The value for this parameter can be matplotlib Axes.
'''