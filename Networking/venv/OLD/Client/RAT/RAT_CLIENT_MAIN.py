#!/usr/bin/python

import socket


def main():
    print "In main - client"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("0.0.0.0", 12345))

    if str(client_socket.recv(1024)).strip().lower() == "hello":
        client_socket.send(raw_input("INPUT"))


if __name__ == "__main__":
    main()
