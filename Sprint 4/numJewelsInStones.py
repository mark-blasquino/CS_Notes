""" 
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Understand
jewels = "aA", stones = "aAAbbbb"
output: 3

Plan
j = {a, A}

1. make a set out of jewels
2. go through stones and count how many stones are jewels

Runtime: O(S + J)

"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        numJewels = 0
        for stone in stones:
            if stone in jewels:
                numJewels += 1
        return numJewels



jewels = 'aA'
stones = 'aAAbbbb'