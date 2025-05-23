### Type casting

# to run this file, use the command:
# python3 1_basics/5_type_casting.py

# Implicit Conversion - automatic type conversion
print("-------Implicit Cast-------")
int_number = 123
float_number = 1.23

result = int_number + float_number # 124.23

print(f"{int_number} + {float_number} = ", result)
print("Result Data Type:", type(result)) #Float

# '12' + 23 => TypeError

#Explicit Conversion - manual type conversion
# use the built-in functions like int(), float(), str(), etc
print("-------Explicit Cast-------")
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_string + num_integer
print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

print("-------Some examples-------")
print(f"int(10.5) => {int(10.5)}") # 10
# print(f"int('11abc4') => {int('11abc4')}") # ValueError