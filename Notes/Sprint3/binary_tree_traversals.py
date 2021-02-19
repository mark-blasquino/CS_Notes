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

    # Recursive Pre-order DFS
    def print_tree(self):
        # do things to current node
        print(self.value)

        # go left
        if self.left is not None:
            self.left.print_tree()

        # go right
        if self.right is not None:
            self.right.print_tree()

    def print_tree_dfs(self):
        stack = []
        # push the first node onto stack     
        stack.append(self)

        while len(stack) > 0:

            top_item = stack.pop()
            
            # do things to the current item
            print(top_item.value)
            
            # go right
            if top_item.right:
                stack.append(top_item.right)

            # go left
            if top_item.left:
                stack.append(top_item.left)

    def print_tree_bft(self):
        queue = []
        # push the first node onto stack     
        queue.insert(0, self)

        while len(queue) > 0:

            top_item = queue.pop()

            # do things to the current item
            print(top_item.value)
            
            # go right
            if top_item.right:
                queue.insert(0, top_item.right)

            # go left
            if top_item.left:
                queue.insert(0, top_item.left)



root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(9)

print("Print Tree Recursive DFS")
root.print_tree()
print("Print Tree BFT")
root.print_tree_bft()
