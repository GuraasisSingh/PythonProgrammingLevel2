'''
 Nidhi is working on a big project and she wants a getIndex() function.
 getIndex() function should return the index number of a value present inside a list of numbers and 
 remove that value as well. She told her friend Himanshi to create this function. 
 Also, Nidhi told she wants binary search algorithm to be used in the function. 
 Himanshi tried to create the function but she is not able to return the value. 
 Write a program in python for the same to help Himanshi.
 Note: Use binary search algorithm to search the element in the list.
'''
def getIndex(a,x,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if(a[mid]==x):
            return mid
        elif (a[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1

a=[34,65,45,37,28,94,13,24,65,99]
a.sort()
print(a)
x=94
pos=getIndex(a,x,0,len(a)-1)

if pos !=-1:
    print("Element is present at index "+str(pos))
    a.remove(a[pos])
    print(a)
else:
    print("Not Found!")
