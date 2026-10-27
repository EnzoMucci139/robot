
from pyfirmata2 import Arduino
import time

# Connect to Romeo
board = Arduino("/dev/ttyACM0")

# Configure motor pins
left_direction = board.get_pin("d:4:o")
left_speed = board.get_pin("d:5:p")

right_speed = board.get_pin("d:6:p")
right_direction = board.get_pin("d:7:o")

# Start with both motors stopped
left_speed.write(0)
right_speed.write(0)

# We'll add motor control here
def stop():
    left_speed.write(0)
    right_speed.write(0)


def forward():
    left_direction.write(1)
    right_direction.write(0)
    left_speed.write(1)
    right_speed.write(1)

def backward():
    left_direction.write(0)
    right_direction.write(1)
    left_speed.write(1)
    right_speed.write(1)

def left():
    left_direction.write(1)
    right_direction.write(1)
    left_speed.write(1)
    right_speed.write(1)

def right():
    left_direction.write(0)
    right_direction.write(0)
    left_speed.write(1)
    right_speed.write(1)

def left_forward():
    left_direction.write(1)
    right_direction.write(1)
    left_speed.write(0.7)
    right_speed.write(1)

def right_forward():
    left_direction.write(0)
    right_direction.write(0)
    left_speed.write(1)
    right_speed.write(0.7)


try:
    forward()
    time.sleep(1)
    backward()
    time.sleep(1)
    right()
    time.sleep(3)
    left()
    time.sleep(3)
finally:
    stop()
    board.exit()

