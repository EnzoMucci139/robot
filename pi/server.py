import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for connection...")

connection, address = server.accept()

print(f"Connected: {address}")

buffer = ""

while True:
    data = connection.recv(1024)
    if not data:
        break

    buffer += data.decode()

    while "\n" in buffer:
        first, remaining = buffer.split("\n", 1)
        buffer = remaining
        print(first)
    

connection.close()
server.close()