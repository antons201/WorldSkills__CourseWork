# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CoordinatorWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CoordinatorWindow(object):
    def setupUi(self, CoordinatorWindow):
        CoordinatorWindow.setObjectName("CoordinatorWindow")
        CoordinatorWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CoordinatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.GreetLabel = QtWidgets.QLabel(self.MainFrame)
        self.GreetLabel.setGeometry(QtCore.QRect(280, 50, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setObjectName("GreetLabel")
        self.NameLabel = QtWidgets.QLabel(self.MainFrame)
        self.NameLabel.setGeometry(QtCore.QRect(390, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(270, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.ManagingVolunteersButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingVolunteersButton.setGeometry(QtCore.QRect(270, 90, 191, 81))
        self.ManagingVolunteersButton.setObjectName("ManagingVolunteersButton")
        self.ManagingSponsorsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingSponsorsButton.setGeometry(QtCore.QRect(270, 200, 191, 91))
        self.ManagingSponsorsButton.setObjectName("ManagingSponsorsButton")
        self.ResultsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ResultsButton.setGeometry(QtCore.QRect(270, 320, 191, 81))
        self.ResultsButton.setObjectName("ResultsButton")
        CoordinatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CoordinatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        CoordinatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CoordinatorWindow)
        self.statusbar.setObjectName("statusbar")
        CoordinatorWindow.setStatusBar(self.statusbar)
        self.LogoutAction = QtWidgets.QAction(CoordinatorWindow)
        self.LogoutAction.setObjectName("LogoutAction")
        self.menu.addAction(self.LogoutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(CoordinatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CoordinatorWindow)

    def retranslateUi(self, CoordinatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CoordinatorWindow.setWindowTitle(_translate("CoordinatorWindow", "MainWindow"))
        self.GreetLabel.setText(_translate("CoordinatorWindow", "Доброе утро,"))
        self.NameLabel.setText(_translate("CoordinatorWindow", "Имя"))
        self.MenuLabel.setText(_translate("CoordinatorWindow", "Меню координатора"))
        self.ManagingVolunteersButton.setText(_translate("CoordinatorWindow", "Управление волонтерами"))
        self.ManagingSponsorsButton.setText(_translate("CoordinatorWindow", "Управление спонсорами"))
        self.ResultsButton.setText(_translate("CoordinatorWindow", "Мои результаты"))
        self.menu.setTitle(_translate("CoordinatorWindow", "Профиль"))
        self.LogoutAction.setText(_translate("CoordinatorWindow", "Выйти"))

