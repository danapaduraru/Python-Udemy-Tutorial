class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getAge(self):
        print("You are " + self.age)
    def getName(self):
        print("Your name is " + self.name)

p = Person("Dana",20)
p.getName()

class Student(Person):
    def __init__(self):
        print("student class init")
    def child(self):
        print("in child class")