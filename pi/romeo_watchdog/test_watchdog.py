import serial
import time

romeo = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(2)

try:
    romeo.write(b"F")
    time.sleep(1.5)
finally:
    romeo.write(b"X")
    romeo.close()