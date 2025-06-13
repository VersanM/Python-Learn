### Arrays and Linked Lists in Python

# to run this file, use the command:
# python3 2_data_structures/1_arrays_linked_lists.py

import array as arr

## Array
# is a data structure that stores multiple values of the same type

print('--------Array--------')
# Syntax: a = arr.array(data type, value list)
a = arr.array('d', [1.1, 5.1, 11.1]) # 'd', 'f' stands for double/float, 'i' for int, 'u' for unicode char
print(f'Array => {a}')
print(f'Array value at index 1 => {a[1]}')

## Basic operations:
# Length: len
length = len(a)
print(f'Array length => {length}')

# Add: append() - single value, extend() - a list, insert(i, x) - certain position
a.append(3.3)
print(f'Array after add => {a}')

a.extend([4.5, 6.7, 8.9])
print(f'Array after extend => {a}')

a.insert(0, 10.0)
print(f'Array after insert at 0 => {a}')

# Concatenation: +
x = arr.array('i', [1, 2, 3])
y = arr.array('i', [4, 5, 6])
print(f'X => {x}')
print(f'Y => {y}')
z = x + y
print(f'X+Y => {z}')

# Remove/Delete: pop()/pop(i) - also returns the value, remove() - does not return the value
n = x.pop()
print(f'x.pop() => {n}')

n = x.pop(1)
print(f'x.pop(1) => {n}')

y.remove(5)
print(f'y after y.remove(5) => {y}')

# Slicing: [i:j]
slice = a[0:3]
print(f'First 3 elements of a => {slice}')

# Looping
for i in a:
    print(i)

# Problem: You are building a simple temperature tracking program. The user inputs the temperatures recorded each day (as floats) for a week. You should:
# 1. Store the temperatures in an array.
# 2. Print all temperatures.
# 3. Find and print the:
#   - Average temperature
#   - Maximum temperature
#   - Minimum temperature
# 4. Count how many days the temperature was above the weekly average.
print('--------Problem--------')
temp = arr.array('d', [30.5, 32.0, 33.5, 31.0, 29.0, 35.2, 36.1])

print(f'All temperatures: {temp}')
avg = 0
sum_t = 0
length = len(temp)
max_t = temp[0]
min_t = temp[0]
for t in temp:
    sum_t += t
    if t > max_t:
        max_t = t
    if t < min_t:
        min_t = t
avg = sum_t / length
counter = 0
for t in temp:
    if t > avg:
        counter += 1
print(f'Average temperature: {avg}')
print(f'Max temperature: {max_t}')
print(f'Min temperature: {min_t}')
print(f'Temperatures above average: {counter}')


## Linked List
# is a data structure that stores multiple values of the same type
from collections import deque

print('--------Linked List--------')
# in Python there's a specific object for double-ended-queue called deque
l = deque() # empty list
print(f'Empty list => {l}')

l = deque(['a','b','c'])
print(f'Linked list => {l}')

# Add
l.append('d')
print(f'Linked list after appending \'d\' => {l}')
l.appendleft('z')
print(f'Linked list after appending \'z\' left => {l}')
l.insert(1, 'q')
print(f'Linked list after insert (1, \'q\') => {l}')

# Remove
x = l.pop()
print(f'Linked list after pop => {l}')
print(f'Poped element => {x}')
x = l.popleft()
print(f'Linked list after pop left => {l}')
print(f'Poped element => {x}')
l.remove('q')
print(f'Linked list after remove(\'q\') => {l}')