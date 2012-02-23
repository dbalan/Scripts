# send the argumnet to manage a bluetooth serial port.

import serial
import sys

port='/dev/ttyUSB0'
baudrate=9600

device= serial.Serial(port,baudrate)


device.write('LLL')

while True:
  value = raw_input("$ ")
  
  try:
    device.write(chr(0x0D)+chr(0x0A))
    device.write(value)
    device.write(chr(0x0D)+chr(0x0A))
  except:
    print "Somethings burning!!"
    exit()