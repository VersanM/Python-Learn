### Hash Tables in Python

# to run this file, use the command:
# python3 2_data_structures/2_hash_tables.py

my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict)

my_dict[4] = "four" # Add
print(f'Dictionary after ADD: {my_dict}')
my_dict[1] = "ONE" # Update
print(f'Dictionary after UPDATE: {my_dict}')
del my_dict[4]
print(f'Dictionary after DELETE: {my_dict}')

print(f'Value of key 1: {my_dict[1]}')

print(f'Dictionary keys: {my_dict.keys()}')
print(f'Dictionary values: {my_dict.values()}')

## Hash tables
# a Hash Function performs hashing by turning any data into a fixed-size sequence of bytes called the hash value/hash code
# it is a number (like a digital fingerprint) - usually much smaller than the original data

# Python's built in hash()
h = hash(3.14)
print(f'hash(3.14) => {h}')

h = hash(3.14159265358979323846264338327950288419716939937510)
print(f'hash(3.14159265358979323846264338327950288419716939937510) => {h}')

h = hash('Mihai')
print(f'hash(\'Mihai\') => {h}')

h = hash('Mihai is learning Python right now')
print(f'hash(\'Mihai is learning Python right now\') => {h}')

# Hash table VS Hash map
# Hash table is synchronized + fast + allows null key and more than one null value
# Hash map is non-synchronized + slow + does not allow null keys or values


