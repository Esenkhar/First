import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 1234))
    s.listen(10)
    i = 0
    while True:
        conn, addr = s.accept()
        i += 1
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print('{0} from {1} - connection {2}'.format(data.decode(), addr, i))
            conn.send(data)
        conn.close()
