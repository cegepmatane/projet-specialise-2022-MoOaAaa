# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from code.src import Correcteur



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.correctBtn = QtWidgets.QPushButton(self.centralwidget)
        self.correctBtn.setGeometry(QtCore.QRect(0, 500, 89, 25))
        self.correctBtn.setObjectName("correctBtn")
        self.correctBtn.clicked.connect(self.correctClick)

        self.suppr_all = QtWidgets.QPushButton(self.centralwidget)
        self.suppr_all.setGeometry(QtCore.QRect(100, 500, 121, 25))
        self.suppr_all.setObjectName("suppr_all")

        self.correctedTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.correctedTxt.setGeometry(QtCore.QRect(405, 5, 390, 485))
        self.correctedTxt.setReadOnly(True)
        self.correctedTxt.setObjectName("correctedTxt")
        self.correctedScrollBar = self.correctedTxt.verticalScrollBar()
        self.correctedScrollBar.setValue(self.correctedScrollBar.maximum())

        self.textToCorrect = QtWidgets.QTextEdit(self.centralwidget)
        self.textToCorrect.setGeometry(QtCore.QRect(5, 5, 390, 485))
        self.textToCorrect.setObjectName("textToCorrect")
        self.textToCorrect.setPlaceholderText("Tapez du texte à corriger ou collez du texte")
        self.toCorrectScrollBar = self.textToCorrect.verticalScrollBar()
        self.toCorrectScrollBar.setValue(self.toCorrectScrollBar.maximum())

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Correcteur"))
        self.correctBtn.setText(_translate("MainWindow", "Corriger"))
        self.suppr_all.setText(_translate("MainWindow", "Tout supprimer"))

    def correctClick(self):
        correct = self.textToCorrect.toPlainText()
        print(correct)