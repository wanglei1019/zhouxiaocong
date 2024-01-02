# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setTextFormat(QtCore.Qt.AutoText)
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.name_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.name_edit.setObjectName("name_edit")
        self.horizontalLayout_2.addWidget(self.name_edit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 90, 221, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.password_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.password_edit.setObjectName("password_edit")
        self.horizontalLayout_3.addWidget(self.password_edit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 150, 221, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registerUser = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.registerUser.setFont(font)
        self.registerUser.setObjectName("registerUser")
        self.horizontalLayout.addWidget(self.registerUser)
        self.landUser = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.landUser.setFont(font)
        self.landUser.setObjectName("landUser")
        self.horizontalLayout.addWidget(self.landUser)
        self.success = QtWidgets.QLabel(self.centralwidget)
        self.success.setGeometry(QtCore.QRect(40, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.success.setFont(font)
        self.success.setText("")
        self.success.setObjectName("success")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-9, -6, 381, 271))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/ing.jpeg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.success.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 26))
        self.menubar.setObjectName("menubar")
        self.login = QtWidgets.QMenu(self.menubar)
        self.login.setObjectName("login")
        self.edit = QtWidgets.QMenu(self.menubar)
        self.edit.setObjectName("edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.login.menuAction())
        self.menubar.addAction(self.edit.menuAction())

        self.name_edit.textChanged['QString'].connect(self.saveName)
        self.password_edit.textChanged['QString'].connect(self.savePassword)
        # 设置为..
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.registerUser.clicked.connect(self.register)
        self.landUser.clicked.connect(self.land)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOG_IN"))
        self.name.setText(_translate("MainWindow", "账号："))
        self.password.setText(_translate("MainWindow", "密码："))
        self.registerUser.setText(_translate("MainWindow", "注册"))
        self.landUser.setText(_translate("MainWindow", "登陆"))

