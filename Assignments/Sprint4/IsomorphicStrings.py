""" 
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character but a character may map to itself.
"""

def csIsomorphicStrings(a, b):
    if len(a) != len(b):
        return False
    return len(set(a)) == len(set(b)) == len(set(zip(a,b)))