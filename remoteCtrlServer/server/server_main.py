
import socket
import subprocess
import os
import json

class Server:
    """The responsibility of the Server is to start 
    the server
    """
    def __init__(self, addr, port):
        """Initialize the server with addr and port arguments"""
        
        self.addr = addr
        self.port = port
        self.my_socket = None
        
    
        
    def start_server(self):
        self.create_socket()
        self.bind_socket() 
        print("-----------------------------------")
        print("| Learn the basics of the shell   |")
        print("-----------------------------------")
        print("==>Execute the client side TO CONNECT, please")
        
        while True:      
            self.accept_connection()
           
    
    #This function create the socket
    def create_socket(self):
        #create the socket
        self.my_socket = socket.socket()
        
    #This function bind the socket and listening for connections
    def bind_socket(self):
        #create de connection(the host and the port)
        self.my_socket.bind((self.addr, self.port))
        #amount of requests
        self.my_socket.listen(10)
    
    #function that accept connection
    def accept_connection(self):
        #with this line we accept the requests or wait for a intent of connection
            #And return 2 values 
            connection, addr = self.my_socket.accept()
            print("-----------------------------------------------------------")
            print(f"The connection works! |  IP: {addr[0]} | Port: {addr[1]}")
            clientRespose01= connection.recv(1024)
            print(clientRespose01.decode())
            print("-----------------------------------------------------------")
            
            #convert the array into json to send it to the client
            commands = ['ls', 'touch', 'cd']
            commands_in_json = json.dumps(commands)
            connection.send(commands_in_json.encode())
                
            
            #Receive the shell command from the client 
            clientCommand01= connection.recv(1024).decode()
            #print(clientRespose02.decode())
            
            
            #execute the command in the server
            if clientCommand01 == 'ls':
                result = subprocess.check_output(["ls"]).decode()        
                #sending the result
                connection.send(result.encode())
                 
            #This is the if statement to create a file from the server
            #and send the response to the client
            elif clientCommand01.startswith('touch'):
                namefile = clientCommand01[6:]
                open(namefile, 'w').close()
                response = f"file created {namefile} successfully"
                connection.send(response.encode())
            elif clientCommand01.startswith('cd'):
                os.chdir(clientCommand01[3:].encode())
                response = f"Now you are in {os.getcwd()}"
                connection.send(response.encode())
           
            else:
                connection.send("Try again".encode())
                
        
            
            
            
            
        