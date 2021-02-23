""" 
runtime = Log(n) (in between constant and linear)
"""

our_array = [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]


def binary_search(arr, target):
    # declare our search space
    start_index = 0 # min
    end_index = len(arr) - 1 # max

    # keep modifying our search space, until its either invalid, or we found our target
    while start_index <= end_index:
        # Keep guessing, checking, and shrinking our space
        middle_index = (end_index + start_index) // 2 # mid -- round down -- this makes it logarithmic, dividing the steps into half
        # check if the guess is our value, or if its greater or less than our value
        if arr[middle_index] == target:
            return middle_index

        # shrink your search space accordingly
        # the guess is smaller than your target
        if arr[middle_index] < target:
            # move the start_index to the middle
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
        
    return -1



print(binary_search(our_array, 2)) # 9

our_string_array = ['a', 'b', 'c', 'd','e']

print(binary_search(our_string_array, 'e'))


















