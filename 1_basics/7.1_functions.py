# Assignment: Create a function that takes in 3 parameters(firstname, lastname, age) and
# returns a dictionary based on those values

def convertToDictionary(firstname, lastname, age):
    return {
        'first_name': firstname,
        'last_name': lastname,
        'age': age
    }

my_dict = convertToDictionary(firstname='Mihai',lastname='Versan',age=31)

print(my_dict)