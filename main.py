#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Nov 26 22:22:23 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from socket import *

import threading
import time
import sys
import os

sys.path.append('/home/Py/encript')

from primeNum import primeNum
from DSGost import DSGost
from stribog import GOST
from user import User


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Client:
    def __init__(self, host='localhost', port=52004):
        self.socket = socket()
        self.socket.connect((host,port))
    def send(self,command):
        self.socket.send(command)
    def close(self):
        self.socket.close()


class Ui_MainWindow(QtGui.QWidget):
    __msg = None

    #login    = 'user'
    #password = 'password'
    myPort     = 52010
    clPort     = 52020
    

    def __init__(self, parent = None):
        
        QtGui.QWidget.__init__(self, parent)
        self.login    = self.showDialog('Авторизация', 'Введите логин')
        inputPassword = self.showDialog('Авторизация', 'Введите пароль')
        self.myUser   = User(self.login, self.myPort)

        if self.myUser.password is None:
            self.password = self.myUser.reg(inputPassword)

        if self.myUser.password != hex(GOST(256).hash(inputPassword.encode('hex') + self.login.encode('hex'))):
            self.error('Ошибка','Неверный логин или пароль')

        self.myUser.start()
        t = threading.Thread(target=self.listen)
        t.daemon = True
        t.start()  

        QtCore.QObject.connect(self,QtCore.SIGNAL("msg(QString)"),self.showMsg) 


    def listen(self):
        host = 'localhost'
        p    = self.myPort

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((host, p))
        self.socket.listen(1)

        while 1:
            csocket, caddress = self.socket.accept()
            while 1:
                data = csocket.recv(4096)
                if not data: break
                self.__msg = data
                s = QtCore.QString()
                for i in self.__msg:
                    s.append(i)
                self.emit(QtCore.SIGNAL("msg(QString)"), s)

            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(370, 540, 98, 27))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 467, 461, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 461, 441))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sendButton.clicked.connect(self.send)

    def showDialog(self, title, request):
            
        text, ok = QtGui.QInputDialog.getText(self, _fromUtf8(title), 
            _fromUtf8(request))
            
        if ok:
            return str(text)

    def error(self, title, describe):
        QtGui.QMessageBox.critical(
        self,
        _fromUtf8(title),
        _fromUtf8(describe),
        QtGui.QMessageBox.Cancel
        )
        sys.exit(1)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", self.login, None))
        self.sendButton.setText(_translate("MainWindow", "Отправить", None))

    def send(self):
        #self.myUser.checkSign('test')
        self.__msg = self.textEdit.toPlainText()
        self.textBrowser.append(self.__msg)
        msg = (self.myUser.encryptMsg('test', str(self.__msg)))
        cl = Client(port = self.clPort)
        cl.send(QtCore.QString(msg))
        cl.close()
        self.textEdit.clear()
        
    def showMsg(self, msg):
        #self.myUser.checkSign('test')
        self.textBrowser.append(self.myUser.decryptMsg(msg))

                 
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())