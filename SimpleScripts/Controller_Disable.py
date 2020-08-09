from PyQt5 import QtWidgets, QtCore, uic, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialogButtonBox
import subprocess
import pprint
import os, sys
pp = pprint.PrettyPrinter()

QMainWindow = QtWidgets.QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # self.ui = uic.loadUi("ui\keyboard.ui", self)

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )

        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(750, 500),
                QtWidgets.qApp.desktop().availableGeometry()
            ))

        self.setStyleSheet("""QToolTip { 
                                   background-color: black; 
                                   color: white; 
                                   border: black solid 1px
                                   }""")

        labelNew = QtWidgets.QPushButton("test", self)
        labelNew.setToolTip("The Key(s) are:  Modifier: ")
        labelNew.resize(150, 30)
        labelNew.clicked.connect(self.toggle_controller)
        
        self.show()

    # @pyqtSlot()
    def testClick(self):
        print("click")
        
        dlg = CustomDialog(self)
        
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")

    def toggle_controller(self):
        print("click")
        
        dlg = CustomDialog(self)
        
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
        
        # find all devices command
        Find_command = 'devcon.exe find *'

        #list HW ids of devices
        hwIds_command = 'devcon.exe hwids *'

        #Enable
        Enable_command = 'devcon.exe enable *PID_1016'

        #Disable
        Disable_command = 'devcon.exe disable *Razer*'

        #Find Device
        Find_SpecificDevice_command = 'devcon.exe find *Razer*'

        find= True

        try:
            if find:
                result = subprocess.check_output(hwIds_command,shell=True ,stderr=subprocess.STDOUT)
                print(result)
        except subprocess.CalledProcessError as e:
            # raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            output = e.output
            results = "reboot" in str(output)
            if results:
                print("Would you like to reboot?")

class CustomDialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):


        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Test")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()