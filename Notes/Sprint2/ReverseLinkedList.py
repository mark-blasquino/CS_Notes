"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None


def reverse(head_of_list):
    # Your code here
    current_node = head_of_list
    previous_node = None
    next_node = None

    while current_node: #is not None by default or is existing
        # set the next_node, preserving access
        next_node = current_node.next

        # make current node, point to previous node
        current_node.next = previous_node

        # Shift the current and previous pointers to the right
        previous_node = current_node
        current_node = next_node

    return previous_node


def print_list(head_of_list):
    # start at head as current_node
    # iterate through list, printing the values
    current_node = head_of_list
    return_str = ''
    while current_node:
        return_str += f'({current_node.value}) -> '
        # move current node forward
        current_node = current_node.next

    print(return_str)


head = LinkedListNode(4)
head.next = LinkedListNode(3)
head.next.next = LinkedListNode(2)
head.next.next.next = LinkedListNode(1)

print_list(head)
new_head = reverse(head)
print_list(new_head)