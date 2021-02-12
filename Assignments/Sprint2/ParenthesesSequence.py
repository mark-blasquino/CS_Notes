"""
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
"""

opened = ["("]
closed = [")"]

def validParenthesesSequence(s):
    stack = []
    for i in s:
        if i in opened:
            stack.append(i)
        elif i in closed:
            pos = closed.index(i)
            if ((len(stack) > 0) and
                (opened[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False