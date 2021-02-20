# implement a stack using an array instead of Linked List
# use this for pushing and popping items, as it's worst case is only O(1), and can be used in stressful situations for simple tasks

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0: # sanity check
            return None
        last_item = self.items.pop()
        return last_item