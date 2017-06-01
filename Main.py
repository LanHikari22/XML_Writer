import os
import sys
import XMLWriter
import socket

def portscan(server, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server, port))
        return True
    except:
        return False


if __name__ == "__main__":
    for i in range(0,256):
        if portscan("google.com", i):
            print("[+] Port %d is open!!" % (i))
        else:
            print("[-] Port %d is closed." % (i))


if __name__ == "__main0__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = 'google.com'
    port = 80 # HTTP port

    # server_ip = socket.getservbyname((server, port))
    request = "GET / HTTP/1.1\nHost: " + server + "\n\n"
    s.connect((server,port))
    s.send(request.encode())
    res = s.recv(4096)
    s.close()
    del s

    # Configuring Socket #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server = 'discordapp.com'
    port = 80
    s.connect((server,port))

    # Sending and Recieving Data #
    request = "GET / HTTP/1.1\nHost: " + server + "\n\n"
    s.send(request.encode())
    bufsize = 4096 # Anything from 2 to 4096?
    data = s.recv(bufsize)

    print(data.decode())

    # Remember to close connection #
    #s.close()


    # Console -- Try it yourself. whatever this is #
    while True:
        request = input("> Enter Request:\n")
        print("> Request Acknowledged. Sending...")
        s.send(request.encode())
        res = s.recv(4096)
        print("> Response:\n", res.decode())


