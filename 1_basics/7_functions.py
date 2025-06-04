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

# Default parameter value
def my_func_default_val(country = "Romania"):
    print(f"I am from {country}")

my_func_default_val("UK")
my_func_default_val()

# List param
fruits = ["kiwi", "apple", "pineapple"]
def my_func_list_param(food):
    for item in food:
        print(item)

my_func_list_param(fruits)

# Return values
def my_func_double(x):
    return x * 2

print(my_func_double(2))
print(my_func_double(5))
print(my_func_double(10))

# pass Statement 
# function definition cannot be empty => use pass 
def my_func_do_nothing():
    pass


