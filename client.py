import socket

try:
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect(('localhost', 9090))
    print("Connect to server")

    msg = input()
    sock.send(msg.encode())
    print("Data sending...")

    data = sock.recv(1024)
    print("Done")
except KeyboardInterrupt:
    sock.send("Client disconnect".encode())

sock.close()

print("Data receiving...")
print(data.decode())
