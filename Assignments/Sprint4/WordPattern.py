""" 
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a 
one-to-one correspondence between a letter in pattern and a 
non-empty word in s.
"""
def csWordPattern(pattern, a):
    arr = a.split()
    if len(pattern)!=len(arr):
        return False
    my_dict = {}
    for i in range(len(pattern)):
        if pattern[i] not in my_dict:
            my_dict[pattern[i]] = arr[i]
        elif my_dict[pattern[i]] != arr[i]:
            return False
        else:
            pass
    my_dict2 = {}
    for j in range(len(arr)):
        if arr[j] not in my_dict2:
            my_dict2[arr[j]] = pattern[j]
        elif my_dict2[arr[j]] != pattern[j]:
            return False
        else:
            pass
    return True