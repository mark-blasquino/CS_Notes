""" 
Note: Your solution should have O(l1.length + l2.length) time complexity, 
since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is 
to merge them. In other words, return a singly linked list, also sorted in 
non-decreasing order, that contains the elements from both original lists.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    # create a temp node None
    temp = None
    
    # l1 is empty then return l2
    if l1 is None:
        return l2
    
    # l2 is empty then return l1
    if l2 is None:
        return l1
    
    # if l1's data is smaller or equal to l2's data
    if l1.value <= l2.value:
        # assign temp to l1's data
        temp = l1
        # again check l1's data is smaller or equal l2's data and call the merge function
        temp.next = mergeTwoLinkedLists(l1.next, l2)
    else:
        # if l2's data is greater than or equal to l1'ss data assign temp to l2
        temp = l2
        # again check l2's data is greater than or equal l1's data and call the merge function
        temp.next = mergeTwoLinkedLists(l1, l2.next)
    # return the temp list
    return temp