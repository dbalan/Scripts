import serial


class copter:
  def __init__(self, port_name, baud_rate,time_between):
    self.control = serial.Serial(port_name, baud_rate, timeout=0)
    print 'coptor connected', port_name, baud_rate, time_between
    
    self.rotor=0
    # Direction Intitlisation value
    self.init_dvalue = 50
    # Rotor base value.
    self.rotor_base = 50
    self.direction_base = 100
    self.dvalue = self.init_dvalue
  
  def map_values(self,value, base):
    # Converts the integer values to corresponding ASCII
    step = 256/base
    value = int(value * step)
    char = chr(value)
    return char
    
    
  def adjust_rotor(self, direction):
    # convert int to bit.
    # self.control.write()?
    if direction == "+":
      if self.rotor < 50:
	self.rotor += 1
      else:
	return
    else:
	if self.rotor > 0:
	  self.rotor -= 1
	else:
	  return
      
    sent_value = self.map_values(self.rotor, self.rotor_base)
    sent_value = "A"+str(sent_value)
    self.control.write(sent_value)
    print "Rotor set to:", sent_value
    
  def adjust_direction(self,direction, value):
    print direction
    # The direction PWM mapping is done here.
    if direction == 'x':
      direction = 'B'
    else:
	if direction == 'y':
	  direction = 'C'
    if self.dvalue > 0 and self.dvalue < 100:
      if value == '+':
	self.dvalue += 1
      else:
	self.dvalue -=1
    sent_value = self.map_values(self.dvalue, self.direction_base)
    sent_value = str(direction)+str(sent_value)
    self.control.write(sent_value)
    print "sent value:", sent_value
    
  def init_direction(self):
    self.dvalue = self.init_dvalue;
   