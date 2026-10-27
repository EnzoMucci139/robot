import socket
import time

valid_commands = {
    "Forward",
    "Backward",
    "Left",
    "Right",
    "Forward Left",
    "Forward Right",
    "Backward Left",
    "Backward Right",
    "Stop"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for connection...")

connection, address = server.accept()

print(f"Connected: {address}")

connection.settimeout(0.1)

buffer = ""

previous_action = None

last_heartbeat = time.monotonic()

while True:
    try:
        data = connection.recv(1024)
    except socket.timeout:
        data = None
    if data == b"":
        if data != "Stop":
            print("Stop")
            previous_action = "Stop"
        break
    if data is not None:
    
        buffer += data.decode()
    elapsed = time.monotonic() - last_heartbeat
    if elapsed > 0.5:
        if previous_action != "Stop":
            print("Stop")
            previous_action = "Stop"
        print("Heartbeat lost")
        break
        
    while "\n" in buffer:
        first, remaining = buffer.split("\n", 1)
        buffer = remaining
        first = first.strip()
        if first in valid_commands:
            last_heartbeat = time.monotonic()
            if first != previous_action:
                print(first)
                previous_action = first
        

connection.close()
server.close()