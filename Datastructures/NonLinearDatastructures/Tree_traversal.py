# Traversing a tree means visiting every node in the tree.

'''
Linear data structures like arrays, stacks, queues, and linked list have only one way to read the data. 
But a hierarchical data structure like a tree can be traversed in different ways.
'''

'''
Types of traversal:
1.Inorder: (left -> root -> right)
2.Preorder: (root -> left -> right)
3.postorder: (left -> right -> root)
'''

# Tree traversal
if 1:
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

    def inorder(root):
        if root:
            inorder(root.left)
            print(root.data,end=" ")
            inorder(root.right)

    def preorder(root):
        if root:
            print(root.data,end=" ")
            preorder(root.left)
            preorder(root.right)

    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.data,end=" ")

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    inorder(root)
    preorder(root)
    postorder(root)
