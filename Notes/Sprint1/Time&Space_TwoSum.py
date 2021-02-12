"""
Given an array of integers 'nums' and an integer 'target', return the indices
of the two numbers that add up to the 'target'.

Examples:
- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] = nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] = nums[2] == 8)

Notes:
- No negative numbers and no zero in array or target
- Return None if no answer
- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.


Plan:
- Brute force:
    2 loops to generate all pairs
    loop for each num_1 in nums: O(n)
        loop num_2 in nums starting at index + 1 O(n)
            num_1 + num_2

O(n^2) runtime for brute force attempt

2nd attempt:
[2,5,9,13]
is there a 5? where is it?
1 - build a dictionary 
    loop: each num: index insert into dict
2 - find the two numbers
    for each num is there a matching number (compliment) - where is it?

O(n) runtime
space complexity = 


"""
# First Attempt
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             num1 = nums[i]
#             num2 = nums[j]
#             if num1 + num2 == target:
#                 return [i, j]
#     return None

# Second Attempt
def two_sum(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i

    for i in range(len(nums)):
        current_num = nums[i]
        # check if the compliment is in dict
        compliment = target - current_num

        if compliment in num_dict and i != num_dict[compliment]:
            #compliment exists! return its index
            return [i, num_dict[compliment]]

print(two_sum(nums = [2,5,9,13], target = 7))