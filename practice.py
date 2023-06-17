"""
1- work with conditions 
2- work with loops
3- work with datastructures
4- work with functions
5- work with classes
6- and finally oop 
"""

"""

#part 1
number = int(input("enter a number: "))

if number % 2 == 0:
    print("your number is even")
elif number % 2 != 0:
    print("your nimber is odd")
elif number == 0:
    print("your number is zero")
"""

"""
#part 2
#for
names = []
number_of_names = int(input("enter number of the names: "))

for i in range(0, number_of_names):
    names.append(input("enter a name: "))

print(f"names list is: {names}")
"""

"""
#while
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

"""
#part 3
#lists
fib_index = int(input("enter a number: "))
fibonatchi = [1, 1]

for i in range(0, fib_index-2):
   fibonatchi.append(fibonatchi[i] + fibonatchi[i+1])

print(f"fibonatchi sequnce is: {fibonatchi}")
"""

