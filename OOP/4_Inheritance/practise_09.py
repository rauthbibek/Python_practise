class Item:

    pay_rate=0.8 #class attribute
    all=[]
    def __init__(self, name, price, quantity):

        assert price>=0, f"Price {price} is not greater than or equal to zero." 
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero."

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    
    def __init__(self, name:str, price:float, quantity=0, broken_phones = 0 ):
        super().__init__(name, price, quantity)

        self.broken_phones= broken_phones
        


phone1 = Phone("OnePlus", 50000, 3, 1)
print(Phone.all)
print(isinstance(phone1, Phone))
print(isinstance(phone1, Item))
