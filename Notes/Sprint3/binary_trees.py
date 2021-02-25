""" 
In-Order:
    - go left
    - print
    - go right
Pre-Order
    - print
    - go left
    - go right
Post-Order
    - go left
    - go right
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

    def print_tree_iter(self):
        stack = [] # DFT
        # push the first node onto stack
        stack.append(self) # add first item
        while len(stack) > 0: # loop until stack is empty
            top_item = stack.pop() # always pop current item
            # do things to the current item
            print(top_item.value) # whatever you want need to do per node (print, return, add to str, convert to arr, etc)

            ## Push the children onto stack
            # go right
            if top_item.right:
                stack.append(top_item.right )
            # go left
            if top_item.left:
                stack.append(top_item.left) 


    def print_tree_bft(self):
        queue = [] # BFT
        # push the first node onto stack
        queue.insert(0, self) # add first item
        while len(queue) > 0: # loop until stack is empty
            top_item = queue .pop() # always pop current item
            # do things to the current item
            print(top_item.value) # whatever you want need to do per node (print, return, add to str, convert to arr, etc)

            ## Push the children onto stack
            # go right
            if top_item.right:
                queue.insert(0, top_item.right )
            # go left
            if top_item.left:
                queue.append(0, top_item.left) 


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