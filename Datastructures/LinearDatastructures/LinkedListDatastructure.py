'''
4.Linked List Data structure:
    In linked list data structure, data elements are connected through a series of nodes. 
    And, each node contains the data items and address to the next node.
    Linked lists can be of multiple types: singly, doubly, and circular linked list.
'''

if 1:
    # Linked list implementation in Python

    class Node:
        # Creating a node
        def __init__(self, item):
            self.item = item
            self.next = None


    class LinkedList:

        def __init__(self):
            self.head = None


    if __name__ == '__main__':

        linked_list = LinkedList()

        # Assign item values
        linked_list.head = Node(1)
        second = Node(2)
        third = Node(3)

        # Connect nodes
        linked_list.head.next = second
        second.next = third

        # Print the linked list item
        while linked_list.head != None:
            print(linked_list.head.item, end=" ")
            linked_list.head = linked_list.head.next


'''
Here's a list of basic linked list operations that we will cover in this article.

Traversal - access each element of the linked list
Insertion - adds a new element to the linked list
Deletion - removes the existing elements
Search - find a node in the linked list
Sort - sort the nodes of the linked list
'''
