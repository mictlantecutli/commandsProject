import socket
import json

#Creating a socket 
def create_socket():
    return socket.socket()

def create_connection():
    global my_socket 
    global host
    global port
    
    while True:
        #create a new socket every iteration
        my_socket = create_socket()
        
        #make the connection
        my_socket.connect(('localhost', 8080))

        #Send message for the server
        welcome_message()

        
        #json list from server. The command list for menu
        listCommands= my_socket.recv(1024).decode()
        listCommandsArray=json.loads(listCommands)
     
        
        print("\n++++++MENU++++++")
        for i in listCommandsArray:
            print(f"✅ {i}")
            
        # #Message from server. 1024 make reference to the buffer
        # response01= my_socket.recv(1024)
        # print(response01.decode())
        
        #Ask shell commands
        print("\n------------------------------")
        command = input("type a shell command from the list and see how it works: ")
        print("------------------------------")
        
        #calling the send_command function
        send_command(command)
        
        response_server()
        
        # my_socket.close()

#function to send the shell command to the server
def send_command(command):
  
  
    if len(str.encode(command)) > 0:
        my_socket.send(command.encode())
          
    if command.lower() == "exit":
        print("Finish the client...")
        my_socket.close()  
        
        
        

#funciton that handle the response from the server
def response_server():
    response02= my_socket.recv(1024).decode()
    print(response02)
    print("---------------------------")
    print("---------------------------")
    
     
#Function that send welcome message to the server
def welcome_message():
    my_socket.send("Hi from client!".encode())
    

def main():
    create_socket()
    create_connection()

main()
    

