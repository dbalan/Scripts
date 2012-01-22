import sys
from PyQt4 import QtCore, QtGui
from gui import Ui_Dialog
from helicopter import copter


class mainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    self.device = copter('/dev/ttyUSB0', 115200)
    
  #def event(self, event):
  #print event.type()
  #if (event.type()==QtCore.QEvent.KeyPress) and (event.key()==QtCore.Qt.Key_Tab):
  #self.emit(QtCore.SIGNAL("tabPressed"))
  #return True
      
    QtCore.QObject.connect(self.ui.verticalSlider, QtCore.SIGNAL("sliderMoved(int)"), self.adjust_rotor)
    QtCore.QObject.connect(self.ui.verticalSlider, QtCore.SIGNAL("valueChanged(int)"), self.adjust_rotor)
    QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), QtCore.QCoreApplication.instance().quit)
    QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL("leftPressed"), lambda: self.device.adjust_direction('x', '-'))
    QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL("rightPressed"), lambda: self.device.adjust_direction('x', '+'))
    QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL("downPressed"), lambda: self.device.adjust_direction('y', '-'))
    QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL("upPressed"), lambda: self.device.adjust_direction('y', '+'))
    QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL("directionReleased"), self.device.init_direction)
   
    
  def adjust_rotor(self, value):
    self.ui.label_2.setText(str(value))
    self.device.adjust_rotor(value)  

def main():
  app = QtGui.QApplication(sys.argv)
  heliapp = mainWindow()
  heliapp.show()
  sys.exit(app.exec_())
  
  
if __name__ == '__main__':
  main()

    