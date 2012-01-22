from PyQt4 import QtGui, QtCore

class DirectionDial(QtGui.QDial):
    def __init__(self, *args):
        QtGui.QDial.__init__(self, *args)
        self.last_key=QtCore.Qt.Key_Left
        
    def event(self, event):
        if event.type()==QtCore.QEvent.KeyPress:
	  if event.key() != self.last_key:
	    self.last_key = event.key()
	    self.emit(QtCore.SIGNAL("directionReleased"))
	  if event.key()==QtCore.Qt.Key_Left:
            self.emit(QtCore.SIGNAL("leftPressed"))
	  if event.key()==QtCore.Qt.Key_Right:
            self.emit(QtCore.SIGNAL("rightPressed"))
          if event.key()==QtCore.Qt.Key_Up:
            self.emit(QtCore.SIGNAL("upPressed"))
          if event.key()==QtCore.Qt.Key_Down:
            self.emit(QtCore.SIGNAL("downPressed"))
          return True
        #if event.type()==QtCore.QEvent.KeyRelease:
	  #if (event.key()==QtCore.Qt.Key_Left) or (event.key()==QtCore.Qt.Key_Right):
	    #self.emit(QtCore.SIGNAL("directionReleased"))
	    #return True
	    
  
        return QtGui.QDial.event(self, event)