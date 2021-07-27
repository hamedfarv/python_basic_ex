def greet_users():
    print("Hi Hamed")
    print("Greeting")

print("start")
greet_users()
print("finish") 

##

def greet_users(name):
    print(f"Hi {name}")
    print("Greeting")

print("start")
greet_users('Mohammad')
print("finish") 

## key word argument to improve readabillity of functions

def greet_users(first_name , last_name):
    print(f"Hi {first_name}  {last_name} ")
    print("Greeting")

print("start")
greet_users(first_name='Hamed' , last_name="farvardin")
print("finish") 

## error and exceptions

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("invalid value")

