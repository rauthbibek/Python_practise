#Use of double underscore

class Person:

    def __init__(self, name, age):

        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)


p1 = Person("Vasu", 28)

# accessing using method
p1.display()

# accessing outside class
print(p1.name)
print(p1.__age) # It will throw error as Python interpreter has created '_Person__age' instead of __age (name mangling)
print(p1._Person__age)

print(p1.__dict__)

