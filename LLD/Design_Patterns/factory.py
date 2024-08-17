"""
Factory method - lies under creational design patterns. 
               - Instead of the client code directly creating objects, it delegates the responsibility to a Factory Method.
"""
class Stripe:

    def __init__(self):
        self.name = 'razorpay'

    def make_payment(self, amount):
        print(f"{self.name} initiating payment {amount} ")

class Razorpay:

    def __init__(self):
        self.name = 'razorpay'

    def make_payment(self, amount):
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