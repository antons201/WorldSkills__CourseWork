# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompetitorWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CompetitorWindow(object):
    def setupUi(self, CompetitorWindow):
        CompetitorWindow.setObjectName("CompetitorWindow")
        CompetitorWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CompetitorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.ProfileButton = QtWidgets.QPushButton(self.MainFrame)
        self.ProfileButton.setGeometry(QtCore.QRect(260, 130, 201, 71))
        self.ProfileButton.setObjectName("ProfileButton")
        self.CompetitionButton = QtWidgets.QPushButton(self.MainFrame)
        self.CompetitionButton.setGeometry(QtCore.QRect(260, 240, 201, 71))
        self.CompetitionButton.setObjectName("CompetitionButton")
        self.ResultsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ResultsButton.setGeometry(QtCore.QRect(260, 350, 201, 81))
        self.ResultsButton.setObjectName("ResultsButton")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(280, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.GreetLabel = QtWidgets.QLabel(self.MainFrame)
        self.GreetLabel.setGeometry(QtCore.QRect(270, 50, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setObjectName("GreetLabel")
        self.NameLabel = QtWidgets.QLabel(self.MainFrame)
        self.NameLabel.setGeometry(QtCore.QRect(380, 50, 55, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        CompetitorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CompetitorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        CompetitorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CompetitorWindow)
        self.statusbar.setObjectName("statusbar")
        CompetitorWindow.setStatusBar(self.statusbar)
        self.LogoutAction = QtWidgets.QAction(CompetitorWindow)
        self.LogoutAction.setObjectName("LogoutAction")
        self.menu.addAction(self.LogoutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(CompetitorWindow)
        QtCore.QMetaObject.connectSlotsByName(CompetitorWindow)

    def retranslateUi(self, CompetitorWindow):
        _translate = QtCore.QCoreApplication.translate
        CompetitorWindow.setWindowTitle(_translate("CompetitorWindow", "MainWindow"))
        self.ProfileButton.setText(_translate("CompetitorWindow", "Мой профиль"))
        self.CompetitionButton.setText(_translate("CompetitorWindow", "Моя компетенция"))
        self.ResultsButton.setText(_translate("CompetitorWindow", "Мои результаты"))
        self.MenuLabel.setText(_translate("CompetitorWindow", "Меню участника"))
        self.GreetLabel.setText(_translate("CompetitorWindow", "Доброе утро,"))
        self.NameLabel.setText(_translate("CompetitorWindow", "Имя"))
        self.menu.setTitle(_translate("CompetitorWindow", "Профиль"))
        self.LogoutAction.setText(_translate("CompetitorWindow", "Выйти"))

