"""
Challenge #3:

Given a string of numbers separated by a comma and space, 
return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!

Understand:
given string
numbers ",_" separator
need to multiply all nums in string
edge cases:
    can have negative decimals? - no
    one number? - sure
    empty string? - no

Plan:
- convert input into numbers
- maybe array
- use .split(",_")
- multiply array of nums
    - final_val = 1
    - for loop over all nums
    - (each num) turn into int
    - multiply into final_val
"""


def multiply_nums(nums):
    # Your code here
    nums_array =  nums.split(', ')
    final_val = 1
    for num in nums_array:
        final_val *= int(num)
    return final_val
