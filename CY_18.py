'''
#Linked List:
Limitation of Arrays:
1. Size of array is fixed
2. Insertiuon of new element/ Deletion of existing element is expensive

Advantages of linked lists over arrays:
1. Dynamic array
2. ease of insertion / deletion

Drawbacks:
1. Random access is not always, always starts sequentially stARTING FORM first  node(head node), so binary search is not efficient
2. Extra memomory space for a pointer is required with each element of list
3. Not Cahche friendly since arrays are contiguous locations, there is a locatility of reference which is not there in case of linked list.

Pointer(used in c, c++)-> it stores memory of previous addresses in linked list of another variable, 
[represented by *]        it holds mutable or immutable objects
                          We only use it as a logical part as it violates the rule or zen of python
'''
'''
class Node():
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
   def _init_(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2
#Link second Node to third node
e2.nextval = e3'''
'''
In the case of a singly linked list, the next of the last node contains the address of the first node and in case of a doubly-linked list,
 the next of last node contains the address of the first node and prev of the first node contains the address of the last node.
 
 Circular Linked List. In circular linked list the last node of the list holds the address of the first node hence forming a circular chain
 
 The first part can be said as information or data part, second part can be called prev field and the third part can be called next field.
 The prev field contains address of the previous node in the list and next field contains the address of next node in the list.
 '''        
'''class Node:
   # Function to initialize the node object
    def _init_(self, data):
        self.data = data  
#assign data
        self.next = None  
# Initialize 
 # next as null
   
# Linked List class
class LinkedList:
     
    # Function to initialize the Linked 
    # List object
    def _init_(self): 
        self.head = None'''

    
'''Each node in a list consists of at least two parts: 

A Data Item (we can store integer, strings or any type of data).
Pointer (Or Reference) to the next node (connects one node to another) or An address of another node'''

"""
# Node class
class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
  
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
  
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
  
    llist.head.next = second; # Link first node with second 
  
    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
  
    second.next = third; # Link second node with the third node
  
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    """





# A simple Python program for traversal of a linked list
  
# Node class
class Node:
  
    # Function to initialise the node object
    def _init_(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
  
  
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
  
    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
  
    llist.printList()