#Multiple Inheritance

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

s1 = Son()
s1.fathername = 'AJAY'
s1.mothername = 'REKHA'
s1.parents()
