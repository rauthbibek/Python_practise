#parent class
class Person:
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name, self.idnumber)

#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, position):
        self.salary = salary
        self.position = position

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
a = Employee('Bibek', 735101, 40000, 'SSE')

#calling a function of the parent class (Person) using child class instance
a.display()