# To plot a nested pie chart in Matplotlib, we can take the following steps −

# Set the figure size and adjust the padding between and around the subplots.
# Create a figure and a set of subplots.
# Initialize a variable size, create vals, cmap, outer_colors, inner_colors data using numpy.
# Use pie() function to make pie charts.
# To display the figure, use show() method.

# What is a Nested Pie Chart in Matplotlib?
# A nested pie chart is a pie chart in which multiple pie charts are embedded.
# We can explain it as an analogy with nested lists.
# We use it to represent the data at multiple levels in the plot.

# What is the use of the Nested Pie Chart in Matplotlib?
# Nested pie charts are handy when we want to plot pie charts with other constraints present.

# For example, Suppose a company wants to plot a pie chart and analyze the data of the share of sales distribution of different products over the past 10 years.
# Then one way of doing this is to make 10 different pie plots. However, this seems to be not a clear idea.
# A much better idea would be to plot all the pie charts in a single graph so we can better visualize the data.

# Plotting a Simple Nested Pie Chart:
# Plotting a simple nested pie chart is simple. We need to keep in mind the following points to plot a nested pie chart:

# We need to pass the multiple pie () function to plot multiple pie charts in the figure.
# Next, we also need to pass another attribute about the radius of the pie chart.
# The radius of each pie chart should be distinct; 
# otherwise, they will overlap each other, and hence we will be able to visualize only one pie chart.


# Syntax: matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)
# Parameters: 
# data represents the array of data values to be plotted, the fractional area of each slice is represented by data/sum(data). If sum(data)<1, then the data values returns the fractional area directly, thus resulting pie will have empty wedge of size 1-sum(data). 
# labels is a list of sequence of strings which sets the label of each wedge. 
# color attribute is used to provide color to the wedges. 
# autopct is a string used to label the wedge with their numerical value. 
# shadow is used to create shadow of wedge.

# A pie chart can be customized on the basis several aspects.
# The startangle attribute rotates the plot by the specified degrees in counter clockwise direction performed on x-axis of pie chart. 
# shadow attribute accepts boolean value, if its true then shadow will appear below the rim of pie. Wedges of the pie can be customized using wedgeprop which takes Python dictionary as parameter with name values pairs denoting the wedge properties like linewidth, edgecolor, etc.
#  By setting frame=True axes frame is drawn around the pie chart.
# autopct controls how the percentages are displayed on the wedges.

from matplotlib import pyplot as plt
import numpy as np
# Creating dataset
size = 6
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
data = np.array([[23, 16], [17, 23], [35, 11], [29, 33], [12, 27], [41, 42]])
# normalizing data to 2 pi
norm = data / np.sum(data)*2 * np.pi
# obtaining ordinates of bar edges
left = np.cumsum(np.append(0,norm.flatten()[:-1])).reshape(data.shape)
# Creating color scale
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(6)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10, 12, 13, 15, 17, 18, 20 ]))
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7),subplot_kw = dict(polar = True))
ax.bar(x = left[:, 0],width = norm.sum(axis = 1),bottom = 1-size,height = size,color = outer_colors, edgecolor ='w',linewidth = 1,align ="edge")
ax.bar(x = left.flatten(),
       width = norm.flatten(),
       bottom = 1-2 * size,
       height = size,
       color = inner_colors,
       edgecolor ='w',
       linewidth = 1,
       align ="edge")
ax.set(title ="Nested pie chart")
ax.set_axis_off()
# show plot
plt.show()

# import numpy as np
# a=10
# print(a)
# c=np.cumsum([a,3,7,5,6])
# print(c)
'''
import matplotlib.pyplot as plt
#creating a user-defined function named nested_pie()
def nested_pie(x,y,z,labelx,labely,labelz,size):
    #creating figure object 
    fig=plt.figure(figsize=(5,10))
    #creating the axis with 4 parameters passed
    ax=fig.add_axes([0,0,1,1])
    #creating the outermost pie chart
    ax.pie(x,radius=size,labels=labelx,labeldistance=0.2)
    #creating the middle pie chart
    ax.pie(y,radius=size-0.3,labels=labely,labeldistance=0.7)
    #creating the smallesst pie chart
    ax.pie(z,radius=size-0.6,labels=labelz,labeldistance=1.8)
    plt.show()
def main():
    #creating data point for the outermost pie chart
    salary1=[78000,89000,97000,68000,85000]
    label1=["john","simon","smith","richard","brine"]
    #creating data point for the middle pie chart
    salary2=[58000,49000,63000,68000,45000]
    label2=["elsa","steve","micheal","johnson","jakson"]
    #creating data point for the pie chart with the least radius
    salary3=[86000,89000,97000,92000,98000]
    label3=["willy","tesla","williamson","dextro","rayan"]
    #defining the size or the pie chart
    size=1
    #calling the nested_pie() function
    nested_pie(salary1,salary2,salary3,label1,label2,label3,size)
#declaring the main() function as the main driving code of the program.

if __name__=="__main__":
    main()
    '''