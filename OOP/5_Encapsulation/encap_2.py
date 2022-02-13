class School:
    def __init__(self, schoolName):
        self._schoolName = schoolName

class Student(School):
    def __init__(self,name):
        self.name = name
        School.__init__(self,"JZS")

    def show(self):
        print(f"Student name: {self.name}")
        # Accessing protected member in child class
        print(f"School name: {self._schoolName}")

#s = School("JZS")
st_1 = Student("Amit")
st_1.show()
print(st_1.__dict__)
# Direct access protected variable is possible
print(st_1._schoolName)