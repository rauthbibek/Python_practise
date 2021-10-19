class Item:

    pay_rate = 0.8 #class attribute
    def __init__(self, name, price, quantity):
        #Run validations to the received arguments
        assert price>=0, f"Price {price} is not greater than or equal to zero."
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero."

        #Assign to self object
        #instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # self.price = self.price*Item.pay_rate #Using class name accessing the class attribute
        self.price = self.price*self.pay_rate # If we override the pay_rate value for any instance it will reflect here
        return self.price

item1 = Item("Phone", 5000, 3)
item2 = Item("Laptop", 50000, 4)

'''
class attributes we generally access through 'class_name'.
We can access it through instance also, because any instance will search for attributes in instance level and 
then it looks for class level and fetches class level attributes.
'''
#accessing class attributes
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

#shows all the attributes belonging to the object
print(Item.__dict__) # ALl the attributes for class level
print("*"*100)
print(item1.__dict__) # ALl the attributes for instance level

print(f"item1 price after discount: {item1.apply_discount()}")
item2.pay_rate = 0.7 #Overriding the class attribute in instance level. pay_rate will be 0.7 only for item2
print(f"item2 price after discount: {item2.apply_discount()}")
