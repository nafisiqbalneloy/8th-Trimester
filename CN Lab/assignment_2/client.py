import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

# file read
with open("test.txt", "r") as f:
    data = f.read()

# send file
client.send(data.encode())

# receive result
result = client.recv(1024).decode()
print("Server Result:", result)

client.close()