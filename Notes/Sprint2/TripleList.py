def triple_list_in_place(int_list):
    for i in range(len(int_list)): # go over every item in loop
        int_list[i] *= 3 # multiply every item to 3

    # No return statement because we've modified the original list in place
    # There is no need to return another reference to the same list

def triple_list_out_of_place(int_list):
    # Allocate a new list with enough room for all of the elements
    tripled_list = [None] * len(int_list)

    for i in range(len(int_list)):
        tripled_list[i] = int_list[i] * 3
    
    return tripled_list

num_list = [1,2,3,4,5]
print(num_list)

# triple_list_in_place(num_list)
# print(num_list) # modified existing list

new_list = triple_list_out_of_place(num_list)
print(num_list) 
print(new_list) # created a new list 