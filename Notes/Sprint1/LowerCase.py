"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*

UPER
- convert characters to ascii
-  "a" to ascii -> 97, "z" -> 122
- how to tell if char is lowercase?
    - ascii numbers between 97 to 122 are lowercase letters
- "A" -> 65, "Z" -> 90
    - ascii numbers 65 -90 are uppercase letters
- 32 alphabets + characters before start of lowercase: add 32 from uppercase chars to get lowercase counterpart 
"""
def to_lower_case(string):
    # create empty answer_string
    answer_string = ""
    # loop through each char of input_string
    for char in string:
        # for each char convert to ascii
        ascii_char = ord(char) # ord casts to ascii
        # check if number is between 65 and 90 (uppercase)
        if 65 <= ascii_char <= 90: 
            #  the letter is uppercase, so lets convert to lower
            lower_char_num = ascii_char + 32
            #  convert the new ascii num back to character
            lower_char = chr(lower_char_num) # chr casts back to character
            #  add lower_char to our answer_string
            answer_string += lower_char
        else:
            # add the character to answer_string
            answer_string += char

    return answer_string


print(to_lower_case('LambdaSchool'))
print(to_lower_case('LLAMA'))