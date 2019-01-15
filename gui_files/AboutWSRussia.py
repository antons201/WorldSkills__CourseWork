# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWSRussia.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWSRussia(object):
    def setupUi(self, AboutWSRussia):
        AboutWSRussia.setObjectName("AboutWSRussia")
        AboutWSRussia.resize(693, 536)
        self.centralwidget = QtWidgets.QWidget(AboutWSRussia)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 220, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 220, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 250, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.BackButton.setObjectName("BackButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        AboutWSRussia.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutWSRussia)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 26))
        self.menubar.setObjectName("menubar")
        AboutWSRussia.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutWSRussia)
        self.statusbar.setObjectName("statusbar")
        AboutWSRussia.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWSRussia)
        QtCore.QMetaObject.connectSlotsByName(AboutWSRussia)

    def retranslateUi(self, AboutWSRussia):
        _translate = QtCore.QCoreApplication.translate
        AboutWSRussia.setWindowTitle(_translate("AboutWSRussia", "MainWindow"))
        self.label.setText(_translate("AboutWSRussia", "Присоединиться к движению:"))
        self.label_3.setText(_translate("AboutWSRussia", "Союз WorldSkills Россия:"))
        self.label_4.setText(_translate("AboutWSRussia", "<a href = \"https://yadi.sk/i/19hVyJyEQRJ8cA\"> ссылка на файл </a>"))
        self.label_5.setText(_translate("AboutWSRussia", "Партнёры и спонсоры:"))
        self.label_6.setText(_translate("AboutWSRussia", "<a href = \"https://worldskills.ru/partneryi-i-sponsoryi.html\"> перейти на сайт </a>"))
        self.BackButton.setText(_translate("AboutWSRussia", "Назад"))
        self.label_2.setText(_translate("AboutWSRussia", "<a href = \"https://worldskills.ru/\"> worldskills.ru</a>"))

