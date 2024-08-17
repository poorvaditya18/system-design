"""
Singleton pattern - 
    - The Singleton Design Pattern is a creational pattern that ensures that a class has only one instance and provides a global point of access to that instance.
    - often used when exactly one object is needed to coordinate actions across a system.
    - Single Instance: Only one instance of the class is created.
    - Global Access: The instance is globally accessible across the system.
"""

# So this is generally used when backend wants to create a shared instance. ( it is mostly for responsiblities that should not change.)

# consider example :  Managing a Shopping Cart - In an eCommerce system, the shopping cart could be implemented as a Singleton to ensure that there is only one cart per user session.
class ShoppingCart:

    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            # create a new instance
            cls._instance = super().__new__(cls)
            cls._instance.items = [] # creating a list of cart items   
        return cls._instance
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items
    
# Usage
if __name__ == "__main__":
    # Get the shopping cart instance
    cart1 = ShoppingCart()
    cart1.add_item("Laptop")

    # we can also get the same shopping cart instance in another part of the program
    cart2 = ShoppingCart()
    cart2.add_item("Smartphone")

    print(cart1.get_items())  # Output: ['Laptop', 'Smartphone']
    print(cart1 is cart2)  # Output: True, both are the same instance