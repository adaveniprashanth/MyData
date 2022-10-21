'''
A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.
It is also known as a proper binary tree.
'''

# Checking if a binary tree is a full binary tree in Python
if 1:
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

    def isFullBinaryTree(root):

        # if tree is empty
        if root is None:
            return True

        # if we have only root element
        if root.left is None and root.right is None:
            return True

        # if we have multiple elements
        if root.left is not None and root.right is not None:
            return isFullBinaryTree(root.left) and isFullBinaryTree(root.right)

        return False

    root = None
    print(isFullBinaryTree(root))

    root = Node(1)
    print(isFullBinaryTree(root))

    root.left = Node(2)
    root.right = Node(3)
    print(isFullBinaryTree(root))

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    # root.right.left = Node(7) # uncomment this line to make full binary tree
    print(isFullBinaryTree(root))
