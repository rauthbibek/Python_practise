import csv
from os import read

class Item:

    pay_rate = 0.8 #class attribute
    all = [] # List to store all the instances
    def __init__(self, name, price, quantity):

        #Run validations to the received arguments
        assert price>=0, f"Price {price} is not greater than or equal to zero."
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero."

        #Assign to self object
        #instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute 
        Item.all.append(self) #appending instances at the time of instance instantiation


    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('OOP\\3_ClassNStatic_methods\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
                try:
                    Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
                except Exception as e:
                    print(e)
                        

    #It will override the instance representation
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


#item1 = Item("Phone", 5000, 3)
#item2 = Item("Laptop", 50000, 4)
#item3 = Item("TV", 70000, 4)
#item4 = Item("Mouse", 500, 6)
#item5 = Item("AC", 30000, 4)

Item.instantiate_from_csv() #Instantiating instances from csv file
print(Item.all) 
#print(Item.instantiate_from_csv())