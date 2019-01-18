# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlanWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlanWindow(object):
    def setupUi(self, PlanWindow):
        PlanWindow.setObjectName("PlanWindow")
        PlanWindow.resize(813, 741)
        self.centralwidget = QtWidgets.QWidget(PlanWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PicLabel = QtWidgets.QLabel(self.centralwidget)
        self.PicLabel.setGeometry(QtCore.QRect(0, 0, 781, 681))
        self.PicLabel.setText("")
        self.PicLabel.setObjectName("PicLabel")
        PlanWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlanWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 30))
        self.menubar.setObjectName("menubar")
        PlanWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlanWindow)
        self.statusbar.setObjectName("statusbar")
        PlanWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlanWindow)
        QtCore.QMetaObject.connectSlotsByName(PlanWindow)

    def retranslateUi(self, PlanWindow):
        _translate = QtCore.QCoreApplication.translate
        PlanWindow.setWindowTitle(_translate("PlanWindow", "MainWindow"))

