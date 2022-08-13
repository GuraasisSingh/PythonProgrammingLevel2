"""
A tree consists of a root, and zero or more subtrees T1, T2, … , Tk
such that there is an edge from the root of the tree to the root of each subtree.

"""
'''
# Function to add an edge between vertices x and y
# Function to print the parent of each node
def printParents(node, adj, parent):
 
    # current node is Root, thus, has no parent
    if (parent == 0):
        print(node, "->Root")
    else:
        print(node, "->", parent)
    # Using DFS
    for cur in adj[node]:
        if (cur != parent):
            printParents(cur, adj, node)
# Function to print the children of each node
def printChildren(Root, adj):
    # Queue for the BFS
    q = []
    # pushing the root
    q.append(Root)
    # visit array to keep track of nodes that have been
    # visited
    vis = [0]*len(adj)
    # BFS
    while (len(q) > 0):
        node = q[0]
        q.pop(0)
        vis[node] = 1
        print(node, "-> ", end=" ")
        for cur in adj[node]:
            if (vis[cur] == 0):
                print(cur, " ", end=" ")
                q.append(cur)
        print("\n")
# Function to print the leaf nodes
def printLeafNodes(Root, adj):
    # Leaf nodes have only one edge and are not the root
    for i in range(0, len(adj)):
        if (len(adj[i]) == 1 and i != Root):
            print(i, end=" ")
    print("\n")
# Function to print the degrees of each node
def printDegrees(Root, adj):
    for i in range(1, len(adj)):
        print(i, ": ", end=" ")
        # Root has no parent, thus, its degree is equal to
        # the edges it is connected to
        if (i == Root):
            print(len(adj[i]))
        else:
            print(len(adj[i])-1)
# Driver code
# Number of nodes
N = 7
Root = 1
# Adjacency list to store the tree

adj = []
for i in range(0, N+1):
    adj.append([])
 
# Creating the tree
adj[1].append(2)

adj[2].append(1)

adj[1].append(3)

adj[3].append(1)

adj[1].append(4)

adj[4].append(1)

adj[2].append(5)
adj[5].append(2)
 
adj[2].append(6)

adj[6].append(2)
adj[4].append(7)
adj[7].append(4)
# Printing the parents of each node
print("The parents of each node are:")
printParents(Root, adj, 0)
# Printing the children of each node
print("The children of each node are:")
printChildren(Root, adj)
# Printing the leaf nodes in the tree
print("The leaf nodes of the tree are:")
printLeafNodes(Root, adj)
 
# Printing the degrees of each node

print("The degrees of each node are:")
printDegrees(Root, adj)
'''
'''
Basic Operation Of Tree:
Create  create a tree in data structure.
Insert Inserts data in a tree.
Search  Searches specific data  in a tree to check it is present or not.
Preorder Traversal perform Traveling a tree in a pre-order manner in data structure .
In order Traversal perform Traveling a tree in an in-order manner.
Post order Traversal perform Traveling a tree in a post-order manner.
'''
"""
Types of Tree data structures
The different types of tree data structures are as follows:

1. General tree

A general tree data structure has no restriction on the number of nodes. It means that a parent node can have any number of child nodes.  

2. Binary tree  

A node of a binary tree can have a maximum of two child nodes. In the given tree diagram, node B, D, and F are left children, while E, C, and G are the right children.  

3. Balanced tree

If the height of the left sub-tree and the right sub-tree is equal or differs at most by 1, 
the tree is known as a balanced tree.

4. Binary search tree

As the name implies, binary search trees are used for various searching and sorting algorithms.
 The examples include AVL tree and red-black tree. It is a non-linear data structure. 
 It shows that the value of the left node is less than its parent, 
while the value of the right node is greater than its parent."""

'''Empty Tree 

When using zero-based counting, the root node has depth zero, leaf nodes have height zero, 
and a tree with only a single node (hence both a root and leaf) has depth and height zero. 
Conventionally, an empty tree (tree with no nodes, if such are allowed) has height-1.

Empty Tree a binary Tree :
A null pointer represents a binary tree with no elements -- the empty tree. The formal recursive definition is:
a binary tree is either empty (represented by a null pointer), 
or is made of a single node, where the left and right pointers (recursive definition ahead) each point to a binary tree.
'''
'''
The height of a node is the length of the longest downward path to a leaf from that node.
The height of the root is the height of the tree.
The depth of a node is the length of the path to its root (i.e., its root path).
When using zero-based counting, the root node has depth zero, leaf nodes have height zero,
and a tree with only a single node (hence both a root and leaf) has depth and height zero. 
Conventionally, an empty tree (tree with no nodes, if such are allowed) has height -1.
'''

# Level
# The level of a node is the number of edges along the unique path between it and the root node.
# This is the same as depth when using zero-based counting.

# Size of a tree
# Number of nodes in the tree.


# Degree
# For a given node, its number of children. A leaf has necessarily degree zero.


# Operations : 

# Enumerating all the items
# Enumerating a section of a tree
# Searching for an item
# Adding a new item at a certain position on the tree
# Deleting an item
# Pruning: Removing a whole section of a tree
# Grafting: Adding a whole section to a tree
# Finding the root for any node
# Finding the lowest common ancestor of two nodes


# Traversal and search methods :

# Stepping through the items of a tree, by means of the connections between parents and children, 
# is called walking the tree, and the action is a walk of the tree. 
# Often, an operation might be performed when a pointer arrives at a particular node. 
# A walk in which each parent node is traversed before its children is called a pre-order walk; 
# a walk in which the children are traversed before their respective parents are traversed is called a post-order walk;
#  a walk in which a node's left subtree, then the node itself, and finally its right subtree are traversed is called an in-order traversal. 
# (This last scenario, referring to exactly two subtrees, a left subtree and a right subtree, assumes specifically a binary tree.)
#  A level-order walk effectively performs a breadth-first search over the entirety of a tree; nodes are traversed level by level, 
# where the root node is visited first, followed by its direct child nodes and their siblings, 
# followed by its grandchild nodes and their siblings, etc., until all nodes in the tree have been traversed.

#HW -> Revise trees theory