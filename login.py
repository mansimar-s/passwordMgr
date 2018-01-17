# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mainWindow



class Ui_MainWindow(object):
    """

   This sets up the UI for the login window

    """
    def setupUi(self, MainWindow):
        """
        Gets MainWindow varialbe of type QMainWindow or QDialog as specified by
        the user and creates the UI
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(450,200,0,0)
        MainWindow.resize(353, 175)
        MainWindow.setStyleSheet("background: rgb(0, 0, 0)")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Master = QtWidgets.QLabel(self.centralwidget)
        self.label_Master.setGeometry(QtCore.QRect(9, 29, 89, 22))
        self.label_Master.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeMono\";")
        self.label_Master.setObjectName("label_Master")

        self.LE_MasterPass = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_MasterPass.setGeometry(QtCore.QRect(104, 29, 221, 23))
        self.LE_MasterPass.setStyleSheet("color: rgb(255, 255, 255);")
        self.LE_MasterPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_MasterPass.setObjectName("LE_MasterPass")

        self.PB_login = QtWidgets.QPushButton(self.centralwidget)
        self.PB_login.setGeometry(QtCore.QRect(130, 80, 80, 23))
        self.PB_login.setStyleSheet("color: rgb(255, 255, 255)")
        self.PB_login.setObjectName("PB_login")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Master.setText(_translate("MainWindow", "MASTER:"))
        self.PB_login.setText(_translate("MainWindow", "LOGIN"))



