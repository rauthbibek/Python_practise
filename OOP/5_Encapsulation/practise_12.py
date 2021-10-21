#using getter setter methods

class Person:

    def __init__(self, name, age):

        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age



p1 = Person("Hey", 30)

p1.display()
print(p1.getAge())
p1.setAge(33)
print(p1.getAge())


