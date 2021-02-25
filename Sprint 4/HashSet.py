### Design HashSet ###
""" 
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""

from collections import deque

class MyHashSet:
    """ 
    Understand
    mySet = MyHashSet()
    mySet.add(1){1}
    mySet.add(2){1,2}
    mySet.contains(1) True
    mySet.remove(1) {2}
    mySet.contains(1) False
    mySet.contains(2) True

    Plan
    Init
        Initialize the list with a static size
    Add
        Run key through hash function and store key in
        the list using the index from the hash function
    Contains
        Run key through hash function to get hashIndex
        Check list at hashIndex to see if something is stored there
    Remove
        Run key through hash function. Make value at hashIndex
        to None
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 10000

    def add(self, key: int) -> None:
        hashIndex = hash(key) % len(self.table)
        if self.table[hashIndex] == None:
            newList = deque()
            newList.append(key)
            self.table[hashIndex] = newList
        elif key not in self.table[hashIndex]:
            self.table[hashIndex].append(key)

    def remove(self, key: int) -> None:
        hashIndex = hash(key) % len(self.table)
        if self.table[hashIndex] != None:
            try:
                self.table[hashIndex].remove(key)
            except:
                pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashIndex = hash(key) % len(self.table)
        if return self.table[hashIndex] != None:
            return key in self.table[hashIndex]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)