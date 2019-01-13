# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExpertWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExpertWindow(object):
    def setupUi(self, ExpertWindow):
        ExpertWindow.setObjectName("ExpertWindow")
        ExpertWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ExpertWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(300, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.GreetLabel = QtWidgets.QLabel(self.MainFrame)
        self.GreetLabel.setGeometry(QtCore.QRect(300, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setObjectName("GreetLabel")
        self.NameLabel = QtWidgets.QLabel(self.MainFrame)
        self.NameLabel.setGeometry(QtCore.QRect(410, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.DrawButton = QtWidgets.QPushButton(self.MainFrame)
        self.DrawButton.setGeometry(QtCore.QRect(270, 90, 191, 81))
        self.DrawButton.setObjectName("DrawButton")
        self.ResultsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ResultsButton.setGeometry(QtCore.QRect(270, 290, 191, 81))
        self.ResultsButton.setObjectName("ResultsButton")
        self.EnterRatingsButton = QtWidgets.QPushButton(self.MainFrame)
        self.EnterRatingsButton.setGeometry(QtCore.QRect(270, 190, 191, 81))
        self.EnterRatingsButton.setObjectName("EnterRatingsButton")
        ExpertWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExpertWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        ExpertWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExpertWindow)
        self.statusbar.setObjectName("statusbar")
        ExpertWindow.setStatusBar(self.statusbar)
        self.LogoutAction = QtWidgets.QAction(ExpertWindow)
        self.LogoutAction.setObjectName("LogoutAction")
        self.menu.addAction(self.LogoutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(ExpertWindow)
        QtCore.QMetaObject.connectSlotsByName(ExpertWindow)

    def retranslateUi(self, ExpertWindow):
        _translate = QtCore.QCoreApplication.translate
        ExpertWindow.setWindowTitle(_translate("ExpertWindow", "MainWindow"))
        self.MenuLabel.setText(_translate("ExpertWindow", "Меню эксперта"))
        self.GreetLabel.setText(_translate("ExpertWindow", "Доброе утро,"))
        self.NameLabel.setText(_translate("ExpertWindow", "Имя"))
        self.DrawButton.setText(_translate("ExpertWindow", "Жеребьевка"))
        self.ResultsButton.setText(_translate("ExpertWindow", "Просмотр результатов"))
        self.EnterRatingsButton.setText(_translate("ExpertWindow", "Ввод оценок"))
        self.menu.setTitle(_translate("ExpertWindow", "Профиль"))
        self.LogoutAction.setText(_translate("ExpertWindow", "Выйти"))

