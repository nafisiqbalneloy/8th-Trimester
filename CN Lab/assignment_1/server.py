import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is waiting for a connection...")

conn, addr = server.accept()
print("Connected by:", addr)

hours = float(conn.recv(1024).decode())

if hours <= 40:
    salary = hours * 200
else:
    salary = 8000 + (hours - 40) * 300

conn.send(str(salary).encode())

conn.close()
server.close()