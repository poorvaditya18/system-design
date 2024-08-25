"""
Behavioural Pattern:  Chain of responsibility 

Characteristics :
- provides a solution for passing requests along a chain of handlers.
- These handlers, like links in a chain, process the request or pass it to the next handler in line. This pattern acts as an intermediary, allowing you to decouple the sender of a request from its receivers.

When to use : 
- Request Processing: In situations where requests must pass through multiple processing stages, each handling a specific task.
- Logging: Logging systems with multiple log handlers like console, file, and email loggers.
- User Interface Events: For user interface components, such as buttons, that handle events through a chain of listeners.

Types of Chain of Responsibility: 
- Basic Chain: In this standard form, handlers are linked sequentially, and each handler either processes the request or passes it to the next in line.
- Bidirectional Chain: Handlers can traverse the chain in both forward and backward directions.
- Hierarchical Chain: Requests can be passed down the hierarchy or propagated back up if necessary.
- Dynamic Chain: The chain's composition can change dynamically during runtime, enabling on-the-fly adjustments to handle different types of requests.
"""

# suppose you want to your request to pass through multiple layer of middleware before reaching to service layer. example : you want to authenticate, log, validate, security check, etc. So here there is a chain of responsibilities. 

# define handler interface
from abc import ABC, abstractmethod

# interface 
class Middleware(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


# create concrete classes
class AuthenticationMiddleware(Middleware):
    """Middleware responsible for user authentication."""
    
    def handle_request(self, request):
        """Handle authentication or pass to the next middleware in the chain."""
        if self.authenticate(request):
            print("Authentication middleware: Authenticated successfully")
            # Pass the request to the next middleware or handler in the chain.
            return True
        else:
            print("Authentication middleware: Authentication failed")
            # Stop the chain if authentication fails.
            return None

    def authenticate(self, request):
        """Implement authentication logic here."""
        # Return True if authentication is successful, else False.
        print("authentication is successful.")
        return True

class LoggingMiddleware(Middleware):
    """Middleware responsible for logging requests."""
    
    def handle_request(self, request):
        """Handle request logging and pass to the next middleware in the chain."""
        print("Logging middleware: Logging request")
        # Further we can provide enhances logging functionalities 
        return True


class DataValidationMiddleware(Middleware):
    """Middleware responsible for data validation."""
    
    def handle_request(self, request):
        """Handle data validation or pass to the next middleware in the chain."""
        if self.validate_data(request):
            print("Data Validation middleware: Data is valid")
            # Pass the request to the next middleware or handler in the chain.
            # return super().handle_request(request) --> we can also pass the request to  parent middleware
            return True
        else:
            print("Data Validation middleware: Invalid data")
            # Stop the chain if data validation fails.
            return None

    def validate_data(self, request):
        """Implement data validation logic here."""
        # Return True if valid data, else False
        print("Data Validation middleware: validity successful")
        return True



# create chain 
class Chain:
    def __init__(self):
        self.middlewares = []

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def handle_request(self, request):
        for middleware in self.middlewares:
            request = middleware.handle_request(request)
            if request is None:
                print("Request processing stopped.")
                break

        # add complex logic to pass to next layer
        if request is not None:
            print("passing request to next layer")

# client code 
if __name__ == "__main__":
    # Create middleware instances.
    auth_middleware = AuthenticationMiddleware()
    logging_middleware = LoggingMiddleware()
    data_validation_middleware = DataValidationMiddleware()

    # Create the chain and add middleware.
    chain = Chain()
    chain.add_middleware(auth_middleware)
    chain.add_middleware(logging_middleware)
    chain.add_middleware(data_validation_middleware)

    # Simulate an HTTP request.
    http_request = {"user": "username", "data": "valid_data"}
    chain.handle_request(http_request)