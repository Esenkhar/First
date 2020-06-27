import socket

req = 'Hello tcp!'
disconnect = False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while not disconnect:
        s.connect(('127.0.0.1', 1234))
        while True:
            req = input()
            if req == 'q':
                s.send(req.encode())
                disconnect = True
                break
            s.send(req.encode())
            rsp = s.recv(1024)
            print(rsp.decode())
