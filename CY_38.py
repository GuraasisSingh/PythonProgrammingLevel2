
# Matplotlib Adding Grid Lines:

# Matplotlib Adding Grid Lines
# Add Grid Lines to a Plot
# With Pyplot, you can use the grid() function to add grid lines to the plot.

# Example
# Add grid lines to the plot:
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid()
plt.show()




# Matplotlib Adding Grid Lines:

# Matplotlib Adding Grid Lines
# Add Grid Lines to a Plot
# With Pyplot, you can use the grid() function to add grid lines to the plot.

# Example
# Add grid lines to the plot:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid()
plt.show()

# Display only grid lines for the y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()

# Set Line Properties for the Grid
# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

# Example
# Set the line properties of the grid:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

# Display Multiple Plots
# With the subplot() function you can draw multiple plots in one figure:

# Example :
# Draw 2 plots:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.show()

# The subplot() Function
# The subplot() function takes three arguments that describes the layout of the figure.

# The layout is organized in rows and columns, which are represented by the first and second argument.

# The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
plt.subplot(1, 2, 2)


# Matplotlib Subplot
# Display Multiple Plots
# With the subplot() function you can draw multiple plots in one figure:

# Example
# Draw 2 plots:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
# Result:


# The subplot() Function
# The subplot() function takes three arguments that describes the layout of the figure.

# The layout is organized in rows and columns, which are represented by the first and second argument.

# The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
# So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:

# Example
# Draw 2 plots on top of each other:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

# You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.

# Example
# Draw 6 plots:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


# Title
# You can add a title to each plot with the title() function:

# Example
# 2 plots, with titles:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

# Super Title
# You can add a title to the entire figure with the suptitle() function:

# Example
# Add a title for the entire figure:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()


# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.

# The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

# Example
# A simple scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

# The observation in the example above is the result of 13 cars passing by.

# The X-axis shows how old the car is.

# The Y-axis shows the speed of the car when it passes.

# Are there any relationships between the observations?

# It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.

# Compare Plots
# In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?

# Example
# Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

# Note: The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.

# By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.
# Colors :
# You can set your own color for each scatter plot with the color or the c argument:

# Example
# Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()

# ColorMap
# The Matplotlib module has a number of available colormaps.

# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

# This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, and up to 100, which is a yellow color.

# How to Use the ColorMap
# You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

# In addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot:

# Example
# Create a color array, and specify a colormap in the scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='plasma')

plt.show()


# viridis
# plasma
# magma
# cividis
# Greys
# Blues
# Breens
# binary
# summer
# autumn
# winter
# spring
# hot 
# cool
# Spectral
# twilight
# hsv
# ocean
# rainbow
# turbo
# terrain
# prism
# jet
#'''
# You can include the colormap in the drawing by including the plt.colorbar() statement:

# Example
# Include the actual colormap:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

# #Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, cmap='Accent')

# plt.colorbar()

# plt.show()

# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
