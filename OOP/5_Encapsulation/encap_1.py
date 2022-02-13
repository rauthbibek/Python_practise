class Employee:
    # constructror
    def __init__(self, name, salary):
        self.name = name # public variable
        self.__salary = salary # private variable

    # public methodto access private variable
    def show(self):
        # access private variable inside class
        print(f"Name: {self.name} salary: {self.__salary}")


emp = Employee("Raj", "30000")
emp.show()
print(emp.__dict__) # all the attributes for particular object
print(emp.__salary) # throws an error, as we can't access private variable

    
