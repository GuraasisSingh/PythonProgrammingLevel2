'''Bubble Sort:::

a=[5,3,8,6,7,2]
1st Iteration
a=[3,5,8,6,7,2]
a=[3,5,8,6,7,2]
a=[3,5,6,8,7,2]
a=[3,5,6,7,8,2]
a=[3,5,6,7,2,8]

2nd Iteration
a=[3,5,6,7,2,8]
a=[3,5,6,7,2,8]
a=[3,5,6,7,2,8]
a=[3,5,6,2,7,8]
a=[3,5,6,2,7,8]

3rd Iteration




def bs(a):
    for i in range (0,len(a)-1): # iterates the list
        for j in range(len(a)-1):# list and compares two elements
            if (a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
a=[5,3,8,6,7,2]
print("The unsorted list: ",a)
print("The sorted list: ",bs(a))

def bs(a):
    for i in range (0,len(a)-1): # iterates the list
        for j in range(len(a)-1):# list and compares two elements
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[5,3,8,6,7,2]
print("The unsorted list: ",a)
print("The sorted list: ",bs(a))
'''
def bs(a):
    s=True
    t=0
    while(s):
        s=False
        for i in range(len(a)-t-1):
            if (a[i]>a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]
            s=True
        t+=1
    print("The number of iterations ",t)
    return a
a=[5,3,8,6,7,2]
print("The unsorted list: ",a)
print("The sorted list: ",bs(a))

#1.Use the bubble sort algorithm to sort the names of ten students in ascending order and display result of each step.
#2.Use the bubble sort algorithm to sort the numbers in ascending order using last digit of the numbers display result of each step. 

