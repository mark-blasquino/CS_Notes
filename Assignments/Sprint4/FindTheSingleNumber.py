""" 
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.
"""

def csFindTheSingleNumber(nums):
    unique_nums = set(nums)
    for element in unique_nums:
        count = nums.count(element)
        if count == 1:
            return element