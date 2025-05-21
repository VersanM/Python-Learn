import random
import time

### Loops

# to run this file, use the command:
# python3 1_basics/4_loops.py

# While loop
print("-------While loop-------")
number = 0

while number < 5:
    print(f"While loop no {number}")
    number += 1

# Loop keywords
# break - immediately termiantes loop
# continue - end only current iteration

number = 0
print("Break example")
print("Loop started")
while number < 5:
    if number == 2:
        break
    print(f"Loop no {number}")
    number += 1
print("Loop ended\n")

number = 0
print("Continue example")
print("Loop started")
while number < 5:
    if number == 2:
        number += 1
        continue
    print(f"Loop no {number}")
    number += 1
print("Loop ended\n")

# While - else
# the else clause will run only if the while loop terminates naturally without a break statement 
# the else branch executes when the condition becomes false and only then
# doesn't make sense to have an else clause in a loop that doesn't have break statement 
MAX_RETRIES = 5
attempts = 0

while attempts < MAX_RETRIES:
    attempts += 1
    print(f"Attempt {attempts}: Connecting to the server...")
    # Simulating a connection scenario
    time.sleep(0.3)
    if random.choice([False, False, False, True]):
        print("Connection successful!")
        break
    print("Connection failed. Retrying...")
else:
    print("All attempts failed. Unable to connect.")

# For loop
print("-------For loop-------")
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(f"For loop through colors: {color}")

# iterate through characters in a string 
my_text = "MIHAI"
for character in my_text:
    print(character)

# iterate in a range
for index in range(5):
    print(index) # 0-4 

numbers = [1, 3, 5, 7, 9]
target = 5

for number in numbers:
    print(f"Processing {number}...")
    if number == target:
        print(f"Target found {target}!")
        break

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(f"{number = }")
    if number % 2 != 0:
        continue
    print(f"{number} is even!")

# nested for loops
for number in range(1, 11):
    for product in range(number, number * 11, number):
        print(f"{product:>4d}", end="")
    print()

# looping with indices
fruits = ["orange", "apple", "mango", "lemon"]
for index in range(len(fruits)):
    fruit = fruits[index]
    print(index, fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

# repeating a predifined number of times
for _ in range(3):
    print("Hello 3 times!")

print("Modifing collections in a loop")
# there are safe and unsafe changes
# modifing items in a list without adding/removing is most of the times safe
names = ["Alice", "Bob", "John", "Jane"]
for index, name in enumerate(names):
    names[index] = name.upper()
print(names)

# when removing items from a list, use "[:]" - operator that creates a copy of the original list
numbers = [2, 4, 6, 8]
for number in numbers[:]:
    if number % 2 == 0:
        numbers.remove(number)
print(numbers)

print("Create a collection using loop")
cubes = []
for number in range(10):
    cubes.append(number**3)
print(cubes)