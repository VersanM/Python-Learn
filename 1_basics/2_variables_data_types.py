### Variables and Data Types

# to run this file, use the command:
# python3 1_basics/2_variables_data_types.py

# Create a variable
x = 5
text = "Hello, World!"

# In Python everything is an object

# ┌──────────────┬──────────────┬────────────────────┐
# │ Type         │ Example      │ Class              │
# ├──────────────┼──────────────┼────────────────────┤
# │ Integer      │ 42           │ int                │
# │ Float        │ 3.14         │ float              │
# │ Boolean      │ True, False  │ bool               │
# │ String       │ 'hello'      │ str                │
# │ List         │ [1, 2, 3]    │ list               │
# │ Tuple        │ (1, 2)       │ tuple              │
# │ Dictionary   │ {'a': 1}     │ dict               │
# │ Set          │ {1, 2, 3}    │ set                │
# │ None         │ None         │ NoneType           │
# │ Function     │ def f():...  │ function           │
# │ Class        │ class X:...  │ type               │
# └──────────────┴──────────────┴────────────────────┘

# Examples of data types
print("-------Data Types-------")
myInt = 42
print(type(myInt))  # <class 'int'>
myFloat = 3.14
print(type(myFloat))  # <class 'float'>
myString = "Hello, World!"
print(type(myString))  # <class 'str'>
myBool = True
print(type(myBool))  # <class 'bool'>
myList = [1, 2, 3]
print(type(myList))  # <class 'list'>
myTuple = (1, 2)
print(type(myTuple))  # <class 'tuple'>
myDict = {"key": "value", "another_key": 42}
print(type(myDict))  # <class 'dict'>
mySet = {1, 2, 3}
print(type(mySet))  # <class 'set'>
myNone = None
print(type(myNone))  # <class 'NoneType'>
myFunction = lambda x: x + 1
print(type(myFunction))  # <class 'function'>
myClass = type("MyClass", (object,), {})
print(type(myClass))  # <class 'type'>


myInt = 4 * 11
print("myInt = " + str(myInt))

# Operations
print("-------Number Operations-------")
print("1+1=" + str(1 + 1)) # 2
print("11-1=" + str(11-1)) # 10
print("10*10=" +  str(10 * 10)) # 100
print("10/4=" + str(10/4)) # 2.5

# the result of division is always a float
x = 14 / 7
print("x = " + str(x))
print("x type: " + str(type(x)))

# modulo
y = 7 % 3 # 1
print("7 % 3 = " + str(y))

# exponential
z = 2 ** 3 # 2^3 = 8
print("2 ** 3 = " + str(z))

# paranthesis 
a = 1 + 3 * 2 # 7
print("1 + 3 * 2 = " + str(a))
a = (1 + 3) * 2 # 8
print("(1 + 3) * 2 = " + str(a))

# Boolean
print("-------Boolean-------")
b = True
print("b = " + str(b))
b = not b
print ("not b = " + str(b))

print("True and False => " + str(True and False))
print("True or False => " + str(True or False))

# True and False are actually 1 and 0 
print("True + True = " + str(True + True)) #2
print("True * 8 = " + str(True * 8)) #8
print("False - 5 = " + str(False - 5))

# None, 0 and empty strings/lists/dicts/tubles/sets are all evaluated as False 
b = bool(0) # False
b = bool("") # False
b = bool([]) # False
b = bool({}) # False
b = bool(()) # False
b = bool(set()) # False
b = bool(4) # True
b = bool(-6) # True

# is VS == (is - checks if 2 variables refer to the same object, but == checks if the objects pointed to have the same values)
a = [1, 2, 3, 4]
b = a
b is a # True (refer to the same object)
b == a # True (objects are equal)
b = [1, 2, 3, 4]
b is a # False (a and b do not refer to the same object)
b == a # True (objects are still equal)

# Strings 
print("-------Strings-------")
"Hello world!"
'Hello world!'
"Hello world!"[0] # => 'H'
len("Hello") # 5

# format strings
name = 'Mihai'
print(f"My name is {name}") # => "My name is Mihai"
print(f"{name} is {len(name)} characters long.")

# input data
print("-------Input Data-------")
input_string_var = input("Enter some data: ")
print(f"You entered: {input_string_var}")

# if as expression
"yay!" if 0 > 1 else "nay!" # "nay!"

# Lists
print("-------Lists-------")
myList = []
otherList = [4, 5, 6]

myList.append(1) # [1]
myList.append(2) # [1, 2]
myList.append(5) # [1, 2, 5]
myList.append(2) # [1, 2, 5, 2]

print(myList)

last_item = myList.pop() # 2

print(f"poped item: {last_item}") # 2
print(myList) # [1, 2, 5]

myList.append(2)
print(myList)

print(f"First item: {myList[0]}") # 1
print(f"Last item: {myList[-1]}") # 2

# print(f"Out of bounds error: {myList[3]}") # IndexError

# List ranges - start index is included, end index is not
print(f"List range 1:3 = {myList[1:3]}") # => [2, 5]
print(f"List range 2: = {myList[2:]}") # => [5, 2]
print(f"List range :3 = {myList[:3]}") # => [1, 2, 5]

# range with step => ::2 
print(f"List range with step ::2 = {myList[::2]}") # => [1, 5]
print(f"List range with step ::-1 = {myList[::-1]}") # => [2, 5, 2, 1]

otherList = myList[:] # => otherList = [1, 2, 5, 2] BUT (otherList is myList) is False

# Remove element from list
del myList[2] # => [1, 2, 2]

# Remove first occurance of value
myList.remove(2) # => raises ValueError if value is not in the list
print(f"myList = {myList}")

# Insert element
myList.insert(1, 9) # => [1, 9, 2]
print(f"myList = {myList}")

# Get index of first value
index = myList.index(9) # => 1 | raises ValueError if value is not in the list
print(f"Index of 9 is {index}")

# List concatenation
list_a = [1, 2, 3]
list_b = [9, 8, 7]
list_sum = list_a + list_b
print(f"List A = {list_a}")
print(f"List B = {list_b}")
print(f"List A + List B = {list_sum}") # => [1, 2, 3, 9, 8, 7]

# Check if value is in list 
present = 9 in list_sum
print(f"9 is in list_sum => {present}")

# List length 
length = len(list_sum)
print(f"Size of list_sum is {length}")

# Tuples - like lists, but immutable
print("-------Touples-------")
tup = (1, 2, 3)
tup[0] # => 1
# tup[0] = 5 # => TypeError
print(f"Touple = {tup}")
print(f"Size of tup = {len(tup)}")

tup = tup + (4, 5, 6) 
print(f"New Tuple = {tup}")

a, b, c = (1, 2, 3) # a = 1, b = 2, c = 3
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4

# Dictionary 
print("-------Dictionary-------")
empty_dict = {}
my_dict = {"one": 1, "two": 2} # keys need to be immutable types 

print(f"my_dict = {my_dict}")
print(f"my_dict[\"one\"] = {my_dict['one']}") # => 1

dict_keys = list(my_dict.keys()) # list is used to convert the result to a list
print(f"my_dict keys = {dict_keys}")

dict_values = list(my_dict.values())
print(f"my_dict values = {dict_values}")

"one" in my_dict # => True - in searches for the key
1 in my_dict # => False
print(f"one in my_dict => {"one" in my_dict}")
print(f"1 in my_dict => {1 in my_dict}")

# my_dict['four'] # => KeyError
# use the get() to avoid KeyError
my_dict.get('one') # => 1
my_dict.get('four') # => None
my_dict.get('four', 4) # => 4 - uses the default value parameter 

# Insert in Dictionary
# setdefault - sets a value only if the key isn't present
my_dict.setdefault("five", 5) # => my_dict['five'] is 5
my_dict.setdefault("five", 6) # => my_dict['five'] is still 5

my_dict.update({"four": 4})
print(f"my_dict after adding 4 => {my_dict}")
my_dict["six"] = 6 
print(f"my_dict after adding 6 => {my_dict}")

# Delete
del my_dict['two']
print(f"my_dict after deleting two => {my_dict}")

# Sets 
print("-------Set-------")
empty_set = set()
my_set = {1, 1, 2, 2, 3, 4} # elements in a set need to be immutable
print(f"my_set = {my_set}")

# invalid_set = {[1], 1} # TypeError => [1] is not immutable

# Add
my_set.add(5)
print(f"my_set after adding 5 => {my_set}")
my_set.add(5)
print(f"my_set after adding another 5 => {my_set}")

other_set = {3, 4, 5}
print(f"other_set = {other_set}")

# set intersection
print(f"my_set & other_set = {my_set & other_set}") # => the intersection of the sets => {3, 4, 5}
# set union
print(f"my_set | other_set = {my_set | other_set}") # => the union of the sets => {1, 2, 3, 4, 5}
# set difference
print(f"my_set - other_set = {my_set - other_set}") # => the difference of the sets => {1, 2}
# set simetric difference
print(f"my_set ^ other_set = {my_set ^ other_set}") # => the simetric difference of the sets => {1, 2}
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
# check if left set is superset of the right one
{1, 2} >= {1, 2, 3} # => False
{1, 2} <= {1, 2, 3} # => True

2 in my_set   # => True
10 in my_set  # => False

# Clone set
filled_set = my_set.copy()  # filled_set is {1, 2, 3, 4, 5}
filled_set is my_set # => False


