import socket               # Import socket module
import sys

print sys.argv
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
ip = "localhost" # Get local machine name
port = 12345                 # Reserve a port for your service.

client_socket.connect((ip, port))
file_handler = open('./mask.gif', 'rb')       #open file for reading
print 'Sending...'
buffer = file_handler.read(1024)
while (buffer):
    print 'Sending...'
    client_socket.send(buffer)
    buffer = file_handler.read(1024)
file_handler.close()
print "Done Sending"
client_socket.shutdown(socket.SHUT_WR)
print client_socket.recv(1024)
client_socket.close()                     # Close the socket when done