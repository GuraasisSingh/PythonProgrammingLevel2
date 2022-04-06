'''
Session 4
Binary Search::
Algo will be using-Divide and Conquer Approach:

a=[3,4,5,6,7,8,9]
#x=4
#high=9, low =3
# mid = a[(low+high)/2]
#here mid=6
#if x==mid, ---->return mid

# if x>mid,------> low=mid+1
#else----->high =mid-1

1-Iterative method:
do until pointers low and high meet each other

2-Recursive method:
def bs(a,x,low,high):
    if low > high:
        return False
    else:
        mid=(low+high)//2
        if x==a[mid]:
            return mid
        elif x>a[mid]:
            return bs(a,x,mid+1,high)
        else:
            return bs(a,x,low,mid-1)
'''
#mid=(low+high)//2
def bs(a,x,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if(a[mid]==x):
            return mid
        elif (a[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1

a=[3,4,5,6,7,8,9]
x=4
res=bs(a,x,0,len(a)-1)
if res!=-1:
    print("Element is present at index "+str(res))
else:
    print("Not Found!")
    


