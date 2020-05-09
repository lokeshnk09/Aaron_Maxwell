import socket


s = socket.socket() # Create a socket object

HOST = socket.gethostbyname('vdi-test01.local')
PORT = 12345
print(HOST)
try:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data)
except OSError as e:
    print(e.args)






