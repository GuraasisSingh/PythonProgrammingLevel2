''' 1- Write a program to insert only positive numbers to a stack

from collections import deque
numbers=deque()
while True:
    n=int(input("Enter positive numbers to stack and any other number to stop:"))
    if n>0:
        numbers.append(n)
    else:
        break

2-Write a program to edit elements in a stack
Write a program to change all even numbers to odd and odd numbers to even in a queue

from collections import deque
numbers=deque()
while True:
    n=int(input("Add a Number and enter 0 to stop\n"))
    if n==0:
        break
    else:
        numbers.append(n)
print(numbers)
for i in (numbers):
    numbers.pop()    
    #numbers.append(i+1)
    
print(numbers)

3-Write a program to take all prime numbers from a queue and add to a new queue


from collections import deque
prime=deque()
for k in range(1,6):
    n=int(input("Add a Number\n"))
    t=0
    for j in range(1,n+1):
        if n%j == 0:
            t+=1
    if t==2:
        prime.append(n)
print(prime)


4-Write a program to store all credit card numbers in a type and verify them.
 

verified=[123456789,7346589,83091093,742891989]
credits=[123456789,4532344234,7346589,83226136565,83091093,2451356566,742891989]
for i in credits:
    if i in verified:
        print(i)


Using the binary search algorithm find the starting alphabet of any word from a list in random order.

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
a=['archana', 'danny', 'benny', 'ishaan', 'zubair', 'ram' ]
x='zubair'
ans=bs(a,x,0,len(a)-1)
word=a[ans]
print(word[0])

Use the binary search algorithm to find the greatest number in a list.

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
a=[3,8,10,4,9,5,7]
a.sort()
print(a)
x=a[len(a)-1]
ans=bs(a,x,0,len(a)-1)
print(a[ans])

 Write a program to implement Queue structure and generate a word “MISSISSIPPI” 

from collections import deque
stack=deque()
stack.append("M")
stack.append("I")
stack.append("S")
stack.append("S")
stack.append("I")
stack.append("S")
stack.append("S")
stack.append("I")
stack.append("P")
stack.append("P")
stack.append("I")
print(stack)
for i in stack:
    print(i,end="")

Write a program to implement Queue structure to enter factorials of any number given.

total=int(input("Enter the number of Elements"))
numbers=[]
for i in range(0,total+1):
    n=int(input("Enter a number"))
    numbers.append(n)
'''