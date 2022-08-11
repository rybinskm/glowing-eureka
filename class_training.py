class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Name: {self.name} Age: {self.age}")
"""
p1 = Person("Michal", "29")
p2 = Person("Adrian", "29")
p3 = Person("Emilian", "29")

p1.myfunc()
p2.myfunc()
p3.myfunc()
"""
