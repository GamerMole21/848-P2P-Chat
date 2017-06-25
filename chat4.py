#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat4.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import socket
import sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text = ''
mode = ''
name = 'You'
rname = 'Them'

def update_list(self, user, data):
        self.listWidget.addItem(user + ": " + data)

def incomingLoop(self, s):
    while True:
        data = s.recv(100).decode()
        if data.find("name=") == 1:
            global rname
            rname = data.replace("name=", '')
            rname = rname.replace("\r\n", '')

        elif data.find("**clear") == 1:
            clear_chat()

        else:
            update_list(self, rname, data)

def readSocketAndOutput(s):
    while True:
        try:
            text = s.recv(100).decode()
            #self.recieveMSG()
            #self.listWidget.addItem(rname + ": " + text)
            if data.find("name=") == 1:
                global rname
                rname = data.replace("name=", '')
                rname = rname.replace("\r\n", '')

            elif data.find("**clear") == 1:
                clear_chat()

            else:
                update_list(self, rname, data)
        except:
            break

def readSTDINandWriteSocket(s):
        s.send(text.encode())

def app_version():
        msg_box("Application Version", "Mole P2P Chat v0.1")

def msg_box(title, data):
        w = QWidget()
        QMessageBox.information(w, title, data)

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

class Ui_MoleP2PWindow(object):
    def setupUi(self, MoleP2PWindow):
        MoleP2PWindow.setObjectName(_fromUtf8("MoleP2PWindow"))
        MoleP2PWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MoleP2PWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 781, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 6, 66, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.box_enterIP = QtGui.QLineEdit(self.frame)
        self.box_enterIP.setGeometry(QtCore.QRect(74, 5, 241, 21))
        self.box_enterIP.setObjectName(_fromUtf8("box_enterIP"))
        self.button_confirmIP = QtGui.QPushButton(self.frame)
        self.button_confirmIP.setGeometry(QtCore.QRect(320, 5, 131, 21))
        self.button_confirmIP.setObjectName(_fromUtf8("button_confirmIP"))
        self.button_confirmIP.clicked.connect(self.set_ip)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(467, 6, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.box_enterPort = QtGui.QLineEdit(self.frame)
        self.box_enterPort.setGeometry(QtCore.QRect(504, 5, 131, 21))
        self.box_enterPort.setObjectName(_fromUtf8("box_enterPort"))
        self.button_confirmPort = QtGui.QPushButton(self.frame)
        self.button_confirmPort.setGeometry(QtCore.QRect(640, 5, 131, 21))
        self.button_confirmPort.setObjectName(_fromUtf8("button_confirmPort"))
        self.button_confirmPort.clicked.connect(self.set_port)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 50, 201, 141))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.button_host = QtGui.QPushButton(self.frame_2)
        self.button_host.setGeometry(QtCore.QRect(20, 40, 161, 41))
        self.button_host.clicked.connect(self.host)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_host.setFont(font)
        self.button_host.setObjectName(_fromUtf8("button_host"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.button_join = QtGui.QPushButton(self.frame_2)
        self.button_join.setGeometry(QtCore.QRect(20, 90, 161, 41))
        self.button_join.clicked.connect(self.join)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_join.setFont(font)
        self.button_join.setObjectName(_fromUtf8("button_join"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 200, 201, 351))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_ip = QtGui.QLabel(self.frame_3)
        self.label_ip.setGeometry(QtCore.QRect(10, 120, 66, 18))
        self.label_ip.setObjectName(_fromUtf8("label_ip"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_port = QtGui.QLabel(self.frame_3)
        self.label_port.setGeometry(QtCore.QRect(10, 180, 66, 18))
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.button_leave = QtGui.QPushButton(self.frame_3)
        self.button_leave.setGeometry(QtCore.QRect(20, 300, 161, 41))
        self.button_leave.clicked.connect(self.leave_chat)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_leave.setFont(font)
        self.button_leave.setObjectName(_fromUtf8("button_leave"))
        self.button_clear = QtGui.QPushButton(self.frame_3)
        self.button_clear.setGeometry(QtCore.QRect(20, 250, 161, 41))
        self.button_clear.clicked.connect(self.clear_chat)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName(_fromUtf8("button_clear"))
        self.check_crypt = QtGui.QCheckBox(self.frame_3)
        self.check_crypt.setGeometry(QtCore.QRect(50, 218, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.check_crypt.setFont(font)
        self.check_crypt.setObjectName(_fromUtf8("check_crypt"))
        self.label_6 = QtGui.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.box_enterName = QtGui.QLineEdit(self.frame_3)
        self.box_enterName.setGeometry(QtCore.QRect(30, 30, 141, 21))
        self.box_enterName.setObjectName(_fromUtf8("box_enterName"))
        self.button_confirmName = QtGui.QPushButton(self.frame_3)
        self.button_confirmName.setGeometry(QtCore.QRect(50, 60, 101, 21))
        self.button_confirmName.setObjectName(_fromUtf8("button_confirmName"))
        self.button_confirmName.clicked.connect(self.setName)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(220, 50, 571, 501))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.button_send = QtGui.QPushButton(self.frame_4)
        self.button_send.setGeometry(QtCore.QRect(420, 460, 141, 31))
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.button_send.clicked.connect(self.sendMSG)
        self.box_sendMessage = QtGui.QLineEdit(self.frame_4)
        self.box_sendMessage.setGeometry(QtCore.QRect(10, 460, 401, 30))
        self.box_sendMessage.setObjectName(_fromUtf8("box_sendMessage"))
        self.listWidget = QtGui.QListWidget(self.frame_4)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 551, 441))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MoleP2PWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MoleP2PWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MoleP2PWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MoleP2PWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MoleP2PWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MoleP2PWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(MoleP2PWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MoleP2PWindow)
        QtCore.QMetaObject.connectSlotsByName(MoleP2PWindow)

    def incomingLoop(s):
        while True:
            data = s.recv(100).decode()
            if data.find("name=") == 1:
                global rname
                rname = data.replace("name=", '')
                rname = rname.replace("\r\n", '')

            elif data.find("**clear") == 1:
                clear_chat()

            else:
                update_list(self, rname, data)

    def sendMSG(self):
        if mode == "H":
            text = self.box_sendMessage.text()
            s.send(text.encode())
            self.box_sendMessage.setText("")
            update_list(self, name, text)
        else:
            text = self.box_sendMessage.text()
            c.send(text.encode())
            self.box_sendMessage.setText("")
            update_list(self, name, text)

    def prepMSG(self):
        self.listWidget.clear()
        #self.listWidget.addItem("<# " + text)

    def clear_chat(self):
        self.listWidget.clear()
        if mode == "H":
            s.send("**clear".encode())
        else:
            c.send("**clear".encode())

    def leave_chat(self):
        s.close()
        msg_box("Disconnected", "You Have Left")
        sys.exit()

    def retranslateUi(self, MoleP2PWindow):
        MoleP2PWindow.setWindowTitle(_translate("MoleP2PWindow", "Mole P2P Chat", None))
        self.label.setText(_translate("MoleP2PWindow", "Their IP:", None))
        self.button_confirmIP.setText(_translate("MoleP2PWindow", "Confirm", None))
        self.label_4.setText(_translate("MoleP2PWindow", "Port:", None))
        self.button_confirmPort.setText(_translate("MoleP2PWindow", "Confirm", None))
        self.button_host.setText(_translate("MoleP2PWindow", "Host", None))
        self.label_2.setText(_translate("MoleP2PWindow", "      Host or Join?", None))
        self.button_join.setText(_translate("MoleP2PWindow", "Join", None))
        self.label_3.setText(_translate("MoleP2PWindow", "Connected To:", None))
        self.label_ip.setText(_translate("MoleP2PWindow", "N/A", None))
        self.label_5.setText(_translate("MoleP2PWindow", "Port:", None))
        self.label_port.setText(_translate("MoleP2PWindow", "N/A", None))
        self.button_leave.setText(_translate("MoleP2PWindow", "Leave", None))
        self.button_clear.setText(_translate("MoleP2PWindow", "Clear Chat", None))
        self.check_crypt.setText(_translate("MoleP2PWindow", "Encryption", None))
        self.label_6.setText(_translate("MoleP2PWindow", "Your Name", None))
        self.button_confirmName.setText(_translate("MoleP2PWindow", "Confirm", None))
        self.button_send.setText(_translate("MoleP2PWindow", "Send", None))
        self.menuFile.setTitle(_translate("MoleP2PWindow", "File", None))
        self.actionAbout.setText(_translate("MoleP2PWindow", "About", None))
        self.actionExit.setText(_translate("MoleP2PWindow", "Exit", None))

    def set_ip(self):
        ip_address = self.box_enterIP.text()
        msg_box("Success", ip_address + " Has Been Set As The IP")

    def set_port(self):
        port = self.box_enterPort.text()
        msg_box("Success", port + " Has Been Set As The Port")

    def setName(self):
        global name
        name = self.box_enterName.text()
        if mode == "H":
            s.send(("name=" + name).encode())
        else:
            c.send(("name=" + name).encode())

        msg_box("Success", name + " Has Been Set As Your Name")


    def host(self):
        global mode
        mode = "H"
        ip_address = self.box_enterIP.text()
        port = int(self.box_enterPort.text())
        s.connect((ip_address, port))
        threading.Thread(target=incomingLoop, args=(self, s,)).start()
        #threading.Thread(target=socketIn, args=(s,)).start()
        self.prepMSG()
        self.label_ip.setText(ip_address)
        self.label_port.setText(self.box_enterPort.text())
        msg_box("Hosting", "You Are Now Hosting")


    def join(self):
        global mode
        mode = "J"
        host = ''
        port = int(self.box_enterPort.text())
        msg_box("Ready", "Ready To Join")
        s.bind((host, port))
        s.listen(2)
        self.label_ip.setText("Joined")
        self.label_port.setText(str(port))
        c, addr = s.accept()
        threading.Thread(target=incomingLoop, args=(self, c,)).start()
        #threading.Thread(target=socketIn, args=(c,)).start()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MoleP2PWindow = QtGui.QMainWindow()
    ui = Ui_MoleP2PWindow()
    ui.setupUi(MoleP2PWindow)
    MoleP2PWindow.show()
    sys.exit(app.exec_())
