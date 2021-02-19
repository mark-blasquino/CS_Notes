
# Linear Search
def linear_search(arr, target):
    # pass
    for i in range(len(arr)):
        current_num = arr[i]
        if current_num == target:
            return i
    
    return -1



def linear_search(arr, item, current_index):
    if current_index >= len(arr):
        return -1

    if arr[current_index] == item:
        return current_index

    return linear_search(arr, item, current_index + 1)

    




our_array = [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]

result = linear_search(our_array, 14, 0))
