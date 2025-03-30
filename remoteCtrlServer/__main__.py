from server.server_main import Server

address = 'localhost'
port = 8080

callServer = Server(address, port)
callServer.start_server()