'''
3.Queue Data structure:
    Unlike stack, the queue data structure works in the FIFO principle 
    where first element stored in the queue will be removed first.
'''
if 1:
    # Queue implementation in Python
    class Queue:
        def __init__(self):
            self.queue = []

        # Add an element
        def enqueue(self, item):
            self.queue.append(item)
        # Remove an element
        def dequeue(self):
            if len(self.queue) < 1:
                return None
            return self.queue.pop(0)

        # Display  the queue
        def display(self):
            print(self.queue)
        def size(self):
            return len(self.queue)

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    q.display()
    q.dequeue()

    print("After removing an element")
    q.display()

'''
There are four different types of queues:

1.Simple Queue
2.Circular Queue
3.Priority Queue
4.Double Ended Queue
'''
