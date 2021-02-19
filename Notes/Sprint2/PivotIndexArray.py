"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
​
The "pivot" index is where the sum of all the numbers on the left of that index is equal 
to the sum of all the numbers on the right of that index.
​
If the input array does not have a "pivot" index, then the function should return `-1`. 
If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
​
Example 1:
​
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal 
to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
​
Example 2:
​
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

---UPER----
Understand:
    - input = array of ints
    return a number (an index) if found
    return -2 otherwise

Plan:
    - serch through the array to find pivot index (go through)
    is index i a pivot index?
        get sum of left subarray
        get sum of right subarray
        and compare
            if true:
                return index(i)
            if false:
                keep looking
    return -1 (if cannot find anything)

Plan (more optimal code):
    Lsum = 0, Rsum = 27 (sum of all numbers)

    start with
        Lsum = 0
        Rsum = sum(nums[1:]) --- done outside of loop

"""
def pivot_index_old(nums):
    # search through nums list for a pivot index
    # go through each item in nums
    for i in range(len(nums)): # O(n^2)
        # check if current index (i) is the pivot index
        left_subarray = nums[0:i] # or [:i] ### will go upto i but will not include i
        right_subarray = nums[i+1:]
        # get sum of left subarray
        left_sum = sum(left_subarray) # O(n)
        # get sum of right subarray
        right_sum = sum(right_subarray) # O(n)
        # check if they are equal
        if left_sum == right_sum:
            return i
        # if equal, return I
    
    return -1
​
def pivot_index_left_right(nums):
    # create Lsum and Rsum
    l_sum = 0
    r_sum = sum(nums[1:])
​
    # search through the array and check if index is pivot index
    for i in range(len(nums)):
        # check if l_sum == r_sum
        if l_sum == r_sum:
            return i
        # add number at current index to left sum
        l_sum += nums[i]
        # check that we are not at the last index (so we dont overflow in the array)
        if (i+1 == len(nums)):
            r_sum = 0
        else:
            r_sum -= nums[i+1]
​
    return -1
​
​
​
def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
​
    # as we go through the array, update left_sum
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i] 
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
​
    return -1
​
​
​
​
print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([]))