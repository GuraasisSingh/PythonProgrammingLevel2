# PAIR PLOTS :-

'''Explanation:

In the above example, we have imported the required libraries and load the data set of penguins t
o work with using the Seaborn load_dataset() function. We have then used the pairplot() function to visualize
 the plot with the hue parameter set to the value 'gender'. 
 At last, we have used the Matplotlib show() function to display the plot to the users.
 As a result, the pair plot has been generated successfully.'''

# import seaborn as sbn  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sbn.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sbn.pairplot(mydata, hue = 'species')  
# # displaying the plot  
# plt.show()

# import seaborn as sbn  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sbn.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sbn.pairplot(mydata, hue = 'species',diag_kind="hist")  
# # displaying the plot  
# plt.show()

# import seaborn as sbn  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sbn.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sbn.pairplot(mydata, hue = 'species',markers=["o", "s", "D"])  
# # displaying the plot  
# plt.show()


# import seaborn as sns  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sns.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sns.pairplot(mydata,x_vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"],y_vars=["bill_length_mm", "bill_depth_mm"],)# displaying the plot  
# plt.show()

# import seaborn as sns  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sns.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sns.pairplot(mydata, corner=True)
# plt.show()

# import seaborn as sns  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sns.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sns.pairplot(
#     mydata,
#     plot_kws=dict(marker="+", linewidth=1),
#     diag_kws=dict(fill=False),
# )
# plt.show()

# import seaborn as sns  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sns.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# g = sns.pairplot(mydata, diag_kind="kde")
# g.map_lower(sns.kdeplot, levels=4, color=".2")
# plt.show()

# import seaborn as sns  
# import matplotlib.pyplot as plt  
# # loading the dataset using the seaborn library  
# mydata = sns.load_dataset('penguins')  
# # pairplot with the hue = gender parameter  
# sns.pairplot(mydata, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='auto', markers=None, height=2.5, aspect=1,
# corner=False, dropna=False, plot_kws=None, diag_kws=None, grid_kws=None, size=None)
# plt.show()

'''
colors = iter(['xkcd:red purple', 'xkcd:pale teal', 'xkcd:warm purple',
       'xkcd:light forest green', 'xkcd:blue with a hint of purple',
       'xkcd:light peach', 'xkcd:dusky purple', 'xkcd:pale mauve',
       'xkcd:bright sky blue', 'xkcd:baby poop green', 'xkcd:brownish',
       'xkcd:moss green', 'xkcd:deep blue', 'xkcd:melon',
       'xkcd:faded green', 'xkcd:cyan', 'xkcd:brown green',
       'xkcd:purple blue', 'xkcd:baby shit green', 'xkcd:greyish blue'])

def my_scatter(x,y, **kwargs):
    kwargs['color'] = next(colors)
    plt.scatter(x,y, **kwargs)

def my_hist(x, **kwargs):
    kwargs['color'] = next(colors)
    plt.hist(x, **kwargs)

iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map_diag(my_hist)
g.map_offdiag(my_scatter)
'''

# import seaborn as sns
# import pandas as pd
# from matplotlib import pyplot as plt

# df = pd.read_csv('dataset.csv')

# g = sns.PairGrid(df)
# g.map_upper(sns.scatterplot,color='red')
# g.map_lower(sns.scatterplot, color='green')
# g.map_diag(plt.hist)

'''
Draw a single horizontal strip plot using Stripplot
If we use only one data variable instead of two data variables then it means that the axis denotes each of these data variables as an axis.

X denotes an x-axis and y denote a y-axis.

Syntax: 
seaborn.stripplot(x)

seaborn.pairplot() :
To plot multiple pairwise bivariate distributions in a dataset, you can use the .pairplot() function. 
The diagonal plots are the univariate plots, and this displays the relationship for the (n, 2) 
combination of variables in a DataFrame as a matrix of plots.
'''


# PAIR GRID
# Plot pairwise relationships in a dataset.

# By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.

# It is also possible to show a subset of variables or plot different variables on the rows and columns.

# This is a high-level interface for PairGrid that is intended to make it easy to draw a few common styles. You should use PairGrid directly if you need more flexibility.

# PairGrid
# Subplot grid for more flexible plotting of pairwise relationships.

# JointGrid
# Grid for plotting joint and marginal distributions of two variables.

# The simplest invocation uses scatterplot() for each pairing of the variables and histplot() for the marginal plots along the diagonal:
# Assigning a hue variable adds a semantic mapping and changes the default marginal plot to a layered kernel density estimate (KDE)
# The kind parameter determines both the diagonal and off-diagonal plotting style. Several options are available, including using kdeplot() to draw KDEs
# The markers parameter applies a style mapping on the off-diagonal axes. Currently, it will be redundant with the hue variable
# The plot_kws and diag_kws parameters accept dicts of keyword arguments to customize the off-diagonal and diagonal plots   ``
