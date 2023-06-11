print("Hello, World!")

#let start with conditions

FirstNumber = int(input("enter first number: "))
SecondNumber = int(input("enter second number: "))
if(FirstNumber > SecondNumber):
    print(f"firstnumber : {FirstNumber} is bigger than secondnumber : {SecondNumber}")
elif(SecondNumber > FirstNumber):
    print(f"secondnumber : {SecondNumber} is bigger than firstnumber : {FirstNumber}")
else:
    print("they are equal")

#datatypes list, tuple, set & dict

names = ['sajjad', 'kevin', 'dock', 'mac']
print(names)
names.append('iphone')
names.sort()
print(f"new names: {names}")

coordinates = ("32.4279° N", "53.6880° E")
print(coordinates[0])
print(coordinates)

fibnums = set()
fibnums.add(1)
fibnums.add(1)
fibnums.add(2)
fibnums.add(3)
fibnums.add(5)
fibnums.add(8)
fibnums.add(13)
fibnums.add(1)
fibnums.add(13)

print(f"fibnums: {fibnums}")

infos = {
    'name' : 'sajjad',
    'age' : '16',
    'height' : 188,
    'weight' : 88,
}
print(infos)