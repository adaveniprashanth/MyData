'''
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.

It is called a binary tree because each tree node has a maximum of two children.
It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.

The properties that separate a binary search tree from a regular binary tree is:

1.All nodes of left subtree are less than the root node
2.All nodes of right subtree are more than the root node
3.Both subtrees of each node are also BSTs i.e. they have the above two properties
'''

'''
Search Operation:
  The algorithm depends on the property of BST that if each left subtree has values below root and each right subtree has values above the root.

Insert Operation:
  Inserting a value in the correct position is similar to searching. 
  Because we try to maintain the rule that the left subtree is lesser than root and the right subtree is larger than root.

Deletion Operation:
  There are three cases for deleting a node from a binary search tree.
  1.Case I:
    In the first case, the node to be deleted is the leaf node. In such a case, simply delete the node from the tree.
  2.Case II:
    In the second case, the node to be deleted lies has a single child node. In such a case follow the steps below:
      a.Replace that node with its child node.
      b.Remove the child node from its original position.
  3.Case III:
    In the third case, the node to be deleted has two children. In such a case follow the steps below:
      a.Get the inorder successor of that node.
      b.Replace the node with the inorder successor.
      c.Remove the inorder successor from its original position.
'''
