import socket
import _thread

def threaded_client(connection, address):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(1024).decode()
        print('{0} from {1}:{2}'.format(data, address[0], address[1]))
        if data=='q':
            print('connection {1}:{2} closed'.format(data, address[0], address[1]))
            break
        connection.sendall(data.encode())
    connection.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 1234))
    print('Waiting to connection...')
    s.listen(3)
    threadCount = 0
    while True:
        conn, addr = s.accept()
        print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        _thread.start_new_thread(threaded_client, (conn, addr))
        threadCount += 1
        print('Thread №'+str(threadCount))
