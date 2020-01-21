# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dominic\Desktop\project\newUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from importlib import reload
from inspect import getsourcefile
from os.path import abspath

import json
import socket
import os
import signal
import sys

newpath = str(os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(newpath)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.x = 0
        self.y = 0
        self._new_window = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 800)
        MainWindow.setMaximumSize(QtCore.QSize(760, 800))
        MainWindow.setStyleSheet("\n"
"background-image: url(:/newback/newbackground.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 8pt \"Agency FB\";")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 580, 200, 45))
        self.pushButton.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet("background-image: url(:/button/button1.html);\n"
"font: 8pt \"Yu Gothic\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 630, 200, 45))
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setStyleSheet("background-image: url(:/button/button1.css);\n"
"\n"
"font: 8pt \"Yu Gothic\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 530, 200, 45))
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setStyleSheet("background-image: url(:/finalbordd/button1.css);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 8pt \"Yu Gothic\";\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 760, 201))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 20pt \"Century Gothic\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 760, 321))
        self.label_2.setMaximumSize(QtCore.QSize(760, 16777215))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"background: transparent;")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.runTk)
        self.pushButton_4.clicked.connect(self.startLocalhost)
        self.pushButton_2.clicked.connect(self.closeIt)
        
    def runTk(self):
##        #global count
##        global var
##        #var = 0
##        #print (var)
##        if var is None:
##            var = 1
##            import generateTemplate
##            print(var)
##        var = 1
##        reload(generateTemplate)
        global x
        #import generateTemplate
        
        
        import generateTemplate1
        if self.x != 0:
            reload(generateTemplate1)
        #reload(generateTemplate1)
        self.x = self.x + 1
        #generateTemplate1.Application
    def runServerUpload(self):
        global y
        import serverWindow
        if self.y !=0:
            reload(serverWindow)
        self.y = self.y + 1
    def closeIt(self):
        sys.exit(0)
        
    def uploadToServer(self):
        self._new_window = NewWindow()
        self._new_window.show()
        #username = "dgargala"
        #password = "123123"
        #host = "compute.gaul.csd.uwo.ca"
        #port = 22

        #import pysftp
        #remotepath = '/'
        #localpath = './'
        #cnopts = pysftp.CnOpts()
        #cnopts.hostkeys = None

        #with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts, port=22) as sftp:
         #   sftp.put_r('../../src/', "/student/dgargala/app/work")
          #  print('Upload finished')

    def startLocalhost(self):
            from subprocess import Popen
            self.p1 = Popen(["npm", "test"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
                        
    def tryPort(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = False
        try:
            sock.bind(("127.0.0.1", port))
            result = True
        except:
            print("Server refreshed")
        sock.close()
        return result

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Make Edits"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Citizen Science Web Creator"))
        self.label_2.setText(_translate("MainWindow", "Welcome"))

import nui_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

