### Exceptions

# to run this file, use the command:
# python3 1_basics/6_exceptions.py

# Try - except
x = None
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    finally:
        if x is not None:
            print(f"Your number is: {x}")

# Handle multiple exacptions
try:
    x = int("abc")
except (RuntimeError, TypeError, NameError, ValueError):
    pass

try:
    x = int("abc")
except RuntimeError:
    pass
except ValueError:
    pass
except TypeError:
    pass

# Raise exceptions
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')

x = int(input("Please enter x: "))
y = int(input("Please enter y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("division by zero!")
else:
    print("result is", result)
finally:
    print("executing finally clause")

# Pass
def risky_operation():
    x = int("abc")

try:
    risky_operation()
except ValueError:
    pass  # Ignore the ValueError and move on
