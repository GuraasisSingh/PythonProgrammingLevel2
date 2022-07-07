'''
n=[1,2,34,56,786,23,56]
for i in n:
    if i%2==0:
        i=i+1
    else:
        i=i-1
'''
'''
total=int(input("Enter the number of Elements"))
numbers=[]
for i in range(0,total+1):
    n=int(input("Enter a number"))
    numbers.append(n)
even = []
odd =[]
for j in numbers:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)
'''
'''
class Queue:  
  
  def _init_(self):  
      self.queue = list()  
  
  def add_element(self,val):  
# Insert method to add element  
      if val not in self.queue:  
          self.queue.insert(0,val)  
          return True  
      return False  
# Pop method to remove element  
  def remove_element(self):  
      if len(self.queue)>0:  
          return self.queue.pop()  
      return ("Queue is Empty")  
  
que = Queue()  
que.add_element("January")  
que.add_element("February")  
que.add_element("March")  
que.add_element("April")  
  
print(que)  
print(que.remove_element())  
print(que.remove_element())
'''
class Queue: 
    def _init_(self):
        self.s1 = []
        self.s2 = []
  
    def enQueue(self, x):
          
        # Move all elements from s1 to s2 
        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
  
        # Push item into self.s1 
        self.s1.append(x) 
  
        # Push everything back to s1 
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
  
    # Dequeue an item from the queue 
    def deQueue(self):
          
            # if first stack is empty 
        if len(self.s1) == 0: 
            print("Q is Empty")
      
        # Return top of self.s1 
        x = self.s1[-1] 
        self.s1.pop() 
        return x
  
# Driver code 
if __name__ == '_main_':
    q = Queue()
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
  
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())