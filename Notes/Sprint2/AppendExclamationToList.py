# In-Place Function

def append_exclamations(str_list):
    for idx, item in enumerate(str_list):
        str_list[idx] += "!"

Mylist = ["Matt", "Beej", "Sean"]
append_exclamations(Mylist)
print(Mylist)

# Out-of-Place

def append_exclamations(str_list):
    # Create a new empty list that has the same length as the input list
    loud_list = [None] * len(str_list)
    for idx, item in enumerate(str_list):
        # insert the modified string into the new list
        loud_list[idx] = item + "!"
    # Since we didn't modify the input list, we need to return the new list to
    # the function caller
    return loud_list

print(Mylist)