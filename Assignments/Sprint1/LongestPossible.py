"""
Given two strings that include only lowercase alpha characters, 
str_1 and str_2, write a function that returns a new sorted string that contains any character 
(only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
"""

def csLongestPossible(str_1, str_2):
    concat = (str_1 + str_2)
    unique_str = set(concat)
    sorted_str = sorted(unique_str)
    return ''.join(sorted_str)