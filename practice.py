#1- work with conditions 
#2- work with loops
#3- work with datastructures
#4- work with functions
#5- work with classes
#6- and finally oop 


#part 1
"""
number = int(input("enter a number: "))

if number % 2 == 0:
    print("your number is even")
elif number % 2 != 0:
    print("your nimber is odd")
elif number == 0:
    print("your number is zero")
"""

#part 2
#for
"""
names = []
number_of_names = int(input("enter number of the names: "))

for i in range(0, number_of_names):
    names.append(input("enter a name: "))

print(f"names list is: {names}")
"""

#while
"""
while_number = 1
entered_numbers = []
while while_number % 2 != 0:
    while_number = int(input("enter an even number: "))
    if while_number == 0:
        print("0 is not an even number!")
        while_number += 1
        entered_numbers.append(while_number - 1)
    else:
        entered_numbers.append(while_number)

print(f"entered_numbers are: {entered_numbers}")
"""

#part 3
#lists
"""
fib_index = int(input("enter a number: "))
fibonatchi = [1, 1]

for i in range(0, fib_index-2):
   fibonatchi.append(fibonatchi[i] + fibonatchi[i+1])

print(f"fibonatchi sequnce is: {fibonatchi}")
"""

#tuple
"""
my_country_position = ("32°00'N", "53°00'E")
"""

#set
"""
numbers = set()
number_of_numbers = int(input("enter a number: "))

for i in range(0, number_of_numbers):
    numbers.add(int(input("enter a number: ")))

print(f"sorted of your entered numbers is: {sorted(numbers)}")
"""

#dict
"""
informations = {}
dict_num = int(input("how many name and age do you want to enter: "))

for i in range(0, dict_num):
    name = input("enter a name: ")
    age = int(input("enter an age: "))
    informations[name] = age
print(informations)
"""

#def
"""
def fibonatchi(number):
    res = [1, 1]
    for i in range(0, number-2):
        res.append(res[i] + res[i+1])
    return res

number = int(input("enter a number: "))
res = fibonatchi(number)
print(f"your sequence is: {res}")
"""

#class
"""
class Math():
    def __init__(self):
        pass
    def fibonatchi(self, number):
        self.res = [1, 1]
        for i in range(0, number-2):
            self.res.append(self.res[i] + self.res[i+1])
        return self.res
    def factoriel(self, num):
        self.tmp = 1
        for i in range(1, num+1):
            self.tmp *= i
        return self.tmp


number = 5
a = Math().factoriel(number)
print(a)
"""