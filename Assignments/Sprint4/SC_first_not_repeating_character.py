""" 
Given a string s consisting of small English letters, find and return 
the first instance of a non-repeating character in it. If there is no 
such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. 
Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.
"""

def first_not_repeating_character(s):
    res = "_"
    d = {}
    for i, c in enumerate(s):
        if c in d.keys():
            d[c] = -1
        else:
            d[c] = i
    min_key = len(s)+1
    for k in d.keys():
        if d[k]>=0:
            min_key = min(min_key,d[k])
            res = s[min_key]
    return res