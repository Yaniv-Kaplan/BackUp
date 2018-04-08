import socket               # Import socket module

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = "0.0.0.0" # Get local machine name
port = 12345                 # Reserve a port for your service.
server_socket.bind((ip, port))        # Bind to the port
server_socket.listen(1)                 # Now wait for client connection.
i = 1
while True:

    client_socket, addr = server_socket.accept()     # Establish connection with client.
    print 'Got connection from', addr
    file = open(str(i) + 'torecv.gif', 'wb')
    print "Receiving..."
    buffer = client_socket.recv(1024)
    while (buffer):
        print "Receiving..."
        file.write(buffer)
        buffer = client_socket.recv(1024)
    file.close()
    print "Done Receiving"
    client_socket.send('Thank you for connecting')
    client_socket.close()                # Close the connection
    i += 1