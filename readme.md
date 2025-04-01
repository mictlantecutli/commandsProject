# Overview

In this networking project, I was curious to learn how to access files on another device, with the goal of facilitating the workflow, that is, not wasting time switching to the other device every time I need to do something on it. For me, it would be very convenient to modify, create, edit, and obtain information from another computer without having to physically access it.

This networking program connects a client and a server on my computer. Each has a separate space within the device to simulate two different devices. The server folder is called remoteCtrlServer, and the client folder is called remoteCtrlClient. I created the server with classes. The main file is located at the root of the same folder, so to access the server execution, you go outside the remoteCtrlServer folder and invoke the server in the terminal like this: >>python3 remoteCtrlServer. The client is just a file containing the main file that manages the program sequence, and it is invoked in the same file. So, to run the client and connect it to the server, you have to go to the remoteCtrlClient folder and type the following in the terminal: >>python3 client.py.

At startup, the client and the server connect, and initial messages are sent. The client then displays a menu of terminal commands, and the program prompts the user to type the command they want to see how it works. The user then types a terminal command, which is sent to the server, and the server executes it, sending the result to the client. This way, the client can view, create, and execute the command.

The purpose of this software is to access, create, and navigate files and folders on a server. I find it a useful tool to streamline workflow when I have useful information on different devices.

[Software Demo Video](https://www.youtube.com/watch?v=ZF5xh71FLGU)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}

Because I am handling files, writing files, and I want greater security in the information, I used TCP for sending information between the server and the client.

The format of the messages between the client and the server is in bytes, so to send I used encode, and to receive I used decode.

# Development Environment

To develop this project, I used Visual Studio Code for a better view of the software files.

I also used the terminal or several terminals a lot. I found it easier to create two terminals, managing the server in one and the client in the other. That way, I could see the behavior of both.

The language I used was Python because it has an easy-to-use networking library. The library is called socket.

I also used subprocess library to execute the 'ls' command.

The os library to navigate to another directory.

Finally, the json library to send an array to the client.

# Useful Websites

Websites helpful to develop this project:
https://en.wikipedia.org/wiki/OSI_model
* [Wikipedia - OSI](https://en.wikipedia.org/wiki/OSI_model)
* [Realpars - OSI](https://www.youtube.com/watch?v=Ilk7UXzV_Qc)
* [Fulldump - TCP](https://www.youtube.com/watch?v=eaqlfnvJQ1I)
* [Ben Eater - Networking tutorial](https://www.youtube.com/watch?v=F27PLin3TV0)
* [Documentation Python - sockets](https://docs.python.org/3/library/socket.html)
* [Código Facilito - youtube channel](https://www.youtube.com/watch?v=nJYp3_X_p6c)
* [Stackoverflow](https://stackoverflow.com/questions/74236528/i-cant-connect-to-pc-socket-server-with-mobile-socket-client-python)
* [Build with Python - youtube channel](https://www.youtube.com/watch?v=_FVvlJDQTxk)

# Future Work
* I need to improve the organization of my code, create more functions and methods. I feel like I have everything in a jumble due to lack of time.
* Implement exception handle
* Network on two different devices, not just one computer.