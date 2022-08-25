from operator import iadd


# Pandas
#used to analyse data

'''pandas series is a one dimensional labelled array capable of holding dta of any type, (integer, string, float, python,objects,etc)
 The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.'''
'''
 Labels need not be unique but must be a hashable type. 
 The object supports both integer and label-based indexing and provides a host of methods for performing operations involving the index.
 '''

 
 Creating a Pandas Series
In the real world, a Pandas Series will be created by loading the datasets from existing storage,
 storage can be SQL Database, CSV file, and Excel file.
  Pandas Series can be created from the lists, dictionary, and from a scalar value etc. 
  Series can be created in different ways, here are some ways by which we create a series:

Creating a series from array: In order to create a series from array, we have to import a numpy module and
                                 have to use array() function.
 '''