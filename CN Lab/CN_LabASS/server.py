import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is running...")

conn, addr = server.accept()
print("Connected:", addr)

# receive file data
data = conn.recv(10000).decode()

# save file
with open("received.txt", "w") as f:
    f.write(data)

# counting korbe
lines = data.count("\n") + 1
words = len(data.split())
chars = len(data)

result = f"Lines: {lines}, Words: {words}, Characters: {chars}"

conn.send(result.encode())
conn.close()