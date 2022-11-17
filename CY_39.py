
'''
# Size
# You can change the size of the dots with the s argument.

# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# Example
# Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()

# Alpha
# You can adjust the transparency of the dots with the alpha argument.

# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# Example
# Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)
#range of alpha is from 0 to 1
plt.show()

# Combine Color Size and Alpha
# You can combine a colormap with different sizes on the dots. This is best visualized if the dots are transparent:

# Example
# Create random arrays with 100 values for x-points, y-points, colors and sizes:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

# Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:

# Example
# Draw 4 bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# The bar() function takes arguments that describes the layout of the bars.

# The categories and their values represented by the first and second argument as arrays.

# The categories and their values represented by the first and second argument as arrays.

# # Example
# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)

# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

# Example
# Draw 4 horizontal bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

# Bar Color
# The bar() and barh() takes the keyword argument color to set the color of the bars:

# Example
# Draw 4 red bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

# Color Names
# You can use any of the 140 supported color names.

# Example
# Draw 4 "hot pink" bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

# Color Hex
# Or you can use Hexadecimal color values:

# Example
# Draw 4 bars with a beautiful green color:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()


# Bar Width
# The bar() takes the keyword argument width to set the width of the bars:

# Example
# Draw 4 very thin bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

# The default width value is 0.8

# Note: For horizontal bars, use height instead of width.

# Bar Height
# The barh() takes the keyword argument height to set the height of the bars:

# Example
# Draw 4 very thin bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()

# The default height value is 0.8

# Histogram
# A histogram is a graph showing frequency distributions.

# It is a graph showing the number of observations within each given interval.

# Create Histogram
# In Matplotlib, we use the hist() function to create histograms.

# The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

# Example
# A Normal Data Distribution by NumPy:

# import numpy as np

# x = np.random.normal(170, 10, 250)

# print(x)

# The hist() function will read the array and produce a histogram:

# Example
# A simple histogram:

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show()

# Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
# You can read from the histogram that there are approximately:

# 2 people from 140 to 145cm
# 5 people from 145 to 150cm
# 15 people from 151 to 156cm
# 31 people from 157 to 162cm
# 46 people from 163 to 168cm
# 53 people from 168 to 173cm
# 45 people from 173 to 178cm
# 28 people from 179 to 184cm
# 21 people from 185 to 190cm
# 4 people from 190 to 195cm

from matplotlib import pyplot as plt
import numpy as np
a=np.array([21,45,65,75,43])
b,c=plt.subplots(figsize=(10,7))
c.hist(a,bins=[20,30,80])
plt.show()

# Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:

# Example
# A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
# As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).

# By default the plotting of the first wedge starts from the x-axis and move counterclockwise:

# Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:

# The value divided by the sum of all values: x/sum(x)


# Labels
# Add labels to the pie chart with the label parameter.

# The label parameter must be an array with one label for each wedge:

# Example
# A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

# Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.

# The startangle parameter is defined with an angle in degrees, default angle is 0:

# Start the first wedge at 90 degrees:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

# Explode :
# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

# The explode parameter, if specified, and not None, must be an array with one value for each wedge.

# Each value represents how far from the center each wedge is displayed:

# Example
# Pull the "Apples" wedge 0.2 from the center of the pie:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.2, 0.2, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

# Shadow
# Add a shadow to the pie chart by setting the shadows parameter to True:

# Example
# Add a shadow:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
'''
# Colors
# You can set the color of each wedge with the colors parameter.

# The colors parameter, if specified, must be an array with one value for each wedge:

# Example
# Specify a new color for each wedge:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

# You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:

# 'r' - Red
# 'g' - Green
# 'b' - Blue
# 'c' - Cyan
# 'm' - Magenta
# 'y' - Yellow
# 'k' - Black
# 'w' - White

# Legend
# To add a list of explanation for each wedge, use the legend() function:

# Example
# Add a legend:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

# Legend With Header
# To add a header to the legend, add the title parameter to the legend function.

# Example
# Add a legend with a header:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()