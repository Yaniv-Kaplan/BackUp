import socket               # Import socket module

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
ip = "localhost" # Get local machine name
port = 12345                 # Reserve a port for your service.
address = (ip, port)

file_handler = open('mask.gif', 'rb')       #open file for reading
print 'Sending...'

buffer = file_handler.read(1024)
while (buffer):
    print 'Sending...'
    client_socket.sendto(buffer, address)
    buffer = file_handler.read(1024)
file_handler.close()
print "File Donwloaded"
client_socket.close()                     # Close the socket when done