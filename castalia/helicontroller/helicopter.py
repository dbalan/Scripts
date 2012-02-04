import serial


class copter:
  def __init__(self, port_name, baud_rate,time_between):
    self.control = serial.Serial(port_name, baud_rate, timeout=0)
    print 'coptor connected', port_name, baud_rate, time_between
    self.init_dvalue = 50
    self.dvalue = self.init_dvalue
  
  def map_values(self,value):
    # Converts the integer values to corresponding ASCII
    # 256/100 = 2.56
    value = int(value * 2.55)
    char = chr(value)
    return char
    
    
  def adjust_rotor(self, value):
    # convert int to bit.
    # self.control.write()?
    sent_value = self.map_values(value)
    sent_value = "A"+str(sent_value)
    self.control.write(sent_value)
    print "Rotor set to:", sent_value
    
  def adjust_direction(self,direction, value):
    print direction
    # The direction PWM mapping is done here.
    if direction == 'x':
      direction = 'A'
    else if direction = 'y':
      direction = 'B'
    if self.dvalue > 0 and self.dvalue < 100:
      if value == '+':
	self.dvalue += 1
      else:
	self.dvalue -=1
    sent_value = self.map_values(self.dvalue)
    sent_value = str(direction)+str(sent_value)
    self.control.write(sent_value)
    print "sent value:", sent_value
    
  def init_direction(self):
    self.dvalue = self.init_dvalue;
   