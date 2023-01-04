# Draw a single horizontal strip plot using Stripplot
# If we use only one data variable instead of two data variables then it means that the axis denotes each of these data variables as an axis.

# X denotes an x-axis and y denote a y-axis.

# Syntax: 
# seaborn.stripplot(x)
'''
import seaborn 
import matplotlib.pyplot as plt 
seaborn.set(style = 'whitegrid') 
tips = seaborn.load_dataset("tips") 
seaborn.stripplot(x=tips["total_bill"])
plt.show()'''

# Draw strip plot using jitter parameter
# jitter can be used to provide displacements along the horizontal axis, which is useful when there are large clusters of data points. You can specify the amount of jitter (half the width of the uniform random variable support), or just use True for a good default.

# Syntax:
# seaborn.stripplot(x, y, data, jitter)
'''import seaborn 
import matplotlib.pyplot as plt 
seaborn.set(style = 'whitegrid') 
tips = seaborn.load_dataset("tips") 
seaborn.stripplot(x="day", y="total_bill", data=tips, jitter=0.1)
plt.show()'''
# Draw outlines around the data points using linewidth
# Width of the gray lines that frame the plot elements. Whenever
# we increase linewidth than the point also will increase automatically.
'''import seaborn 
import matplotlib.pyplot as plt 
seaborn.set(style = 'whitegrid') 
tips = seaborn.load_dataset("tips") 
seaborn.stripplot(y="total_bill", x="day", data=tips, linewidth=3)
plt.show()'''
'''
A Box Plot is also known as Whisker plot is created to display the 
summary of the set of data values having properties like minimum, first quartile,
 median, third quartile and maximum. In the box plot, a box is created from the 
 first quartile to the third quartile, a vertical line is also there which goes 
 through the box at the median. Here x-axis denotes
 the data to be plotted while the y-axis shows the frequency distribution.
'''
# Syntax:
# matplotlib.pyplot.boxplot(data, notch=None, vert=None, patch_artist=None, widths=None)

'''import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
np.random.seed(10)
 
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
fig = plt.figure(figsize =(10, 7))
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
# Creating plot
bp = ax.boxplot(data)
# show plot
plt.show()'''
# Example 2: Let’s try to modify the above plot with some of the customizations: 

# Import libraries
'''import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
colors = ['#0000FF', '#00FF00', 
          '#FFFF00', '#FF00FF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
for whisker in bp['whiskers']:
    whisker.set(color ='blue',
                linewidth = 1.5,
                linestyle =":")
for cap in bp['caps']:
    cap.set(color ='red',
            linewidth = 2)
for median in bp['medians']:
    median.set(color ='black',
               linewidth = 3)
for flier in bp['fliers']:
    flier.set(marker ='D',

              color ='yellow',

              alpha = 0.5)
ax.set_yticklabels(['data_1', 'data_2', 
                    'data_3', 'data_4'])
plt.title("Customized box plot")
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.show()

'''

