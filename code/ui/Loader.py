from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from pathlib import Path
sys.path.insert(1, str(Path(__file__).parents[2].absolute()))
sys.path.insert(2, str(Path(__file__).parents[1].absolute()))
sys.path.extend([str(Path(__file__).parents[1] / "src")])
print(sys.path)
import GUI

class UIWindow(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.loadingScreen(self)

def main():
    app = QApplication(sys.argv)
    with open('stylesheet.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)
    form = UIWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()