"""
You are given a sorted array in ascending order that is rotated at some unknown pivot 
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present 
in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
"""

def findValueSortedShiftedArray(nums, target):
    n = len(nums)
    pivot = findPivot(nums, 0, n-1)
    
    if pivot == -1:
        return binarySearch(nums, 0, n-1, target)
        
    if nums[pivot] ==  target:
        return pivot
    if nums[0] <= target:
        return binarySearch(nums, 0, pivot-1, target)
    return binarySearch(nums, pivot + 1, n-1, target)
    
def findPivot(nums, min, max):
    min, max = 0, len(nums)
    
    if max < min:
        return -1
    if max == min:
        return min
        
    mid = int((min + max) / 2)
    
    if mid < max and nums[mid] > nums[mid + 1]:
        return mid
    if mid > min and nums[mid] < nums[mid - 1]:
        return (mid - 1)
    if nums[min] >= nums[mid]:
        return findPivot(nums, mid + 1, max)
        
def binarySearch(nums, min, max, target):
    
    if max < min:
        return -1
    
    mid = int((min + max) / 2)
    
    if target == nums[mid]:
        return mid
    if target > nums[mid]:
        return binarySearch(nums, (mid + 1), max, target)
    return binarySearch(nums, min, (mid - 1), target)