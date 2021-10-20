# Python Inheritance

Inheritance is the capability of one class to derive or inherit the properties from another class. In Python 3.x, object is root of all classes. Means "class Test(object)" and "class Test" are same.
We achieve inheritance by mentioning the parent class name in the definition of the child class. 
Eg: class subclass_name(superclass_name)

'''

    class Person:

        def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber

        def display(self):
            print(self.name, self.idnumber)

    class Employee(Person):

        def __init__(self, name, idnumber, salary, position):
            self.salary = salary
            self.position = position

            Person.__init__(self, name, idnumber)
    a = Employee('Bibek', 735101, 40000, 'SSE')

    a.display()
'''

'a' is the instance of the class Employee. The construtor i.e. the __ init __ function of a class is invoked when we create an object of the class. The parameters defined within __ init __() are called as the instance attributes. Hence, 'name' and 'idnumber' are the instance attributes of class Person and similarly, 'salary' and 'position' are the instance attributes of class Employee. Since the class Employee inherits from class Person, 'name' and 'idnumber' are can be accessed through instance of the class Employee. If you forget to invoke the __ init __ () of the parent class then its instance attributes would not be available to the child class.

# Types of Inheritance:

## Single Inheritance: 
   Single Inheritance enables a derived class to inherit properties from a single class, thus enabling the code reusuability and the addition of new features to existing code. Above code is an ex Single Inheritance.

## Multiple Inheritance: 
When a class can be derived from more than one class.

    class Mother:

        mothername = ""
        def mother(self):
            return self.mothername

    class Father:

        fathername = ""
        def father(self):
            return self.fathername

    class Son(Mother, Father):

        def parents(self):
            print(f"Father: {self.father()}")
            print(f"Mother: {self.mother()}")

There are few more types of Inheritance, like:
Multilevel, Hierarchical and Hybrid.