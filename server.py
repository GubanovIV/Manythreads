import socket
import threading

sock = socket.socket()
print("Boot up server")
sock.bind(('', 9090))
sock.listen(2)
print("Listening...")

def server():
	while True:
		try:
			conn, addr = sock.accept()
			print("Client connection")
			print(addr)

			msg = ''
			while True:
				data = conn.recv(1024)
				if not data:
					break
				print("Data receiving...")
				msg += data.decode()
				print("Data sending...")
				conn.send(data)
			print(msg)

		except KeyboardInterrupt:
			conn.send("Server disconnect".encode())

		print("Server stop")
		conn.close()
		fn = input()
		if fn == "end":
			print('Thread off')
			break

ports = [threading.Thread(target=server) for i in range(2)]
for i in ports:
	i.start()
