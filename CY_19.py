'''
Types of Queue :
Simple Queue: Simple queue also known as a linear queue is the most basic version of a queue.
 Here, insertion of an element i.e. the Enqueue operation takes place at the rear end and removal of an element
 i.e. the Dequeue operation takes place at the front end.


Circular Queue: 
In a circular queue, the element of the queue act as a circular ring.
The working of a circular queue is similar to the linear queue except for the fact that the last element is connected to the first element. Its advantage is that the memory is utilized in a better way.
This is because if there is an empty space i.e.
if no element is present at a certain position in the queue,
then an element can be easily added at that position

Priority Queue:

 This queue is a special type of queue.
  Its specialty is that it arranges the elements in a queue based on some priority.
   The priority can be something where the element with the highest value has the priority 
   so it creates a queue with decreasing order of values. 
   The priority can also be such that the element with the lowest value gets the highest priority 
   so in turn it creates a queue with increasing order of values.

   if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)

   the check for full queue has a new additional case:

Case 1: FRONT = 0 && REAR == SIZE - 1
Case 2: FRONT = REAR + 1
 '''

# Circular Queue implementation in Python

class MyCircularQueue():

    def __init__(self, k):
        # k-> Number of elements or size
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()