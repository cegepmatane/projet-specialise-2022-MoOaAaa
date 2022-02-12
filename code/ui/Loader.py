from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import GUI

class UIWindow(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = UIWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()