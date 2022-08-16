'''
Inorder :

Algorithm Inorder(tree) 
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)
 '''

# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree

class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.val),
        # now recur on right child
        printInorder(root.right)

def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        # First recur on left child
        printPostOrder(root.right)
        # now recur on right child
        print(root.val)
        # then print the data of node

def printPreOrder(root):
    if (root):
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 

print ("\nInorder traversal of binary tree is")
printInorder(root)
print ("\nPreOrder traversal of binary tree is")
printPreOrder(root)
print ("\nPostorder traversal of binary tree is")
printPostOrder(root)

'''An inorder traversal technique follows the Left Root Right policy.
 Here, Left Root Right means that the left subtree of the root node is traversed first, 
 then the root node, and then the right subtree of the root node is traversed. 
 Here, inorder name itself suggests that the root node comes in between the left and the right subtrees.
'''