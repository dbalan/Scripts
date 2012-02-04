import serial


class copter:
  def __init__(self, port_name, baud_rate):
    #self.control = serial.Serial(port_name, baud_rate, timeout=0)
    print 'coptor connected', port_name, baud_rate  
    self.dvalue = 50
  
  def map_values(self,value):
    # Converts the integer values to corresponding ASCII
    # 256/100 = 2.56
    value = int(value * 2.56)
    char = chr(value)
    return char
    
    
  def adjust_rotor(self, value):
    # convert int to bit.
    # self.control.write()?
    sent_value = self.map_values(value)
    print "Rotor set to:", sent_value
    
  def adjust_direction(self,direction, value):
    print direction
    
    if self.dvalue > 0 and self.dvalue < 100:
      if value == '+':
	self.dvalue += 1
      else:
	self.dvalue -=1
    sent_value = self.map_values(self.dvalue)
    print sent_value
    
  def init_direction(self):
    self.dvalue = 50;
   