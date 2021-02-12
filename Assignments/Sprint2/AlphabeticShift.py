"""
Given a string, your task is to replace each of its characters by the next one in the 
English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
"""

def alphabeticShift(inputString):
    alphabet_list = list('abcdefghijklmnopqrstuvwxyzabc')
    output_string = []
    for letter in inputString:
        if letter == 'z':
            output_string.append('a')
        else:
            letter_index = alphabet_list.index(letter) + 1
            output_string.append(alphabet_list[letter_index])
        new_word = "".join(output_string)
    
    return new_word