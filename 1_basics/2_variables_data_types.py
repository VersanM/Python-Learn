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
"Hello world!"
'Hello world!'
"Hello world!"[0] # => 'H'
len("Hello") # 5

# format strings
name = 'Mihai'
f"My name is {name}" # => "My name is Mihai"
f"{name} is {len(name)} characters long."


