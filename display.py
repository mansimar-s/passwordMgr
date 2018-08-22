# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(428, 158)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 0, 0, 1, 1)
        self.LE_Username = QtWidgets.QLineEdit(Dialog)
        self.LE_Username.setObjectName("LE_Username")
        self.gridLayout.addWidget(self.LE_Username, 1, 0, 1, 1)
        self.label_pass = QtWidgets.QLabel(Dialog)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout.addWidget(self.label_pass, 2, 0, 1, 1)
        self.LE_Password = QtWidgets.QLineEdit(Dialog)
        self.LE_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_Password.setObjectName("LE_Password")
        self.gridLayout.addWidget(self.LE_Password, 3, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)
        self.label_copied = QtWidgets.QLabel(Dialog)
        self.label_copied.setEnabled(True)
        self.label_copied.setStyleSheet("color: rgb(54, 188, 74);\n"
"font: 12pt \"Sans Serif\";")
        self.label_copied.setObjectName("label_copied")
        self.gridLayout.addWidget(self.label_copied, 5, 0, 1, 1)
        self.PB_Copy = QtWidgets.QPushButton(Dialog)
        self.PB_Copy.setObjectName("PB_Copy")
        self.gridLayout.addWidget(self.PB_Copy, 3, 1, 1, 1)
        self.PB_ClearClip = QtWidgets.QPushButton(Dialog)
        self.PB_ClearClip.setStyleSheet("color: rgb(255, 0, 0);")
        self.PB_ClearClip.setObjectName("PB_ClearClip")
        self.gridLayout.addWidget(self.PB_ClearClip, 5, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_username.setText(_translate("Dialog", "Username"))
        self.label_pass.setText(_translate("Dialog", "Password"))
        self.checkBox.setText(_translate("Dialog", "Show Password"))
        self.label_copied.setText(_translate("Dialog", "Password Copied!"))
        self.PB_Copy.setText(_translate("Dialog", "Copy"))
        self.PB_ClearClip.setText(_translate("Dialog", "Clear Clipboard"))

