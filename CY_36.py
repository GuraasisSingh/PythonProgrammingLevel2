'''
The interquartile range defines the difference between the third and the first quartile. 
Quartiles are the partitioned values that divide the whole series into 4 equal parts.
 So, there are 3 quartiles. First Quartile is denoted by Q1 known as the lower quartile, 
 the second Quartile is denoted by Q2 and the third Quartile is denoted by Q3 known as the upper quartile. 
Therefore, the interquartile range is equal to the upper quartile minus lower quartile.'''
'''
Interquartile Range Formula : 

The difference between the upper and lower quartile is known as the interquartile range. The formula for the interquartile range is given below

Interquartile range = Upper Quartile – Lower Quartile = Q­3 – Q­1

where Q1 is the first quartile and Q3 is the third quartile of the series.
'''
'''
What is the mean of the first 10 natural numbers?


Find the median of the following:

4, 17, 77, 25, 22, 23, 92, 82, 40, 24, 14, 12, 67, 23, 29


Find the mode of the given data set: 3, 3, 6, 9, 15, 15, 15, 27, 27, 37, 48.
'''

'''
In statistics, the mode is the value that is repeatedly occurring in a given set. We can also say that the value or number in a data set, which has a high frequency or appears more frequently, is called mode or modal value. It is one of the three measures of central tendency, apart from mean and median.

Mode formula for grouped data :

Where,

l = lower limit of the modal class

h = size of the class interval

f1 = frequency of the modal class

f0 = frequency of the class preceding the modal class

f2 = frequency of the class succeeding the modal class

Let us take an example to understand this clearly.
'''
'''
Standard Deviation :
Standard Deviation is a measure which shows how much variation (such as spread, dispersion, spread,) 
from the mean exists. The standard deviation indicates a “typical” deviation from the mean. 
It is a popular measure of variability because it returns to the original units of measure of the data set.  
Like the variance, if the data points are close to the mean, there is a small variation whereas the data points are highly spread out from the mean,
 then it has a high variance. Standard deviation calculates the extent to which the values differ from the average.
  Standard Deviation, the most widely used measure of dispersion, is based on all values. 
  Therefore a change in even one value affects the value of standard deviation. It is independent of origin but not of scale. 
It is also useful in certain advanced statistical problems.'''

'''
First quartile: Also known as Q1, or the lower quartile. This is the number halfway between the lowest number and the middle number.

Second quartile: Also known as Q2, or the median. This is the middle number halfway between the lowest number and the highest number.

Third quartile: Also known as Q3, or the upper quartile. This is the number halfway between the middle number and the highest number.
'''
import numpy

values = [13,21,21,40,42,48,55,72]

x = numpy.quantile(values, [0,0.25,0.5,0.75,1])

print(x)
'''
Percentiles :

Percentiles are values that separate the data into 100 equal parts.

For example, The 95th percentile separates the lowest 95% of the values from the top 5%

The 25th percentile (P25%) is the same as the first quartile (Q1).

The 50th percentile (P50%) is the same as the second quartile (Q2) and the median.

The 75th percentile (P75%) is the same as the third quartile (Q3)

With Python use the NumPy library percentile() method to find the 65th percentile of the values 13, 21, 21, 40, 42, 48, 55, 72:
'''
import numpy

values = [13,21,21,40,42,48,55,72]

x = numpy.percentile(values, 65)

print(x)
'''
Interquartile range is a measure of variation, which describes how spread out the data is.

Interquartile Range
Interquartile range is the difference between the first and third quartiles (Q1 and Q3).

The 'middle half' of the data is between the first and third quartile.

The first quartile is the value in the data that separates the bottom 25% of values from the top 75%.

The third quartile is the value in the data that separates the bottom 75% of the values from the top 25%

With Python use the SciPy library iqr() method to find the interquartile range of the values 13, 21, 21, 40, 42, 48, 55, 72:
'''
from scipy import stats
values = [13,21,21,40,42,48,55,72]
x = stats.iqr(values)
print(x)

# With Python use the NumPy library std() method to find the standard deviation of the values 4,11,7,14:
import numpy
values = [4,11,7,14]
x = numpy.std(values)
print(x)
# With Python use the NumPy library std() method to find the sample standard deviation of the values 4,11,7,14:
import numpy
values = [4,11,7,14]
x = numpy.std(values, ddof=1)
print(x)
'''
Scipy is a python library that is useful in solving many mathematical equations and algorithms.

It is designed on the top of Numpy library that gives more extension of finding scientific mathematical formulae like Matrix Rank, Inverse, polynomial equations, LU Decomposition, etc. 

Using its high-level functions will significantly reduce the complexity of the code and helps in better analyzing the data.'''

'''
Basic  Probability : 

Probability is a measure of the likelihood of an event to occur. 
Many events cannot be predicted with total certainty. We can predict only the chance of an event to occur i.e. how likely they are to happen,
 using it. Probability can range in from 0 to 1, where 0 means the event to be an impossible one and 1 indicates a certain event. 
 Probability for Class 10 is an important topic for the students which explains all the basic concepts of this topic.
 The probability of all the events in a sample space adds up to 1.

 Types of data  ::

Ordinal
Nominal 
Categorical
Numerical

Ordinal data

With ordinal scales, the order of the values is what’s important and significant, but the differences between each one is not really known. Ordinal scales are typically measures of non-numeric concepts like satisfaction, happiness, discomfort, etc.

Example of ordinal scale :
Very happy , Happy , Unhappy , Very unhappy

Nominal data : 

Nominal data is data that can be labelled or classified into mutually exclusive categories within a variable. These categories cannot be ordered in a meaningful way.

Example of Nominal data :
For the nominal variable of preferred mode of transportation, you may have the categories of car, bus, train, tram or bicycle.


Categorical Data : 

Categorical data is the statistical data comprising categorical variables of data that are converted into categories.
 One of the examples is a grouped data. More precisely, categorical data could be derived from qualitative data analysis that are countable, or from quantitative data analysis grouped within given intervals. These data are summarised in the form of a probability table. However, when we consider data analysis, it is referred to use the term “categorical data”, which is applied to data sets. 
Also, it is to be noted that, while containing some categorical variables, the data set may also contain non-categorical variables.

Numerical Data : 

Numerical data refers to the data that is in the form of numbers, and not in any language or descriptive form. Often referred to as quantitative data, numerical data is collected in number form and stands different from any form of number data types due to its ability to be statistically and arithmetically calculated. 

Example for numerical data :
You have a total count of your employees. You take a count of male employees and subtract that from the total number of employees to get the count of female employees. 
This characteristic of numerical data to be manipulated arithmetically makes it a best suit for statistical data analysis.
'''
'''
Application : 

Census
Sampling
Prediction
Medical Science 
Social Science
Agriculture'''

'''
A probability Distribution represents the predicted outcomes of various values for a given data.
 Probability distributions occur in a variety of forms and sizes, each with its own set of characteristics such as
  mean, median, mode, skewness, standard deviation, kurtosis, etc.
'''