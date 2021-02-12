"""
Given a string, write a function that removes all duplicate words from the input. 
The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
"""

from collections import Counter

def csRemoveDuplicateWords(input_str):
    input_str = input_str.split(" ")
    for i in range(0, len(input_str)):
        input_str[i] = "".join(input_str[i])
        dupli = Counter(input_str)
        s = " ".join(dupli.keys())
        return s