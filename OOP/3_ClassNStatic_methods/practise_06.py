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

    @staticmethod
    def is_int(num):
        '''
        This behaves like a normal function which we can declare outside of the class.
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''
        #We will count out the floats that are point zero
        #Like, 5.0 7.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_int(5.50))

