# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 521))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(260, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.GreetLabel = QtWidgets.QLabel(self.MainFrame)
        self.GreetLabel.setGeometry(QtCore.QRect(280, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setObjectName("GreetLabel")
        self.NameLabel = QtWidgets.QLabel(self.MainFrame)
        self.NameLabel.setGeometry(QtCore.QRect(390, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.ManagingChampionshipsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingChampionshipsButton.setGeometry(QtCore.QRect(250, 110, 221, 101))
        self.ManagingChampionshipsButton.setObjectName("ManagingChampionshipsButton")
        self.ManagingCompetitorsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingCompetitorsButton.setGeometry(QtCore.QRect(250, 250, 221, 101))
        self.ManagingCompetitorsButton.setObjectName("ManagingCompetitorsButton")
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)
        self.LogoutAction = QtWidgets.QAction(AdminWindow)
        self.LogoutAction.setObjectName("LogoutAction")
        self.menu.addAction(self.LogoutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.MenuLabel.setText(_translate("AdminWindow", "Меню администратора"))
        self.GreetLabel.setText(_translate("AdminWindow", "Доброе утро,"))
        self.NameLabel.setText(_translate("AdminWindow", "Имя"))
        self.ManagingChampionshipsButton.setText(_translate("AdminWindow", "Управление чемпионатами"))
        self.ManagingCompetitorsButton.setText(_translate("AdminWindow", "Управление участниками"))
        self.menu.setTitle(_translate("AdminWindow", "Профиль"))
        self.LogoutAction.setText(_translate("AdminWindow", "Выйти"))

