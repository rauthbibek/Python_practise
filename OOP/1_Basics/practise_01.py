#Basic Class, without attributes


#class creation
class Item:
    
    #we pass self--> means when call this method through any object of the class, by default object itself is
    #passed as a parameter
    def calculate_total_price(self, X, Y):
        return X*Y

#Instance instantiation
item1 = Item()
item1.name = "OnePlus"
item1.price = 50000
item1.quantity = 5

print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "IPhone"
item2.price = 150000
item2.quantity = 3

print(item2.calculate_total_price(item2.price, item2.quantity))

#print(type(item1))
#print(type(item1.name))
#print(type(item1.price))
#print(type(item1.quantity))


#we can say tghat, using class "Item" we have created our own data type of Item type
#<class '__main__.Item'>

#<class 'str'>
#<class 'int'>
#<class 'int'>