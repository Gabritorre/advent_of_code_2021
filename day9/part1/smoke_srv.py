import socket

s = socket.socket()
s.bind(("localhost", 1111))
s.listen()
conn, addr = s.accept()

input = open("input.txt", "r")
counter = 0
lines = []
for line in input.readlines():
	lines.append(line)
	counter += 1
conn.send(str(counter).encode())

for line in lines:
	conn.send(line.encode())
	confirm = conn.recv(256)
