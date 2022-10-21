'''
Binary Tree:
  A binary tree is a tree data structure in which each parent node can have at most two children. Each node of a binary tree consists of three items:
  1.data item
  2.address of left child
  3.address of right child

Types of Binary Tree:
1.Full Binary Tree:
  A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.

2.Perfect Binary Tree:
  A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

3.Complete Binary Tree:
  A complete binary tree is just like a full binary tree, but with two major differences.
  a.Every level must be completely filled
  b.All the leaf elements must lean towards the left.
  c.The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.
  
4.Degenerate or Pathological Tree:
  A degenerate or pathological tree is the tree having a single child either left or right.

5.Skewed Binary Tree:
  A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes.
  Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

6.Balanced Binary Tree:
  It is a type of binary tree in which the difference between the height of the left and the right subtree for each node is either 0 or 1.
'''

# Binary Tree in Python
if 1:
    class Node:
        def __init__(self,value):
            self.left = None
            self.right = None
            self.data = value

    def traversePreOrder(root):
        if root:
            print(root.data)
            traversePreOrder(root.left)
            traversePreOrder(root.right)

    def traverseInOrder(root):
        if root:
            traverseInOrder(root.left)
            print(root.data)
            traverseInOrder(root.right)

    def traversePostOrder(root):
        if root:
            traversePostOrder(root.left)
            traversePostOrder(root.right)
            print(root.data)

    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    traverseInOrder(root)
    print()
    traversePreOrder(root)
    print()
    traversePostOrder(root)
