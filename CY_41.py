# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()
'''
Seaborn is an amazing visualization library for statistical graphics plotting in Python. 
It provides beautiful default styles and color palettes to make statistical plots more attractive.
It is built on the top of matplotlib library and also closely integrated to the data structures from pandas.
Seaborn aims to make visualization the central part of exploring and understanding data. 
It provides dataset-oriented APIs, so that we can switch between different visual representations
 for same variables for better understanding of dataset.
'''
'''
Different categories of plot in Seaborn 
Plots are basically used for visualizing the relationship between variables. 
Those variables can be either be completely numerical or a category like a group, class or division.

 Seaborn divides plot into the below categories –

 Relational plots: This plot is used to understand the relation between two variables.

# Relational plots are used for visualizing the statistical relationship between the data points.
 Visualization is necessary because it allows the human to see trends and patterns in the data. 
 The process of understanding how the variables in the dataset relate each other and their relationships are termed as Statistical analysis. 

Seaborn, unlike to matplotlib, also provides some default datasets. We will be using a default dataset named ‘tips’. This dataset gives information about people w
ho had food at some restaurant and whether they left tip for waiters or not, their gender and whether they do smoke or not, and more


 Categorical plots: This plot deals with categorical variables and how they can be visualized.
 Distribution plots: This plot is used for examining univariate and bivariate distributions
 Regression plots: The regression plots in seaborn are primarily intended to add a visual guide that 
                    helps to emphasize patterns in a dataset during exploratory data analyses
 Matrix plots: A matrix plot is an array of scatterplots.
 Multi-plot grids: It is an useful approach is to draw multiple instances of the same plot on different subsets of the dataset
 '''
# import seaborn as sns
# data=sns.load_dataset('tips')
# print(data.head())
#This dataset gives info for ppl who ate a t a restaurant and find whether the left the tip or not 

# To draw the relational plots seaborn provides three functions. These are:

# relplot()
# scatterplot()
# lineplot()

'''
#Seaborn.relplot()
This function provides us the access to some other different axes-level functions which
shows the relationships between two variables with semantic mappings of subsets.

Syntax : 
seaborn.relplot(x=None, y=None, data=None, **kwargs)
Parameter	Value	Use
x, y	numeric	Input data variables

Data	Dataframe	Dataset that is being used

hue, size, style	name in data; optional	Grouping variable that will produce elements with different colors.
kind	scatter or line; default : scatter	defines the type of plot, either scatterplot() or lineplot()
row, col	names of variables in data; optional	Categorical variables that will determine the faceting of the grid.
col_wrap	int; optional	“Wrap” the column variable at this width, so that the column facets span multiple rows.
row_order, col_order	lists of strings; optional	Order to organize the rows and columns of the grid.
palette	name, list, or dict; optional	Colors to use for the different levels of the hue variable.
hue_order	list; optional	Specified order for the appearance of the hue variable levels.
hue_norm	tuple or Normalize object; optional	Normalization in data units for colormap applied to the hue variable when it is numeric.
sizes	list, dict, or tuple; optional	determines the size of each point in the plot.
size_order	list; optional	Specified order for appearance of the size variable levels
size_norm	tuple or Normalize object; optional	Normalization in data units for scaling plot objects when the size variable is numeric.
legend	“brief”, “full”, or False; optional	If “brief”, numeric hue and size variables will be represented with a sample of evenly spaced values. 
                    If “full”, every group will get an entry in the legend. If False, no legend data is added and no legend is drawn.
height	scalar; optional	Height (in inches) of each facet.
Aspect	scalar; optional	Aspect ratio of each facet, i.e. width/height
facet_kws	dict; optional	Dictionary of other keyword arguments to pass to FacetGrid
kwargs	key, value pairings	Other keyword arguments are passed through to the underlying plotting function.
'''

# Example 1: Visualizing the most basic plot to show all the data points in tips dataset.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="darkgrid")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill", y ="tip", data = tips)
plt.show()

# Example 2: Grouping data points on the basis of category, here as time.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill",
            y="tip",
            hue="time",
            data=tips)
plt.show()


# Example 3: using time and sex for determining the facet of the grid.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", 
            y="tip",
            hue="day",
            col="time",
            row="sex",
            data=tips)
plt.show()
