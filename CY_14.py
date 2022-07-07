#Session 14

'''Queue ::: 

First in first out(fifo).

Operations:
enque: It adds an item to the queue. if the queue is full, it is said to be an overflow condition
deque: It removes an item from the queue, items are popped in the same order as they are pushed. 
        if the queue is empty, then it is said to be an underflow condition.
front: gets the front item from the queue
rear: gets the last item from the queue

'''
q=[]
q.append(10)
q.append(100)
q.append(1000)
print("Initial Queue:", q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print("After Removing Elements:", q)
