import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for connection...")

connection, address = server.accept()

print(f"Connected: {address}")

while True:
    data = connection.recv(1024)
    if not data:
        break
  
    data = data.decode()
    message = data.strip()
    print(message) 

connection.close()
server.close()