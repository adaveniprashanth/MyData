'''
A doubly linked list is a type of linked list in which each node consists of 3 components:

*prev - address of the previous node
data - data item
*next - address of next node
'''
'''
Insertion on a Doubly Linked List
Pushing a node to a doubly-linked list is similar to pushing a node to a linked list, but extra work is required to handle the pointer to the previous node.

We can insert elements at 3 different positions of a doubly-linked list:
1.Insertion at the beginning
2.Insertion in-between nodes
3.Insertion at the End
'''

if 1:
    import gc


    # node creation

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None


    class DoublyLinkedList:

        def __init__(self):
            self.head = None

        # insert node at the front
        def insert_front(self, data):

            # allocate memory for newNode and assign data to newNode
            new_node = Node(data)

            # make newNode as a head
            new_node.next = self.head

            # assign null to prev (prev is already none in the constructore)

            # previous of head (now head is the se.cond node) is newNode
            if self.head is not None:
                self.head.prev = new_node

            # head points to newNode
            self.head = new_node

        # insert a node after a specific node
        def insert_after(self, prev_node, data):

            # check if previous node is null
            if prev_node is None:
                print("previous node cannot be null")
                return

            # allocate memory for newNode and assign data to newNode
            new_node = Node(data)

            # set next of newNode to next of prev node
            new_node.next = prev_node.next

            # set next of prev node to newNode
            prev_node.next = new_node

            # set prev of newNode to the previous node
            new_node.prev = prev_node

            # set prev of newNode's next to newNode
            if new_node.next:
                new_node.next.prev = new_node

        # insert a newNode at the end of the list
        def insert_end(self, data):

            # allocate memory for newNode and assign data to newNode
            new_node = Node(data)

            # assign null to next of newNode (already done in constructor)

            # if the linked list is empty, make the newNode as head node
            if self.head is None:
                self.head = new_node
                return

            # store the head node temporarily (for later use)
            temp = self.head

            # if the linked list is not empty, traverse to the end of the linked list
            while temp.next:
                temp = temp.next

            # now, the last node of the linked list is temp

            # assign next of the last node (temp) to newNode
            temp.next = new_node

            # assign prev of newNode to temp
            new_node.prev = temp

            return

        # delete a node from the doubly linked list
        def deleteNode(self, dele):

            # if head or del is null, deletion is not possible
            if self.head is None or dele is None:
                return

            # if del_node is the head node, point the head pointer to the next of del_node
            if self.head == dele:
                self.head = dele.next

            # if del_node is not at the last node, point the prev of node next to del_node to the previous of del_node
            if dele.next is not None:
                dele.next.prev = dele.prev

            # if del_node is not the first node, point the next of the previous node to the next node of del_node
            if dele.prev is not None:
                dele.prev.next = dele.next

            # free the memory of del_node
            gc.collect()

        # print the doubly linked list
        def display_list(self, node):

            while node:
                print(node.data, end="->")
                last = node
                node = node.next


    # initialize an empty node
    d_linked_list = DoublyLinkedList()

    d_linked_list.insert_end(5)
    d_linked_list.insert_front(1)
    d_linked_list.insert_front(6)
    d_linked_list.insert_end(9)

    # insert 11 after head
    d_linked_list.insert_after(d_linked_list.head, 11)

    # insert 15 after the seond node
    d_linked_list.insert_after(d_linked_list.head.next, 15)

    d_linked_list.display_list(d_linked_list.head)

    # delete the last node
    d_linked_list.deleteNode(d_linked_list.head.next.next.next.next.next)

    print()
    d_linked_list.display_list(d_linked_list.head)
