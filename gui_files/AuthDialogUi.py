# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuthDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthDialog(object):
    def setupUi(self, AuthDialog):
        AuthDialog.setObjectName("AuthDialog")
        AuthDialog.resize(467, 277)
        self.AuthLabel = QtWidgets.QLabel(AuthDialog)
        self.AuthLabel.setGeometry(QtCore.QRect(130, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AuthLabel.setFont(font)
        self.AuthLabel.setObjectName("AuthLabel")
        self.InfoAuthLableabel = QtWidgets.QLabel(AuthDialog)
        self.InfoAuthLableabel.setGeometry(QtCore.QRect(40, 60, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InfoAuthLableabel.setFont(font)
        self.InfoAuthLableabel.setScaledContents(False)
        self.InfoAuthLableabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoAuthLableabel.setObjectName("InfoAuthLableabel")
        self.LoginLabel = QtWidgets.QLabel(AuthDialog)
        self.LoginLabel.setGeometry(QtCore.QRect(140, 130, 41, 20))
        self.LoginLabel.setObjectName("LoginLabel")
        self.PasswordLabel = QtWidgets.QLabel(AuthDialog)
        self.PasswordLabel.setGeometry(QtCore.QRect(130, 170, 51, 20))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.LoginEdit = QtWidgets.QLineEdit(AuthDialog)
        self.LoginEdit.setGeometry(QtCore.QRect(190, 130, 141, 22))
        self.LoginEdit.setObjectName("LoginEdit")
        self.PasswordEdit = QtWidgets.QLineEdit(AuthDialog)
        self.PasswordEdit.setGeometry(QtCore.QRect(190, 170, 141, 22))
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.LoginButton = QtWidgets.QPushButton(AuthDialog)
        self.LoginButton.setGeometry(QtCore.QRect(150, 210, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.LoginButton.setPalette(palette)
        self.LoginButton.setObjectName("LoginButton")
        self.BackButton = QtWidgets.QPushButton(AuthDialog)
        self.BackButton.setGeometry(QtCore.QRect(240, 210, 81, 31))
        self.BackButton.setObjectName("BackButton")
        self.ErrorLabel = QtWidgets.QLabel(AuthDialog)
        self.ErrorLabel.setGeometry(QtCore.QRect(134, 110, 211, 20))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(AuthDialog)
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)

    def retranslateUi(self, AuthDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthDialog.setWindowTitle(_translate("AuthDialog", "Dialog"))
        self.AuthLabel.setText(_translate("AuthDialog", "Авторизация"))
        self.InfoAuthLableabel.setText(_translate("AuthDialog", "Пожалуйста, авторизуйтесь в системе, используя\n"
" Ваш логин и пароль"))
        self.LoginLabel.setText(_translate("AuthDialog", "Логин:"))
        self.PasswordLabel.setText(_translate("AuthDialog", "Пароль:"))
        self.LoginButton.setText(_translate("AuthDialog", "Войти"))
        self.BackButton.setText(_translate("AuthDialog", "Назад"))

