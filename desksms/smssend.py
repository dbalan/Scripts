#!/usr/bin/env python2

# Connects to a phone via serial port and uses SMS in AT Text mode, though I am thinking about a PDU version soon.
# AT Commands from - http://www.developershome.com/sms/howToSendSMSFromPC.asp
# Author : Dhananjay Balan.
# 
# Depends : python-serial

import serial

# port to connect to
port_name="/def/rfcomm1"



# starting of program
def send(port, msg):
    # Todo implement error checking. (reading back should give same msg?)
    port.write(msg)
    return

def setMode(port, mode):
    if mode=="text":
        send(port, "AT+CMGF=1")
    return

def sendMsg(port, mode, no):
    if mode=="text":
        send(port, "AT+CMGS="+no)
        send(port, msg)
        

phone = serial.Serial(port_name)

setMode(phone, "text")

while True:
    No = raw_input("No>>")
    text = raw_input("Msg>>")
    sendMsg(phone, text, No)

    
