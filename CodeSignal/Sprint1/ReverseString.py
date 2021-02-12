"""
Given a string (the input will be in the form of an array of characters), 
write a function that returns the reverse of the given string.

Examples:

csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> 
["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
Notes:

Your solution should be "in-place" with O(1) space complexity. Although many in-place 
functions do not return the modified input, in this case you should.
You should try using a "two-pointers approach".
Avoid using any built-in reverse methods in the language you are using 
(the goal of this challenge is for you to implement your own method).
"""

def csReverseString(chars):
    return chars[::-1]