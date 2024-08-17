"""
Builder Pattern - 
    - is creational pattern that separates the construction of a complex object from its representation.
    - The Builder pattern provides a step-by-step approach to create an object, allowing  to construct different types and representations of the object without changing the construction logic. 
"""

# consider an example of ecommerce application where you have a order which should have properties and items , shipping method, payment_method, discount.

class Order:

    def __init__(self):
        self.items = []
        self.shipping_method = None
        self.payment_method = None
        self.discount = None

class OrderBuilder:

    def __init__(self):
        # here Builder will be responsible for creating a Order object 
        self.order = Order()

    def set_items(self, items : str):
        self.order.items.append(items)
        return self
    
    def set_shipping_method(self, shipping_method:str):
        self.order.shipping_method = shipping_method
        return self
    
    def set_payment_method(self, payment_method:str):
        self.order.payment_method = payment_method
        return self
    
    def set_discount(self, discount:str):
        self.order.discount = discount
        return self
    
    def build(self):
        return self.order


# so here creation of complex object is still same we are just adding properties.
order = OrderBuilder().set_items('t-shirt').set_items('jeans').set_shipping_method('standard_delivery').set_payment_method('COD').set_discount('SUMMER50').build()

print(order.items, order.shipping_method, order.payment_method,  order.discount)