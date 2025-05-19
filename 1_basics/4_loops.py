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