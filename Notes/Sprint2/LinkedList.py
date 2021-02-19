"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` 
from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.
"""

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(delete_this_node):
    # Your code here
    next_node = delete_this_node.next
    # copy all of next node into the current node we are "deleting"
    # start with the value
    if next_node is not None:
        delete_this_node.value = next_node.value
        # skip over the next_node in our linked list
        delete_this_node.next = next_node.next

    else:
        print("Sorry we cannot delete the last node using this technique")






x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)

""" 
Linked Lists Core Operations:
    - access
    - search
    - insert
    - delete
"""