class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, item): # insert item on queue
        # create a new LinkedLIstNode
        new_node = LinkedListNode(item)
        # if the queue is empty (point both ends to new_node)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        # add new node to the rear
        # make sure the old rear, points to the new node
        else:
            self.rear.next = new_node
            # make the rear point to new_node
            self.rear = new_node


    def dequeue(self): # delete item on queue
        if self.front is None: # putting this in for check because we can't delete an empty queue
            return None
        # store a temp variable so we dont lose our node
        old_front = self.front
        # move the front pointer, to the next node over
        self.front - self.front.next # old_front.next will also work
        # special case: if the queue should now be empty
        if self.front is None:
            self.rear = None

my_queue = Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print(f"front: ",my_queue.front.data)
print(f"rear: ",my_queue.rear.data)