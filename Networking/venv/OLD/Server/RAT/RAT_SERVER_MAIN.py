#!/usr/bin/python

import socket

client_socket = socket.socket


def main():
    global client_socket

    print "In main - server"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(1)

    print "Server ready"

    client_socket = server_socket.accept()[0]
    client_socket.send("hello")

    print str(client_socket.recv(1024)).strip().lower()


if __name__ == "__main__":
    main()
