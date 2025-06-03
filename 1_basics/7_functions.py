### Exceptions

# to run this file, use the command:
# python3 1_basics/7_functions.py

# Creating and calling a function
def my_function():
    print("This is my function!")

my_function()

# Arguments
def my_func_with_arg(name):
    print(f"Your name is {name}")

my_func_with_arg('Mihai')

# Arbitrary arguments *args
def my_func_arbitrary_args(*kids):
    print(f"Second kid is {kids[1]}")

my_func_arbitrary_args("Tom", "Jerry", "Spike")

# Keyword arguments
def my_func_keyword(child3, child2, child1):
    print(f"Second child is {child2}")

my_func_keyword(child1 = "Tom", child2 = "Jerry", child3 = "Spike")


