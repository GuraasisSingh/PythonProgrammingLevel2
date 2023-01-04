
#Swarm Plot
# Syntax:
# seaborn.swarmplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, dodge=False, orient=None, color=None, palette=None, size=5, edgecolor=’gray’, linewidth=0, ax=None, **kwargs)
# Parameters: 
# x, y, hue: Inputs for plotting long-form data. 
# data: Dataset for plotting. 
# color: Color for all of the elements 
# size: Radius of the markers, in points.

# Example 1: Basic visualization of “fmri” dataset using swarmplot()
'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")
seaborn.swarmplot(x="timepoint", y="signal",data=fmri)
plt.show()'''
# Example 2: Grouping data points on the basis of category, here as region and event.
'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")
seaborn.swarmplot(x="timepoint",y="signal", hue="region",
data=fmri)
plt.show()'''
# Example 3: Basic visualization of “tips” dataset using swarmplot()
'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tip = seaborn.load_dataset('tips')
seaborn.swarmplot(x='day', y='tip', data=tip)
plt.show()'''

# Grouping variables in Seaborn Swarmplot with different attributes :

# 1. Draw a single horizontal swarm plot using only one axis:

# If we use only one data variable instead of two data variables then it means that the axis denotes each of these data variables as an axis.

# X denotes an x-axis and y denote a y-axis.

# Syntax: 
# seaborn.swarmplot(x)
'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style="whitegrid")
fmri = seaborn.load_dataset("fmri")
seaborn.swarmplot(x="timepoint", y="signal",data=fmri)
plt.show()'''

# Seaborn swarmplot is probably similar to stripplot, only the points are adjusted so it won’t 
# get overlap to each other as it helps to represent the better representation of the distribution of values.
# A swarm plot can be drawn on its own, but it is also a good complement to a box, preferable because 
# the associated names will be used to annotate the axes. This type of plot sometimes known as “beeswarm”.

# Syntax: seaborn.swarmplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, dodge=False, orient=None, color=None, palette=None, size=5, edgecolor=’gray’, linewidth=0, ax=None, **kwargs)
'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")
seaborn.swarmplot(x="timepoint",y="signal",hue="region",data=fmri)
plt.show()'''
# Parameters: 
# x, y, hue: Inputs for plotting long-form data. 
# data: Dataset for plotting. 
# color: Color for all of the elements 
# size: Radius of the markers, in points.
'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tip = seaborn.load_dataset('tips')
seaborn.swarmplot(x='day', y='tip', data=tip)
plt.show()'''

'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tip = seaborn.load_dataset('tips')
seaborn.swarmplot(y='day', x='tip', hue='time',data=tip)
plt.show()'''

# Using hue parameter:
# While the points are plotted in two dimensions, another dimension can be added to the plot by coloring the points according to a third variable.
# Syntax:
# sns.swarmplot(x, y, hue, data)
# seaborn.swarmplot(x="day", y="total_bill", hue="time", data=tips)

# 4. Draw outlines around the data points using linewidth:
# Width of the gray lines that frame the plot elements. Whenever we increase linewidth than the point also will increase automatically.
# Syntax:
# seaborn.swarmplot(x, y, data, linewidth)

'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tips = seaborn.load_dataset('tips')
seaborn.swarmplot(y="total_bill", x="day", data=tips, linewidth=2,edgecolor='green')
plt.show()'''


# Draw each level of the hue variable at different locations on the major categorical axis:
# When using hue nesting, setting dodge should be True will separate the point for different hue levels along the categorical axis. And Palette is used for the different levels of the hue variable.
# Syntax:
# seaborn.stripplot(x, y, data, hue, palette, dodge)
'''
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tips = seaborn.load_dataset('tips')
seaborn.swarmplot(x="day", y="total_bill", hue="smoker",
                   data=tips, palette="Set2", dodge=False)
plt.show()
'''

# 6. Plotting large points and different aesthetics With marker and alpha parameter:

# We will use alpha to manage transparency of the data point, and use marker for marker to customize the data point. 

'''
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tips = seaborn.load_dataset('tips')
seaborn.swarmplot(x="day", y="total_bill", hue="smoker",
data=tips, palette="Set2", size=20, marker="D",edgecolor="gray", alpha=.25)
plt.show()'''
# alpha is for setting opaqueness
# marker is for shape
# size will set the size

# Control swarm order by passing an explicit order:

# seaborn.swarmplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])

'''import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='whitegrid')
tips = seaborn.load_dataset('tips')
seaborn.swarmplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])
plt.show()'''


# Adding size attributes.
# Using size we can generate the point and we can produce points with different sizes.
# seaborn.swarmplot( x, y, data, size)


# Adding the palette attributes:
# Using the palette we can generate the point with different colors. In this below example we can see the palette can be responsible for a generate the swarmplot with different colormap values.
# Syntax:
# seaborn.swarmplot( x, y, data, palette=”color_name”)

##################################################################################################################################################################################################################
# COUNT PLOT ::