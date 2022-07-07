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

