import serial

class copter:
  def __init__(self, port_name, baud_rate):
    #self.control = serial.Serial(port_name, baud_rate, timeout=0)
    print 'coptor connected', port_name, baud_rate  
    self.dvalue = 50
    
  def adjust_rotor(self, value):
    # convert int to bit.
    # self.control.write()?
    print "Rotor set to:", value
    
  def adjust_direction(self,direction, value):
    print direction
    
    if self.dvalue > 0 and self.dvalue < 100:
      if value == '+':
	self.dvalue += 1
      else:
	self.dvalue -=1
    print self.dvalue
    
  def init_direction(self):
    self.dvalue = 50;
   