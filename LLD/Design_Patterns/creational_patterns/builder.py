"""
Builder Pattern - 

characteristics:
    - is creational pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
    - The Builder pattern provides a step-by-step approach to create an object, allowing  to construct different types and representations of the object without changing the construction logic. 

Benefits : 
    - Flexibility: Different types of orders (e.g., standard, express) can be built using the same builder process but with different configurations.
    - Readability: The order-building process is easy to read and maintain with method chaining, as opposed to a large constructor with many parameters.
    - Extendability: Adding new order components (e.g., new shipping methods, payment methods) only requires adding new methods in the builder without changing the core construction logic.
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
        # this builder method will return object
        return self.order

class OrderBuilderDirector:
    """Director for constructing complex forms using a specific builder."""

    def __init__(self, builder):
        self.builder = builder

    def construct_order(self, **order_details):
        """Construct the form using the builder."""
        items = order_details.get('items')
        delivery_method = order_details.get('delivery_method')
        payment_method = order_details.get('payment_method')
        discount = order_details.get('discount')
        self.builder.set_items(items).set_shipping_method(delivery_method).set_payment_method(payment_method).set_discount(discount)

if __name__ == "__main__":
    # Demonstrate form generation using the Builder Pattern
    order_builder = OrderBuilder()
    order_builder_director = OrderBuilderDirector(order_builder)
    order_details = {
        'items':'t-shirt',
        'delivery_method':'Regular Shipping Method',
        'payment_method':'COD',
        'discount':'SUMMER50'
    }
    order_builder_director.construct_order(**order_details)
    order = order_builder.build()
    print(order.items, order.shipping_method, order.payment_method,  order.discount)

# so here creation of complex object is still same we are just adding properties.
# order = OrderBuilder().set_items('t-shirt').set_items('jeans').set_shipping_method('standard_delivery').set_payment_method('COD').set_discount('SUMMER50').build()
# print(order.items, order.shipping_method, order.payment_method,  order.discount)