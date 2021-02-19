# my_dict = {
#     'apple': 'apple is a fruit',
#     'banana': 'banana is a fruit',
#     'peach': 'fruit',
#     'cucumber': 'vegetable',
# }
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity            

    def my_hash(self, key):
        # do stuff to convert this str to a number
        bytes_str = key.encode()
        bytes_sum = 0
        for byte in bytes_str:
            bytes_sum += byte

        return bytes_sum % self.capacity 

    def insert(self, key, value):
        # convert the key to an index for our storage  
        index = self.my_hash(key)
        print(f'{key} hashed to {index}')
        # Store the value in storage 
        self.storage[index] = value

    def get(self, key):
        # convert the key to an index for our storage  
        index = self.my_hash(key) 
        return self.storage[index]


my_dict = HashTable(8)

my_dict.insert('banana', 'banana is a fruit')
# my_dict['banana'] = 'banana is a fruit'
# print my_dict['banana']
my_dict.insert('apple', 'apple is also a fruit')
my_dict.insert('cucumber', 'cucumber is a vegetable')
my_dict.insert('tomato', 'no one can agree on tomato')

# print(my_dict.get('banana'))
# print(my_dict.get('apple'))
# print(my_dict.get('tomato'))
# print(my_dict.get('cucumber'))

my_dict.insert('peach', 'Definitely not a banana')

print(my_dict.get('banana'))
