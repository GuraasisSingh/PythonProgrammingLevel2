'''#Session 6
#Selection Sort-> In-Place Sorting
#Empty By Default
a=[21,6,9,33,3]
a=[3,6,9,33,21]
a=[3,6,9,33,21]
a=[3,6,9,33,21]
a=[3,6,9,21,33]


'''
def ss(l):
    n=len(l)
    for i in range(n-1):
        mvi=i #minimum value index
        for j in range(i+1,n):
            if l[j]<l[mvi]:
                mvi=j
        if mvi != i:
            temp=l[i]
            l[i]=l[mvi]
            l[mvi]=temp
    return l

a=[21,6,9,33,3]
print("The unsorted list: ",a)
print("The sorted list: ",ss(a))
'''

def ss(a):
    for i in range(0,len(a)-1):
        s=i
        for j in range(i+1,len(a)):
            if a[j] < a[s]:
                s=j
        a[i],a[s]=a[s],a[i]
    return a    
a=[21,6,9,33,3]
print("The unsorted list: ",a)
print("The sorted list: ",ss(a))


# dry run it
# Use the selection sort algorithm to sort a list in the reverse order
# Use the selection sort algorithm to sort a list of names in the reverse order

# concept : what happens when common elements are used selection and bubble sort
# program to find second largest element in the array.
# write a binary search program to eliminate an odd number in list of 25 numbers
'''