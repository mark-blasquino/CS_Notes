""" 
In-Order:
    - go left
    - print
    - go right
Pre-Order
    - print
    - go right
    - go left
Post-Order
    - go right
    - go left
    - print
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            # the value must go right    
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)

    def search(self, target):
        if target == self.value:
            # we have found the item
            return True
        if target < self.value:
            # Search the left side of the tree
            if self.left is None:
                return False
            else:
            # if a node exists to the left, call search on that node
                return self.left.search(target)
        
        else:
            # Search the right side of the tree
            if self.right is None:
                return False
            else:
                return self.right.search(target)

    # In-order Traversal
    def print_tree(self):
        # go left
        if self.left is not None:
            self.left.print_tree()
        # do things to current node
        print(self.value)
        # go right
        if self.right is not None:
            self.right.print_tree()


root = BSTNode(8)
root.insert(5)
root.insert(7)
root.insert(12)
root.insert(11)


print(root.search(7))
print(root.search(9))

root.insert(9)
print(root.search(9))

root.print_tree()