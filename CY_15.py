"""
Queue
Implementation using:
1-list
2-collections.deque
--------------
from collections import deque
q=deque()
q.append("a")
q.append("b")
q.append("c")
print("Initial Queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements:")
print(q)
------------------
3-queue.Queue
--------------------
from queue import Queue
q=Queue(maxsize=3)
print(q.qsize())
q.put("a")
q.put("b")
q.put("c")
print("\nFull: ",q.full())
print("\nElements dequeued from the queue: ")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ",q.empty())
q.put(1)
print("\nEmpty: ",q.empty())
print("Full: ",q.full())
------------------
"""
