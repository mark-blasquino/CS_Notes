"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0
Notes:

The input integer will not be negative.
"""

def csReverseIntegerBits(n):
    result = 0
    while n:
        result = (result << 1) + (n & 1) ## << is left shift by 1
        n >>= 1
    return result