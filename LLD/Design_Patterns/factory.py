"""
Factory method - lies under creational design patterns. 
               - Instead of the client code directly creating objects, it delegates the responsibility to a Factory Method.
               - The Factory Design Pattern is a creational design pattern used to create objects without specifying the exact class of the object that will be created.
               - Benefits : 
                   - Encapsulation: The client code is decoupled from the specific classes needed to instantiate the logger. The factory handles this.
                   - You can add new types of Payment without modifying the client code.
                   - This pattern is useful in larger systems where object creation logic becomes more complex.
"""
from abc import abstractmethod

class Payment:
    @abstractmethod
    def make_payment(self,amount):
        pass

class Stripe(Payment):

    def __init__(self):
        self.name = 'razorpay'

    def make_payment(self, amount : float ):
        print(f"{self.name} initiating payment {amount} ")

class Razorpay(Payment):

    def __init__(self):
        self.name = 'razorpay'

    def make_payment(self, amount : float):
        print(f"{self.name} initiating payment {amount} ")

class PaymentFactoryMethod:

    # suppose you have multiple payment providers 
    payment_providers ={
        "Stripe": Stripe(),
        "Razorpay": Razorpay(),
        }

    def get_payment_provider(self, payment_service_provider):
       payment_service_provider = self.payment_providers[payment_service_provider]
       return payment_service_provider

if __name__ == "__main__":
    # This helps :  no need to explicitly create object of razorpay or strip class 
    # Factory will return its creation. 
    payment_factory = PaymentFactoryMethod()
    payment_provider = payment_factory.get_payment_provider('Razorpay')
    payment_provider.make_payment(1000)