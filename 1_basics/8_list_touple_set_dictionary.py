### Exceptions

# to run this file, use the command:
# python3 1_basics/8_list_touple_set_dictionary.py

print("---------List---------")
list1 = ["String", 100, 11.1, 'c', True]
print(list1)

list1[0] = "New Text"
print(list1)


print("---------Touple---------")
touple1 = ("String", 100, 11.1, 'c', True) # imutable
print(touple1)

# touple1[0] = "NewString" # not gonna work - Touples are immutable

print("---------Set---------")
set1 = set(["String", 100, 11.1, 'c', True])
print(set1)
set1.add("String")
print(set1)
set1 = {"String", 100, 11.1, 'c', True}
print(set1)

print("---------Dictionary---------")
dict1 = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday'
}
print(dict1)