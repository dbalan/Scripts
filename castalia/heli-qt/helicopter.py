import serial

class copter:
  def __init__(self, port_name, baud_rate):
    #self.control = serial.Serial(port_name, baud_rate, timeout=0)
    print 'coptor connected', port_name, baud_rate  
      
  def adjust_rotor(self, value):
    # convert int to bit.
    # self.control.write()?
    print "Rotor set to:", value
    
  def adjust_direction(self,direction, value):
    print direction, value
 
   