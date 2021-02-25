""" 
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.
"""
def csFindTheSingleNumber(nums):
    once = 0
    twice = 0
    for i in range(len(nums)):
        # once and nums[i] gives the bits that are there in both 'once' and new element
        # from nums[]. we add these bits to 'multi' using bitwise or
        twice = twice | once & nums[i]
        once =  once ^ nums[i]
        # the common bits are those biths which appear 3rd time. So these biths should not
        # be there in both 'once' and 'twice'. common_bit_mask contains all these bits as 0,
        # so that the bits can be removed from 'once' and 'twice'
        common_bit_mask = ~(once & twice)
        # remove common bith (the biths that appear 3 times) from 'once'
        once &= common_bit_mask
        # remove common bith (the biths that appear 3 times) from 'twice'
        twice &= common_bit_mask
    return once