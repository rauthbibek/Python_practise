

class Item:

    '''
    attributes will be initialized with the instance and we can pass default values for any attributes,
    like we passed for 'quantity=0'
    '''
    def __init__(self,name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    '''
    As we all know methods has instance as a parameter(using self), we need not to pass any extra parameter
    to access the attributes of this instance
    '''
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 5000, 3)
item2 = Item("Laptop", 5000) #we have not passed 'quantity' here


'''
we have added some attributes to the constructor, that doesn't means we can't add some more attributes
based on our requirements.So, we can add other attributes after we instantiate the instance.
'''
item2.has_numpad = False 

print("All the attributes")
print(item1.name)            
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
print(item2.has_numpad)
print("Methods")
print(item1.calculate_total_price())
print(item2.calculate_total_price())