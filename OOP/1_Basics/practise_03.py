class Item:

    def __init__(self, name: str, price: float, quantity=0):

        '''
        Using assert statement could allow us to validate the arguments we received.
        Also it will allow us to catch up the bugs ASAP.
        '''
        #Run validations to the received arguments
        assert price>=0, f"Price {price} is not greater than or equal to zero."
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero."

        '''
        we can define the type of the attribute by adding ': <data_type>: after the attribute
        like "name: str". We can only control the type of the attribute in "__init__" method, we can't do any
        other validations like, "price >= 0"
        '''
        #Assign to self object
        #instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 5000, 3)
item2 = Item("Laptop", 50000, -4)

print(item1.name)            
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)


