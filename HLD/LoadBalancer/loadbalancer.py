"""
Load Balancer Implementation in python 
Here we will implement different Load balancing algorithms to route traffic .
Load Balancer can configure your server in PULL (heartbeatModel) or PUSH .
Key points for reference
1. Load Balancer can be implemented as a separate server which will route traffic. 
2. Load Balancer can be implemented as a socket server connection also . 
"""
import threading
import socket
import time 

class LoadBalancer:

    def __init__(self,ip,port,algorithm="random"):
        # by default algorithm I am considering as random 
        print("Initialising Load Balancer....")
        self.ip = ip
        self.port = port
        self.algorithm = algorithm
        self.servers = {}  # Dictionary to store registered servers [shared Resource]
        self.server_lock= threading.Lock()
        self.start_load_balancer()

    def start_load_balancer(self):
        # create a new load balancer : IPV4 , TCP socket conenction
        try:
            self.lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.lb_socket.bind((self.ip,self.port))
            self.lb_socket.listen()

            print(f"Load Balancer listening on {self.ip}:{self.port}")

            # start thread to accept connections 
            threading.Thread(target=self.accept_clients).start()

            # start thread : heartbeat monitoring
            threading.Thread(target=self.heartbeat_monitoring).start()

        except Exception as e:
            print("Exception occured :"+str(e))

    def accept_clients(self):
        try:
            while True:
                # accept the incoming connections 
                # multithreaded as we can handle multiple connections request from different sources 
                # no need to wait for connection to finish first. another thread will receive and parse the incoming data 
                # from server or client app 
                client_socket, client_address = self.lb_socket.accept()
                print(f"Accepted connection from {client_address}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            print("Exception occured :"+str(e))

    def handle_client(self,client_socket):
        # handle the incoming request 
        # parse the request do some modifications
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        # Choose a server based on the load balancing algorithm
        server = self.choose_server()

        # Send the request to the selected server
        if server:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect(server)
            # send request to the selected server
            server_socket.send(request.encode('utf-8'))
            # get the response back
            response = server_socket.recv(1024).decode('utf-8')

            print(f"Received response from server: {response}")

            # Forward the response back to the client
            client_socket.send(response.encode('utf-8'))

            # Close the connections
            server_socket.close()
            client_socket.close()

    def heartbeat_monitoring(self):
        # PULL ---> heartbeat monitoring
        # regularly checks whether the server is alive or died. 
        # heartbeat messages should be only sent to registered servers 
        while True:
            with self.server_lock:
                # logic 
                pass

            # check every 5 sec
            threading.Event().wait(5)

    def choose_server(self):
        # implement load balancing algorithm 
        pass

# start load balancer at port : 5000
loadbalancer = LoadBalancer("localhost",5001,"RoundRobin")
