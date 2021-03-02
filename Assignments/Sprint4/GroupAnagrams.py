""" 
Given an array of strings strs, write a function that can group the anagrams. 
The groups should be ordered such that the larger groups come first, 
with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.
"""

def csGroupAnagrams(strs):
    result = {}
    for i in strs:
        x = "".join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]
    return list(result.values())