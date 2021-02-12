"""
Given a string, write a function that returns the index of the first unique (non-repeating) 
character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.
"""
def csFirstUniqueChar(input_str):
    for item in input_str:
        if input_str.count(item) == 1:
            return input_str.index(item)
    return -1