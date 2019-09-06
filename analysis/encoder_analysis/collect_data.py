import serial
import time
import csv

ser = serial.Serial('/dev/cu.usbmodem39556101')
ser.flushInput()

lines = [ser.readline().decode('utf8') for i in range(2 ** 20)]

# with open("ma702_data.csv", "a") as f:
with open("as5048a_data.csv", "a") as f:
    for s in lines:
        f.write(str(s))
