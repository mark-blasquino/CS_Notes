"""
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

csCheckPalindrome("racecar") -> true
csCheckPalindrome("anna") -> true
csCheckPalindrome("12345") -> false
csCheckPalindrome("12321") -> true
Notes:

Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and make the necessary comparisons.
Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?
def csCheckPalindrome(input_str):
    return input_str == "".join(reversed(input_str))
"""

def csCheckPalindrome(input_str):
    for i in range(0, int(len(input_str)/2)):
        if input_str[i] != input_str[len(input_str)-i-1]:
            return False
        return True