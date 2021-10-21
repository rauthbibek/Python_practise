#Use of underscore

class Person:

    def __init__(self, name, age):

        self.name = name
        self._age = age

    def display(self):
        print(self.name)
        print(self._age)


p1 = Person("Vasu", 28)

# accessing using method
p1.display()

# accessing outside class
print(p1.name)
print(p1._age)

