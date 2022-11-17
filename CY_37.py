

'''
Visualize Distributions With Seaborn :

Seaborn is a library that uses Matplotlib underneath to plot graphs. 
It will be used to visualize random distributions.

Distplot :
Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.


What is Matplotlib?
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.


Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

import matplotlib.pyplot as plt
Now the Pyplot package can be referred to as plt
'''
'''
# import matplotlib.pyplot as plt
# Draw a line in a diagram from position (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.'''

#  Draw a line in a diagram from position (1, 3) to position (8, 10):
'''
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
#  The x-axis is the horizontal axis.

# The y-axis is the vertical axis.

# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

# Example
# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# Multiple Points:
# You can plot as many points as you like, just make sure you have the same number of points in both axis.

# Example:
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# Default X-Points:
# If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

# So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

# Plotting without x-points:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
# The x-points in the example above is [0, 1, 2, 3, 4, 5]


# Matplotlib Markers :
# Markers :
# You can use the keyword argument marker to emphasize each point with a specified marker:

# Example:
# Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = '*')
plt.show()

# Mark each point with a star:

# ...
# plt.plot(ypoints, marker = '*')
# ...

Matplotlib Markers
Markers
You can use the keyword argument marker to emphasize each point with a specified marker:

Example
Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
Result:


# Marker	Description
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline


# Format Strings fmt :
# You can use also use the shortcut string notation parameter to specify the marker.

# This parameter is also called fmt, and is written with this syntax:
# marker|line|color

# Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# The marker value can be anything from the Marker Reference above.

# The line value can be one of the following:

# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line

# Note: If you leave out the line value in the fmt parameter, no line will be plotted

# Color Reference:
# Color Syntax	Description
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White
'''
# Marker Size :
# You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

# Example:
# Set the size of the markers to 20:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Marker Color:
# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:

# Example :
# Set the EDGE color to red:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:

# Example
# Set the FACE color to red:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()
# Use both the mec and mfc arguments to color of the entire marker

# Set the color of both the edge and the face to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

# Mark each point with a beautiful green color:

# ...
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# ...

# Mark each point with the color named "hotpink":

# ...
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
# ...

# Linestyle
# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

# Example
# Use a dotted line:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Use a dashed line:
# plt.plot(ypoints, linestyle = 'dashed')

# Line Color:
# You can use the keyword argument color or the shorter c to set the color of the line:

# Example:
# Set the line color to red:

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'r')
plt.show()

# Plot with a beautiful green line:

# ...
# plt.plot(ypoints, c = '#4CAF50')
# ...

# Plot with the color named "hotpink":

# ...
# plt.plot(ypoints, c = 'hotpink')
# ...

# Line Width
# You can use the keyword argument linewidth or the shorter lw to change the width of the line.

# The value is a floating number, in points:

# Example
# Plot with a 20.5pt wide line:
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:

# Example
# Draw two lines by specifying a plt.plot() function for each line:

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# You can also plot many lines by adding the points for the x- and y-axis 
# for each line in the same plt.plot() function.

# (In the examples above we only specified the points on the y-axis, meaning that the points on the
#  x-axis got the the default values (0, 1, 2, 3).)

# The x- and y- values come in pairs:

# Example
# Draw two lines by specifiyng the x- and y-point values for both lines:

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# Create Labels for a Plot:

# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

# Example
# Add labels to the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Create a Title for a Plot:

# With Pyplot, you can use the title() function to set a title for the plot.

# Example
# Add a plot title and labels for the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# Set Font Properties for Title and Labels :
# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

# Example
# Set font properties for the title and labels:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

# Position the Title :
# You can use the loc parameter in title() to position the title.

# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

# Example
# Position the title to the left:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()
