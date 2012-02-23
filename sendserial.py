# send the argumnet to serial port.

import serial
import sys

port='/dev/ttyUSB0'
baudrate=9600

device= serial.Serial(port,baudrate)


try:
  device.write(sys.argv[1])
except IndexError:
  print "Specify value to send!!"
  