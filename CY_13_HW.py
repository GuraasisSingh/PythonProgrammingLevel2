'''HW QUESTIONS :::

Nidhi is preparing for her examination, and she has so many topics to cover.
She decided to study each topic properly, and then revise each topic in reverse order to finalize it.
To make her work easy, write a python program and create a Stack class ( stack data structure ) where she
can add the topic that she is learning for the first time.
After completing all the topics she can check the peak value of the stack to check which topic she has to revise. 
After revising the topic she can pop the element from the stack.
Once the stack becomes empty, it indicates she is ready for her examination.'''
from queue import LifoQueue
stack=LifoQueue()
print("Please add the topics which are covered and input space key to stop ")
while True:
    topic=input()
    if topic==" ":
        break
    else:
        stack.put(topic)
while True:
    if stack.empty():
        print("You are ready for your examinations.")
        break
    else:
        print("Please revise the peak topic",stack.get(),"\nPress 1 to move to next")
        if input() =="1":
            continue
