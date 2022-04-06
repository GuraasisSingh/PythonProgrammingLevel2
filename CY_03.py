#Searching
'''
Linear Search- Method to find elements in a list -> known as sequential search

a=[1,3,5,4,7,9]
Algorithm:::
def ls(a,key):
    for i in a:
        if i==key:
            return a[i]
    return -1   
'''
def ls(a,n,key):
    for i in range(0,n):
        if(a[i]==key):
            return i
    return -1

a=[1,3,5,4,7,9]
k=7
n=len(a)
res=ls(a,n,k)

if(res==-1):
    print("Element is not present")
else:
    print("Element found at index ",res)
    
'''
HomeWork
->Implement linear search algorithm to find how many no. of times the letter p and s occured in the word mississippi
->Implement Linear Search Algorithm to find the odd numbers within a list and replace them if:
They end with 1, replace the entire number with 0
They end with 3, don't do anything
They end with 5, replace the entire number -3
They end with 7, replace them with 2
They end with 9, replace them with 18
'''
'''
Binary Search ::

a=[12,24,32,39,45,50,54]
low=0
high=6
mid=(0+6)//2
Hence, mid=3

'''
