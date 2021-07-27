class Point:
    def move(slef):
        print("move")

    def draw(self):
        print("draw")

Point1 = Point()
Point1.x = 10 
Point1.draw()
print(Point1.x)

## A constructor : 
#   is function that gets call at the time of creating objects
# self : when we create instance of object .. 
#   self refrence same object in memory 

class Point:
    def __init__(self , x ,y):
        self.x = x
        self.y = y
    def move(slef):
        print("move")

    def draw(self):
        print("draw")

Point = Point(10,20)
Point.x = 12
print(Point.x)

#
class Person:
    def __init__(self , name):
        self.name = name

    def talk(slef):
        print("talk")

Person1 = Person("Hamed F")
print (Person1.name)
Person1.talk()