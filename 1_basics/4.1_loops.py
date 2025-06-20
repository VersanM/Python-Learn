# Loops assignemnt

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < len(my_list):
    for j in range(3):
        if my_list[i] == "Monday": continue
        print(my_list[i])
    i += 1