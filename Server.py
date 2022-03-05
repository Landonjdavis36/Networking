import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conection from {address} has been established!")

    msg = "Welcome to the Server!"
    msg= f'{len(msg):^{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))
    