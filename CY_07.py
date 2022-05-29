# Insertion Sort

# Assume thst the first card is sorted.
'''
a=[9,5,1,4,3]
key=5
a=[5,9,1,4,3]
key=1
a=[1,5,9,4,3]
key=4
a=[1,4,5,9,3]
key=3
a=[1,3,4,5,9]
'''
def iso(a):
    for i in range(1,len(a)):
        key =a[i]
        j=i-1        
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
        
al=[9,5,1,4,3]
iso(al)
print("Sorted List in Ascending Order: ",al)
# In Place->  requires additional place without caring for the input size of the collection   

# Hw
# Concept Test: which among selection, bubble and insertion is better and why?
# which among selection and insertion is better and why?
# Use insertion sort to sort a random list of numbers and find 21 in it using linear search.
# Use the insertion sort to sort a list of book names in the alphabetical order of their author name.
# Use insertion sort to names of students in reverse alphabetical order.
# Use insertion sort and binary search to eliminate the odd numbers from a list of 25 numbers

