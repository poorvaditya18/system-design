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
import requests
import json 

class LoadBalancer:

    def __init__(self,ip,port,algorithm="random"):
        # by default algorithm I am considering load balancing algo as random 
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

            # start thread : to accept connections 
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
                # start : request handler 
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            print("Exception occured :"+str(e))

    def handle_client(self,client_socket):
        # handle the incoming request 
        # parse the request do some modifications
        request = client_socket.recv(1024).decode('utf-8')
        request_lines = request.split('\r\n')
        
        # Find the start of the body
        body_start = request_lines.index('') + 1
        
        # Join the body lines to get the JSON payload
        json_payload = '\r\n'.join(request_lines[body_start:])
        
        print(f"Received request: {request}")
        
        # parse it to json 
        try:
            json_data = json.loads(json_payload)
        except json.JSONDecodeError:
            print("Invalid JSON format")

        # check server request 
        # Check if it's a registration request
        if self.is_registration_request(json_data):
            """
            {
                server_ip: "127.0.0.1",
                server_port: 3000,
                request_type : "Register",
                data:{
                    isAlive:False/True
                }
            }
            """
            server_ip = json_data['server_ip']
            server_port = json_data['server_port']
            isAlive = json_data['isAlive']
            # register server 
            self.register_server(server_ip,server_port,isAlive)
        else:
            print("Sending Data to server ....")
            # Choose a server based on the load balancing algorithm
            # server = self.choose_server(self.algorithm)
            # # Send the request to the selected server
            # if server:
            #     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #     server_socket.connect(server)
            #     # send request to the selected server
            #     server_socket.send(json_data.encode('utf-8'))
            #     # get the response back
            #     response = server_socket.recv(1024).decode('utf-8')

            #     print(f"Received response from server: {response}")
            #     # Forward the response back to the client
            #     client_socket.send(response.encode('utf-8'))
            #     # Close the connections
            #     server_socket.close()
            #     client_socket.close()

    def heartbeat_monitoring(self):
        # PULL ---> heartbeat monitoring
        # regularly checks whether the server is alive or died. 
        # heartbeat messages should be only sent to registered servers 
        # server list will always have registered servers
        while True:
            with self.server_lock:
                print("checking health of servers from server list ......")
                for server_addr ,server_obj in self.servers.items():
                    heartbeat_payload = {}
                    heartbeat_payload["server_address"] = server_addr
                    heartbeat_payload["request_type"] = "heartbeat"
                    heartbeat_payload["data"] = {}
                    hearbeat_url = f"http://{server_addr}/heartbeat"
                    response = requests.post(hearbeat_url,data=heartbeat_payload)
                    
                    # Accessing JSON content from the response
                    json_response = response.json()

                    if response.status_code == 200 :
    
                        # check for healthy or not
                        if json_response["data"].get("isAlive") == 0:
                            # means not alive remove from server list
                            print(f"server is not alive . Making {server_addr} inactive from server list...")
                            self.servers[server_addr]["isAlive"] = json_response["data"].get("isAlive")
                            print(f"{server_addr} is inactive.")
                        else:
                            print(f"{server_addr} is alive.")
                            self.servers[server_addr]["isAlive"] = json_response["data"].get("isAlive")
                    else:
                        # cannot send request to server 
                        # server is not started or crashed or not found or any connection error 
                        print("invalid response from server: " + str(response))
                    
                print("Server List : " + str(self.servers))
            # delay
            threading.Event().wait(5)

    # choosing server 
    def choose_server(self,algorithm)->str:
        # implement load balancing algorithm 
        # return server which is registered as well as alive 
        pass
    
    # register server 
    def register_server(self, server_ip, server_port,isAlive):
        with self.server_lock:
            try:
                server_address = f"{server_ip}:{server_port}"
                server_obj = {
                    "isRegistered":1,
                    "isAlive":isAlive
                }
                self.servers[server_address] = server_obj
            
                # Notify the server about successful registration
                server_url = f"http://{server_address}/registration-response"
                register_response = {
                    "statuscode": 200,
                    "message": "Successfully registered with load balancer",
                    "data": {
                        "isRegistered": self.servers[server_address]["isRegistered"],
                    }
                }
                # Send the response back to the server
                res = requests.post(server_url, json=register_response)
            except Exception as e:
                print("Exception occured : " + str(e))

    # check registeration request 
    def is_registration_request(self,register_data)->bool:
        # check payload 
        rStatus = False 
        try:
            if register_data is not None:
                if register_data.get("request_type") is not None and register_data.get("request_type") == "Register":
                    # request type is registeration 
                    rStatus = True
        except Exception as e:
            print(f"Error occured while parsing request : " + str(e))
        return rStatus

# start load balancer at port : 5000
loadbalancer = LoadBalancer("localhost",5001,"RoundRobin")
