"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. 
Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
"""

openBrackets = ["[", "(", "{"]
closedBrackets = ["]", ")", "}"]

def validBracketSequence(sequence):
    stack = []
    for i in sequence:
        if i in openBrackets:
            stack.append(i)
        elif i in closedBrackets:
            pos = closedBrackets.index(i)
            if ((len(stack) > 0) and (openBrackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False