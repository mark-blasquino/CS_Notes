"""
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
"""

def csRemoveTheVowels(input_str):
    return (re.sub("[aeiouAEIOU]","",input_str))