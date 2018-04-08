import socket               # Import socket module

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object

ip = "0.0.0.0"
port = 12345                 # Reserve a port for your service.
udp_socket.bind((ip, port))        # Bind to the port
udp_socket.settimeout(20)
address = (ip, port)
file = open('./torecv.gif', 'wb')
try:
    buffer, addr = udp_socket.recvfrom(1024)  # start get data from client.
    print 'Got connection from', addr

    while (buffer):
        print "Receiving..."
        file.write(buffer)
        buffer, addr = udp_socket.recvfrom(1024)
except socket.timeout:
    file.close()
    udp_socket.close()
    print "File Donwloaded"
