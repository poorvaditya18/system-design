"""
Singleton pattern - 

Characteristics: 
    - The Singleton Design Pattern is a creational pattern that ensures that a class has only one instance and provides a global point of access to that instance.
    - It is particularly useful when you want to ensure that a class has only one instance throughout the application's lifecycle.
    - Singleton pattern restricts the instantiation of a class to a single object. This means that regardless of how many times the code requests an instance of the class, it will always receive the same instance.
    - This uniqueness can prove to be incredibly valuable when dealing with resources that need to be shared across different parts of the codebase.
    - often used when exactly one object is needed to coordinate actions across a system.
    - Single Instance: Only one instance of the class is created.
    - Global Access: The instance is globally accessible across the system.

    - usage: This can be valuable in scenarios where you need a single point of control, such as managing configurations, database connections, or logging services.

Benefits: 
    - Single Instance: Ensures that only one instance of the class is created,
    - Global Access: Provides a global point of access to the instance, making it easy to share data or functionality across different parts of the application.
    - Resource Management: Helps manage resources that should be shared, such as database connections, without creating multiple connections and overwhelming the system.
    - Lazy Initialization: Allows for efficient resource usage by creating the instance only when it is actually needed.

Applications:
    - Database Connection Pools: Enhancing database interaction efficiency via a unified connection pool.
    - Logger Services: Centralizing application logging through a single logger instance.
    - Configuration Management: Ensuring a solitary configuration manager instance oversees application settings.
    - Hardware Access: Controlling access to hardware resources, such as a printer or sensor, through a single instance.
"""
import threading
# 1. MetaClass Implementation -> 
class SingletonMeta(type):
    """this class is responsible for managing instances."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument
        do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """
    Here goes our class's business logic without concerning about
    handling the intricacies of the singleton pattern.
    """
    pass

# 2. Decoration Implementation -> 
def singleton(cls):
    instances = {}  # Dictionary to store instances of different classes
    def get_instance(*args, **kwargs):
        # If class instance doesn't exist in the dictionary
        if cls not in instances:
            # Create a new instance and store it
            instances[cls] = cls(*args, **kwargs)  
        return instances[cls]  # Return the existing instance
    # Return the closure function for class instantiation
    return get_instance  

@singleton  # Applying the singleton decorator
class SingletonClass:
    def __init__(self, data):
        self.data = data

    def display(self):
        print(f"Singleton instance with data: {self.data}")

# 3. Thread Safety and Lazy Initialization
class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # a threading lock is used to ensure that only one thread can create the instance at a time, preventing race conditions
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

# 4. Real world example :  Managing a Shopping Cart - In an eCommerce system, the shopping cart could be implemented as a Singleton to ensure that there is only one cart per user session.
class ShoppingCart:
    _instance = None 
    # Unlike the rigid Singleton class, Python enables normal instantiation with a custom "__new__" method for obtaining the singleton instance.
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