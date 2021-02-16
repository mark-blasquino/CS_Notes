"""
Given a number, write a function that converts that number into a string that contains 
"raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly 
divides into another number, leaving no remainder. The simplest way to test if one number is a 
factor of another is to use the modulo operator.

Here are the rules for csRaindrop. If the input number:

has 3 as a factor, add "Pling" to the result.
has 5 as a factor, add "Plang" to the result.
has 7 as a factor, add "Plong" to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.
Examples:

csRaindrops(28) -> "Plong"
28 has 7 as a factor, but not 3 or 5.
csRaindrops(30) -> "PlingPlang"
30 has both 3 and 5 as factors, but not 7.
csRaindrops(34) -> "34"
34 is not factored by 3, 5, or 7.
"""

def csRaindrops(number): # First, number is passed into the method convert.
    output = '' # Then the variable output is declared as an empty string.
    # If the remainder of number / 3 is 0 (meaning that 3 is a factor), we append ‘Pling’ to the string. Same for 5 and 7.
    if number % 3 == 0: # modulo operator is %; modulo operator returns the remainder
        output += 'Pling'
    if number % 5 == 0:
        output += 'Plang'
    if number % 7 == 0:
        output += 'Plong'
    # Then we come to that last task… if the number does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
    if output is '':
        return str(number)
    return output