"""
Given a sorted array (in ascending order) of integers and a target, 
write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.
"""

def csSortedTwoSum(numbers, target):
    num_dict = {}
    for i in range(len(numbers)):
        num_dict[numbers[i]] = i
        
    for i in range(len(numbers)):
        current_num = numbers[i]
        compliment = target - current_num
        
        if compliment in num_dict and i != num_dict[compliment]:
            return [i, num_dict[compliment]]