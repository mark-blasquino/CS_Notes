""" 
given a string, return the number of 'lambdas' that can be constructed
"""
import sys

def csMaxNumberOfLambdas(text):
    len1 = len(text)
    len2 = len('lambda')
    ans = sys.maxsize
    # initialize hash for both strings
    hash1 = [0] * 26
    hash2 = [0] * 26
    # hash the frequency of letters of text
    for i in range(0, len1):
        hash1[ord(text[i]) - 97] = hash1[ord(text[i]) - 97] + 1
    # hash the frequency of letters of 'lambda'
    for i in range(0, len2):
        hash2[ord('lambda'[i]) - 97] = hash2[ord('lambda'[i]) - 97] + 1
    # find the count of 'lambda' constructed from text
    for i in range(0, 26):
        if (hash2[i] != 0):
            ans = min(ans, hash1[i] // hash2[i])
    return ans