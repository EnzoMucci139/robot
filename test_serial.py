import serial           #import PySerial
import time

romeo = serial.Serial("/dev/ttyACM0", 9600, timeout=2)          #open communication with Romeo
time.sleep(2)

romeo.write(b"F")                       #Send lettter F as bytes
response = romeo.readline()             #receives repsonse
string = response.decode()
message = string.strip()                #makes it readable and into a string
print(message)

romeo.close()                       #close serial connection