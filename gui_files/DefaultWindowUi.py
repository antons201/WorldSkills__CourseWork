# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DefaultWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DefaultWindow(object):
    def setupUi(self, DefaultWindow):
        DefaultWindow.setObjectName("DefaultWindow")
        DefaultWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DefaultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.WorldSkillsLabel = QtWidgets.QLabel(self.MainFrame)
        self.WorldSkillsLabel.setGeometry(QtCore.QRect(260, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WorldSkillsLabel.setFont(font)
        self.WorldSkillsLabel.setObjectName("WorldSkillsLabel")
        self.WorldSkillsButton = QtWidgets.QPushButton(self.MainFrame)
        self.WorldSkillsButton.setGeometry(QtCore.QRect(260, 80, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WorldSkillsButton.setFont(font)
        self.WorldSkillsButton.setObjectName("WorldSkillsButton")
        self.WorldSkillsRussiaButton = QtWidgets.QPushButton(self.MainFrame)
        self.WorldSkillsRussiaButton.setGeometry(QtCore.QRect(260, 190, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WorldSkillsRussiaButton.setFont(font)
        self.WorldSkillsRussiaButton.setObjectName("WorldSkillsRussiaButton")
        self.TerritoryButton = QtWidgets.QPushButton(self.MainFrame)
        self.TerritoryButton.setGeometry(QtCore.QRect(260, 300, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TerritoryButton.setFont(font)
        self.TerritoryButton.setObjectName("TerritoryButton")
        DefaultWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DefaultWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        DefaultWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DefaultWindow)
        self.statusbar.setObjectName("statusbar")
        DefaultWindow.setStatusBar(self.statusbar)
        self.LoginAction = QtWidgets.QAction(DefaultWindow)
        self.LoginAction.setObjectName("LoginAction")
        self.menu.addAction(self.LoginAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(DefaultWindow)
        QtCore.QMetaObject.connectSlotsByName(DefaultWindow)

    def retranslateUi(self, DefaultWindow):
        _translate = QtCore.QCoreApplication.translate
        DefaultWindow.setWindowTitle(_translate("DefaultWindow", "MainWindow"))
        self.WorldSkillsLabel.setText(_translate("DefaultWindow", "WorldSkills Russia 2019"))
        self.WorldSkillsButton.setText(_translate("DefaultWindow", "О WorldSkills"))
        self.WorldSkillsRussiaButton.setText(_translate("DefaultWindow", "О WorldSkills Russia"))
        self.TerritoryButton.setText(_translate("DefaultWindow", "О Приморском крае"))
        self.menu.setTitle(_translate("DefaultWindow", "Профиль"))
        self.LoginAction.setText(_translate("DefaultWindow", "Войти"))

