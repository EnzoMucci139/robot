
import socket
import time
import serial

# Commands sent from PC to Romeo V2
commands = {
    "Forward": b"F",
    "Backward": b"B",
    "Left": b"L",
    "Right": b"R",
    "Forward Left": b"G",
    "Forward Right": b"H",
    "Backward Left": b"J",
    "Backward Right": b"K",
    "Stop": b"X"
}

romeo = None
server = None
connection = None

try:
    # Connect to Romeo V2
    romeo = serial.Serial("/dev/ttyACM0", 9600, timeout=1, write_timeout=1)
    time.sleep(2)
    romeo.write(b"X")

    # Create TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("0.0.0.0", 5000))
    server.listen(1)

    print("Waiting for connection...")

    connection, address = server.accept()
    print(f"Connected: {address}")

    connection.settimeout(0.1)

    buffer = ""
    previous_action = "Stop"
    last_heartbeat = time.monotonic()

    # Main receiving loop
    while True:

        try:
            data = connection.recv(1024)
        except socket.timeout:
            data = None

        # Check for disconnection
        if data == b"":
            print("PC disconnected")
            break

        # Check heartbeat
        elapsed = time.monotonic() - last_heartbeat

        if elapsed > 0.5:
            print("Heartbeat lost")
            break

        # Process received data
        if data is not None:
            buffer += data.decode()

        # Process complete messages
        while "\n" in buffer:
            first, remaining = buffer.split("\n", 1)
            buffer = remaining
            first = first.strip()

            if first in commands:

                # Update heartbeat
                last_heartbeat = time.monotonic()

                # Send command to Romeo
                romeo.write(commands[first])

                # Only print when action changes
                if first != previous_action:
                    print(first)
                    previous_action = first

# Always attempt to stop motors and close connections
finally:
    if romeo is not None:
        try:
            if romeo.is_open:
                romeo.write(b"X")
        except (serial.SerialException, OSError):
            pass
        finally:
            romeo.close()

    if connection is not None:
        connection.close()

    if server is not None:
        server.close()

    print("Motors stopped and connections closed")
