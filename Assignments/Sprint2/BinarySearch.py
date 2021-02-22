"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search for target in nums. If target exists, then return its index, otherwise, 
return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

All elements in nums are unique.
The length of nums will be <= 100
The value of each element in nums will be in the range [1, 10000]

"""

def csBinarySearch(nums, target):
    min, max = 0, len(nums) - 1
    while min <= max:
        mid = int((min + max) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
    return -1

my_nums = [1,3,4,6,7,12,26,90,104]
my_target = 26

print(csBinarySearch(my_nums, my_target))