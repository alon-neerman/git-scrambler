import sys
import serial
import time

scanner = serial.Serial("/dev/ttyACM0",9600,timeout=0.5)

print("serial test start...")
while scanner != None:
    f = open("barcode_data.txt", "a")
    print("serial ready...")
    s = scanner.read(100)
    barcode = s.decode()
    if barcode != "":
        f.write(barcode)
        f.close()
    print(barcode)