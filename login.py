# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 215)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.LE_MasterPass = QtWidgets.QLineEdit(self.tab)
        self.LE_MasterPass.setGeometry(QtCore.QRect(140, 20, 321, 23))
        self.LE_MasterPass.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LE_MasterPass.setStyleSheet("color: rgb(255, 255, 255);")
        self.LE_MasterPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_MasterPass.setCursorPosition(0)
        self.LE_MasterPass.setClearButtonEnabled(True)
        self.LE_MasterPass.setObjectName("LE_MasterPass")
        self.PB_login = QtWidgets.QPushButton(self.tab)
        self.PB_login.setGeometry(QtCore.QRect(190, 70, 80, 23))
        self.PB_login.setStyleSheet("")
        self.PB_login.setObjectName("PB_login")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 20, 87, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.LE_currentPass = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_currentPass.sizePolicy().hasHeightForWidth())
        self.LE_currentPass.setSizePolicy(sizePolicy)
        self.LE_currentPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_currentPass.setObjectName("LE_currentPass")
        self.gridLayout.addWidget(self.LE_currentPass, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.LE_newPass = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_newPass.sizePolicy().hasHeightForWidth())
        self.LE_newPass.setSizePolicy(sizePolicy)
        self.LE_newPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_newPass.setObjectName("LE_newPass")
        self.gridLayout.addWidget(self.LE_newPass, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.LE_newPassVerification = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_newPassVerification.sizePolicy().hasHeightForWidth())
        self.LE_newPassVerification.setSizePolicy(sizePolicy)
        self.LE_newPassVerification.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_newPassVerification.setObjectName("LE_newPassVerification")
        self.gridLayout.addWidget(self.LE_newPassVerification, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.PB_changePass = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_changePass.setObjectName("PB_changePass")
        self.verticalLayout.addWidget(self.PB_changePass)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PB_login.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "Password: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Enter Current Password"))
        self.label_3.setText(_translate("MainWindow", "Enter New Password"))
        self.label_4.setText(_translate("MainWindow", "Confirm New Password"))
        self.PB_changePass.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Change Password"))

