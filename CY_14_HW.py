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
'''
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
'''
3-Write a program to take all prime numbers from a queue and add to a new queue

4-Write a program to store all credit card numbers in a type and verify them.
 Using the binary search algorithm find the starting alphabet of any word from a list in random order.

Use the binary search algorithm to find the greatest number in a list.
 Write a program to implement Queue structure and generate a word “MISSISSIPPI” 

Write a program to implement Queue structure to enter factorials of any number given.'''