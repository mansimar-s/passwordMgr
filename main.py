#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMainWindow, QDialog
import login, mainWindow
import pickle
import base64
import security
import display
from cryptography.fernet import Fernet


class pass_loginWin(QMainWindow, login.Ui_MainWindow):

    """
        Class for adding interaction ability to the login window of the
        application.
        Inherits from QMainWindow and
        inherits UI from the login module
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.PB_login.clicked.connect(self.btn_click)
        self.LE_MasterPass.returnPressed.connect(self.btn_click)
        self.centeronScreen()

    def btn_click(self):
        with open("mysec.txt", 'rb') as f:

            if security.myHash(self.LE_MasterPass.text()) == f.read():

                self.close()
                self.mainWin = pass_mainWin(self.LE_MasterPass.text())
                self.mainWin.show()
            else:
                self.LE_MasterPass.setText(None)
                self.InvalidBox = QtWidgets.QMessageBox()
                self.InvalidBox.setText("Password is Invalid")
                self.InvalidBox.exec_()

    def centeronScreen(self):
        """
            Gets the screen resolution and centers the window accorging to it.
        """

        resolution = QtWidgets.QDesktopWidget().screenGeometry()

        self.move(((resolution.width() / 2) - (self.frameSize().width() / 2)),
        ((resolution.height() / 2 ) - (self.frameSize().height() /2)))



class pass_mainWin(QMainWindow, mainWindow.Ui_mainWindow):

    """
        Class for interacting with the main window of the application.
        Inherits from QMainWindow and inherits UI from the mainWindow module
    """

    def __init__(self, myPass):

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.centeronScreen()

        self.btn_Delete.clicked.connect(self.btn_click)
        self.commandLinkButton.clicked.connect(self.btn_click)
        self.btn_AddNew.clicked.connect(self.btn_click)
        self.passDict = None



        my_fer_key = security.make_ferKey(myPass)
        self.fer = Fernet(my_fer_key)
        with open("pass_dictMain.txt", 'rb+') as f:
            token = self.fer.decrypt(f.read())

        self.passDict = pickle.loads(token)

        self.CB_Delete.addItems(sorted(self.passDict.keys()))
        self.CB_View.addItems(sorted(self.passDict.keys()))

    def btn_click(self):
        """
            Adds the main functionality of the app for deleting, adding, and
            viewing stored entries
        """
        button = self.sender()

        if button.text() == "Delete":
            del self.passDict[self.CB_Delete.currentText()]
            self.dltBox = QtWidgets.QMessageBox()
            self.dltBox.setText("Password Entry Deleted Successfully.")
            self.dltBox.exec_()

        if button.text() == "Add":
            serv = self.LE_AddServ.text()
            self.passDict[serv]= (self.LE_AddUser.text(), self.LE_AddPass.text())
            self.LE_AddServ.setText(None)
            self.LE_AddUser.setText(None)
            self.LE_AddPass.setText(None)

            # Message box for displaying password added
            self.AddBox = QtWidgets.QMessageBox()
            self.AddBox.setText("Password Entry Added Successfully.")
            self.AddBox.exec_()



        if button.text() == "Go":

            self.details = (self.passDict[self.CB_View.currentText()][0],\
            self.passDict[self.CB_View.currentText()][1],self.CB_View.currentText())

            self.DisplayWin = displayWin(self.details)
            self.DisplayWin.show()

        #
        # Writing to the database file after updation of entries
        #

        with open('pass_dictMain.txt', 'wb') as f:
            f.seek(0)
            f.truncate()
            to_write_data = self.fer.encrypt(pickle.dumps(self.passDict))

            f.write(to_write_data)


        self.CB_Delete.clear()
        self.CB_View.clear()
        self.CB_Delete.addItems(sorted(self.passDict.keys()))
        self.CB_View.addItems(sorted(self.passDict.keys()))

    def centeronScreen(self):

        """
            Gets the screen resolution and centers the window accorging to it.
        """

        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(((resolution.width() / 2) - (self.frameSize().width() / 2)),
        ((resolution.height() / 2 ) - (self.frameSize().height() /2)))




class displayWin(QDialog, display.Ui_Dialog):

    """
        Class for the password display window
        Inherits from QDialog and gets UI from display.py
    """

    def __init__(self, d):
        QDialog.__init__(self)
        self.setupUi(self)
        self.centeronScreen()
        self.d = d

        self.PB_Copy.clicked.connect(self.copyPass)
        self.PB_ClearClip.clicked.connect(self.clearclip)
        self.LE_Username.setText(d[0])
        self.LE_Password.setText(d[1])
        self.setWindowTitle(("Your Details for {}".format(d[2])))
        self.label_copied.hide()
        self.checkBox.stateChanged.connect(self.checked)

    def copyPass(self):
        cb = QApplication.clipboard()
        cb.setText(self.LE_Password.text())


    def clearclip(self):

        cb.clear()


    def checked(self, state):
        if state == 0:
            self.LE_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.LE_Password.setEchoMode(QtWidgets.QLineEdit.Normal)


    def centeronScreen(self):
        """
        Gets the screen resolution and centers the window accorging to it.
        """


        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(((resolution.width() / 2) - (self.frameSize().width() / 2)),
        ((resolution.height() / 2 ) - (self.frameSize().height() /2)))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWin = pass_loginWin()
    loginWin.show()

    sys.exit(app.exec_())
