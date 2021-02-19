""" 
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, 
since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. 
Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity 
of visualization: in real data you will be given a head node l of the linked list
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def insertValueIntoSortedLinkedList(l, value):
    value = ListNode(value) # convert int value to node by using the pre-defined class ListNode

    # special case for head end
    if l is None or l.value >= value.value:
        value.next = l
        l = value
        return l
    
    # locate the node before the poof insertion
    current = l
    while current.next and current.next.value < value.value:
        current = current.next
        
    value.next = current.next
    current.next = value
    
    return l