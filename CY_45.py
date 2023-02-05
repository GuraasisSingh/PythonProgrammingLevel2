
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
# seaborn.countplot() method is used to Show the counts of observations in each categorical bin using bars.


# Syntax : seaborn.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)
# Parameters : This method is accepting the following parameters that are described below: 
 

# x, y: This parameter take names of variables in data or vector data, optional, Inputs for plotting long-form data.
# hue : (optional) This parameter take column name for colour encoding.
# data : (optional) This parameter take DataFrame, array, or list of arrays, Dataset for plotting. If x and y are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.
# order, hue_order : (optional) This parameter take lists of strings. Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.
# orient : (optional)This parameter take “v” | “h”, Orientation of the plot (vertical or horizontal). This is usually inferred from the dtype of the input variables but can be used to specify when the “categorical” variable is a numeric or when plotting wide-form data.
# color : (optional) This parameter take matplotlib color, Color for all of the elements, or seed for a gradient palette.
# palette : (optional) This parameter take palette name, list, or dict, Colors to use for the different levels of the hue variable. Should be something that can be interpreted by color_palette(), or a dictionary mapping hue levels to matplotlib colors.
# saturation : (optional) This parameter take float value, Proportion of the original saturation to draw colors at. Large patches often look better with slightly desaturated colors, but set this to 1 if you want the plot colors to perfectly match the input color spec.
# dodge : (optional) This parameter take bool value, When hue nesting is used, whether elements should be shifted along the categorical axis.
# ax : (optional) This parameter take matplotlib Axes, Axes object to draw the plot onto, otherwise uses the current Axes.
# kwargs : This parameter take key, value mappings, Other keyword arguments are passed through to matplotlib.axes.Axes.bar().
# Returns: Returns the Axes object with the plot drawn onto it.


# The below examples illustrate the countplot() method of the seaborn library.
# Grouping variables in Seaborn countplot with different attributes


# Example 1: Show value counts for a single categorical variable. 
# If we use only one data variable instead of two data variables then it means that the axis denotes each of these data variables as an axis.
# X denotes an x-axis and y denote a y-axis.

'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.countplot(x ='sex',data = df)
plt.show()'''
# Count Plot does not take two dimensional variables together.-> either x or y.
# Syntax:
# seaborn.countplot(x)

# Example 2 : Show value counts for two categorical variables and using hue parameter:
# While the points are plotted in two dimensions, another dimension can be added to the plot by coloring the points according to a third variable.

'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.countplot(x ='sex', hue = "smoker", data = df)
plt.show()'''


# Example 3 : Plot the bars horizontally. 
# In the above example, we see how to plot a single horizontal countplot and here can perform multiple horizontal count plots with the exchange of the data variable with another axis.
# sns.countplot(y ='sex', hue = "smoker", data = df)

'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.countplot(y ='sex', hue = "smoker", data = df)
plt.show()'''

# Example 4 : Use different color palette attributes. 
# Using the palette we can generate the point with different colors. In this below example we can see the palette can be responsible for a generate the countplot with different colormap values.
# Syntax :
# seaborn.countplot(x, y, data, hue, palette)
'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.countplot(x ='sex', data = df, palette = "Set2")
plt.show()'''

# Example 5: using a color parameter in the plot.
# Using color attributes we are Color for all the elements.
# Syntax:
# seaborn.countplot(x, y, data, color)

'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
sns.countplot(x = 'class',hue = 'sex', data = df,color="salmon")
plt.show()'''


# Example 6: Using a saturation parameter in the plot.
# Proportion of the original saturation to draw colors at.Large patches often look better with slightly desaturated colors,
#  but set this to 1 if you want the plot colors to perfectly match the input color spec.
# Syntax:
# seaborn.colorplot(x, y, data, saturation)
'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
sns.countplot(x ='sex', data = df, color="salmon",saturation = 0.1)
plt.show()'''

# Example 7: Use matplotlib.axes.Axes.bar() parameters to control the style.
# We can set Width of the gray lines that frame the plot elements using linewidth. Whenever we increase linewidth than the point also will increase automatically.
# Syntax:
# seaborn.countplot(x, y, data, linewidth, edgecolor)

'''import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
sns.countplot(x ='sex', data = df,color="salmon", facecolor=(1,1,1,1), linewidth=5,edgecolor=sns.color_palette("BrBG", 2))
plt.show()'''

'''
from matplotlib import pyplot as plt
import numpy as np
# Rc-> Runtime Configuration
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(-10, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, color='yellow', lw=7)
ax.set_facecolor('red') 
plt.show()'''

###########################################################################################################################################################

'''
# SQL -> Structured Queried Language

What is Data?
Facts related to object in consideration  eg: age, height etc.

Database:
database is a systematic collection of data.
they support electronic storage and manipulation of data
management of data becomes easy

DBMS->Database Management System
collection of programs that lets its users to access to databases, manipulate data, report and represent data
It also helps to control access to the database

# continue from here........
Advantages of database management:

SQL is a standard language for accessing and manipulating databases.


What is SQL?
SQL stands for Structured Query Language
SQL lets you access and manipulate databases
SQL became a standard of the American National Standards Institute (ANSI) in 1986,
and of the International Organization for Standardization (ISO) in 1987


What Can SQL do?
SQL can execute queries against a database
SQL can retrieve data from a database
SQL can insert records in a database
SQL can update records in a database
SQL can delete records from a database
SQL can create new databases
SQL can create new tables in a database
SQL can create stored procedures in a database
SQL can create views in a database
SQL can set permissions on tables, procedures, and views

Query?
gives result


Relational. This tabular approach defines data so it can be reorganized and accessed in many ways.
 Relational databases are comprised of tables. Data is placed into predefined categories in those tables.
   Each table has columns with at least one data category, and rows that have a certain data instance for the categories which are defined in the columns. 
   Information in a relational database about a specific customer is organized into rows, columns and tables.
 These are indexed to make it easier to search using SQL or NoSQL queries.

 Typically, the RDBMS gives users the ability to control read/write access, specify report generation and analyze use.
   Some databases offer atomicity, consistency, isolation and durability, or ACID, compliance to guarantee that data is consistent and that transactions are complete.
 
   2)

Distributed. This database stores records or files in several physical locations. Data processing is also spread out and replicated across different parts of the network.

Distributed databases can be homogeneous, where all physical locations have the same underlying hardware and run the
 same operating systems and database applications. They can also be heterogeneous.
 In those cases, the hardware, OS and database applications can be different in the various locations.
 
3)

Cloud. These databases are built in a public, private or hybrid cloud for a virtualized environment.
 Users are charged based on how much storage and bandwidth they use. 
 They also get scalability on demand and high availability.
 These databases can work with applications deployed as software as a service.

 
 4)

NoSQL. NoSQL databases are good when dealing with large collections of distributed data.
 They can address big data performance issues better than relational databases. 
 They also do well analyzing large unstructured data sets and data on virtual servers in the cloud. 
These databases can also be called non-relational databases.

5)

Object-oriented. These databases hold data created using object-oriented programming languages. 
They focus on organizing objects rather than actions and data rather than logic. 
For instance, an image data record would be a data object, rather than an alphanumeric value.


6)

Graph. These databases are a type of NoSQL database. They store, map and query relationships using concepts from 
graph theory.
 Graph databases are made up of nodes and edges. Nodes are entities and connect the nodes.


 What are the components of a database?
While the different types of databases vary in schema, data structure and data types most suited to them, they are all comprised of the same five basic components.

Hardware. This is the physical device that database software runs on. Database hardware includes computers, servers and hard drives.
Software. Database software or application gives users control of the database. Database management system (DBMS) software is used to manage and control databases.
Data. This is the raw information that the database stores. Database administrators organize the data to make it more meaningful.
Data access language. This is the programming language that controls the database. The programming language and the DBMS must work together. One of the most common database languages is SQL.
Procedures. These rules determine how the database works and how it handles the data.
 
 What are database challenges?
Setting up, operating and maintaining a database has some common challenges, such as the following:

Data security is required because data is a valuable business asset. Protecting data stores requires skilled cybersecurity staff, which can be costly.
Data integrity ensures data is trustworthy. It is not always easy to achieve data integrity because it means restricting access to databases to only those qualified to handle it.
Database performance requires regular database updates and maintenance. Without the proper support, database functionality can decline as the technology supporting the database changes or as the data it contains changes.
Database integration can also be difficult. It can involve integrating data sources from varying types of databases and structures into a single database or into data lakes and data warehouses.
 


APIs connect the user or application to the database management system, which lets them interact with the database.


What is a database management system?
A DBMS enables users to create and manage a database. It also helps users create, read, update and delete data in a database, and it assists with logging and auditing functions.

The DBMS provides physical and logical independence from data. Users and applications do not need to know either the physical or logical locations of data. A DBMS can also limit and control access to the database and provide different views of the same database schema to multiple users.
 '''

'''
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index

'''

