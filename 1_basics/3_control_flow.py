my_var = 10

# If-Else statement
if my_var > 10:
    print("my_var is greater than 10")
elif my_var < 10:
    print("my_var is less than 10")
else:
    print("my_var is exactly 10!")

# do nothing if contidion is met
if my_var == 10:
    pass

# Switch statement
# Basic implementation using a Dictionary
switcher = {
    0: "This is Zero",
    1: "This is One",
    2: "This is Two" 
}
switch_val = switcher.get(1, "Not Found")
print(f"Switcher[0] = {switch_val}")
switch_val = switcher.get(5, "Not Found")
print(f"Switcher[5] = {switch_val}")

# Match command
match my_var:
    case 0:
        print("Var is 0")
    case 1:
        print("Var is 1")
    case 2:
        print("Var is 2")
    case other:
        print("Var is not 0, 1 or 2")