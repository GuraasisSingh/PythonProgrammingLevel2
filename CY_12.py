'''Rahul and his friends were measuring their heights in random order. 
They created the list of heights of all the students. 
Rahul wanted to know the range of the height in his class. 
 i.e lowest height, biggest height, and the difference between lowest height and biggest height. 
 Write a python program to get the answer.
Hint: Create a list. Enter all the heights inside the list in any order.
 Apply selection sort algorithm and arrange it in ascending order. 
 Then the first element of the list will be the lowest height, the last element of the list will be the 
 biggest height and the difference between these two values will be the range.'''

def ss(l):
    n=len(l)
    for i in range(n-1):
       mvi=i 
       for j in range(i+1,n):
           if l[j]<l[mvi]:
               mvi=j
       if mvi != i:
           temp=l[i]
           l[i]=l[mvi]
           l[mvi]=temp
    return l

a=[54,61,35,23,78,93,45,79,97,112,110]
t=ss(a)
print("The lowest height is: ",t[0])
print("The biggest height is ",t[len(a)-1])
print("The difference =",t[len(a)-1]-t[0])


