'''
Stack:
Operations:
1- Push
2-Pop

'''

'''
from collections import deque
stack=deque()
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial Stack")
print("\nElements popped from the stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nStack after elements are popped:: ")
print(stack)
'''
from queue import LifoQueue
stack=LifoQueue(maxsize=3)
print(stack.qsize())
stack.put("a")
stack.put("b")
stack.put("c")
print("Full",stack.full())
print("Size:",stack.qsize())
print("Initial Stack: ")
print("\nElements popped from the stack: ")
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty:: ",stack.empty())
print(stack)

# Write a program to insert random letters and while popping, create a word,"train".
# Write a program to use fibonacci series using stack.
# Write a program to insert and display five names using stack algorithm
# Write a program to implement factorial of all numbers using stack.