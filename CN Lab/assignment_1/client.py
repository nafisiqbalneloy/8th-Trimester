import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

hours = input("Enter hours worked: ")

client.send(hours.encode())

salary = client.recv(1024).decode()

print("Salary = Tk", salary)

client.close()