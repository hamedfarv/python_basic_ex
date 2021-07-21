#### Variables ####

x = 100

y = 200

x = y

print(x + y)


print('----------------')

w, z = 400, 500

print(z)

print('----------------')

_myNumber = 100

_myNumber = _myNumber - 2

_myNumber2 = 50

_mynumber2 = 51

print(_myNumber2)
print(_mynumber2)

my_age = 23  # snake case variable naming

myAge = 23  # camel case variable naming

PI = 3.14

MyAge = 23  # upper camel case

#### Number Operarators ####

print("Hiii") ; 

print (type('5'))
print (type('5'))

# operators : + - * /
# **

print(3 ** 2)  # means : 3 in power of 2
print(49 ** 0.5)

print('----------------------')

# %  returns what remains from division

print(68 / 6)
print(68 % 6)

print(78 % 2)
print('----------------------')

# // return integer part of a division

print((68 - (68 % 6)) / 6)

print(68 // 6)

#### strings ####

print('*' * 10)

name = input("Please write your name:" ) 
print('Hi' + ' ' + name)

my_string = 'my name is nobody'

print(my_string[1:]) ## start print from 1 index to end of array
print(my_string[0:-1]) ## ignore last charecter from end of array and print all
print(my_string[:]) ## work like copy

## How to format string using 'f'

first_name = 'hamed'
last_name = 'farvardin'
msg = f'{first_name} [{last_name}] is a coder '
print (msg)

#### String Method ####

my_string = "Salam Hamed"
print(len(my_string))

my_number = 123
print(len(str(my_number)))

    ## Using Find
my_find_string = "Salam Hamed"
my_find_string.find('Ha')
print("Hamed" in my_find_string)

##### Argumented assignment

x= 10
x +=4 ## increment by 4
print(x)

#### Math options

import math

print(math.sin(180))

#### List , collections , dic ####

productList = ['hamed' , 'farvardin' , 13 , True]

print(productList)

Person =  { "name" : 'hamed' , "age" : 34 , "lastName" : 'Farvardin' }

print(Person["age"])

## touples when you want to have list o objects that now where in
## project can change items immutable

my_touple = (1,2,3,4)
my_touple[0] = 2 ## getting error

## unpacking
coordinate = (1,2,3)
x,y,z = coordinate

print(z)

