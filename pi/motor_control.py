
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

def stop():
    left_speed.write(0)         #function to stop
    right_speed.write(0)


def forward():
    left_direction.write(1)
    right_direction.write(0)            #function to go forwards etc...
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

def forward_left():
    left_direction.write(1)
    right_direction.write(0)
    left_speed.write(0.5)
    right_speed.write(1)

def forward_right():
    left_direction.write(1)
    right_direction.write(0)
    left_speed.write(1)
    right_speed.write(0.5)

def backward_left():
    left_direction.write(0)
    right_direction.write(1)
    left_speed.write(0.7)
    right_speed.write(1)

def backward_right():
    left_direction.write(0)
    right_direction.write(1)
    left_speed.write(1)
    right_speed.write(0.7)



try:
    forward()
    time.sleep(1)
    backward()
    time.sleep(1)               #test each function
    right()
    time.sleep(3)
    left()
    time.sleep(3)
finally:
    stop()
    board.exit()

