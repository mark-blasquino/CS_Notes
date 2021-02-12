"""
Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>" or "pop". 
Return an array composed of the results of each "pop" operation that is performed.

Example

For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, 
"pop", and add the first element of the queue 1 to the answer array. The queue becomes {2}. After the 
fourth request, the queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and 
the queue becomes {3}.
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        # transfer everything from left to right
        while not left.isEmpty():
            right.push(left.pop())
        # at this point, the first item inserted in left is now the last element in right
        deleted = right.pop()
        # transfer everything to left
        while not right.isEmpty():
            left.push(right.pop())
        return deleted

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans
