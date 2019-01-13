# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DistributeVolunteersUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DistributeVolunteers(object):
    def setupUi(self, DistributeVolunteers):
        DistributeVolunteers.setObjectName("DistributeVolunteers")
        DistributeVolunteers.resize(575, 289)
        self.DistributeLabel = QtWidgets.QLabel(DistributeVolunteers)
        self.DistributeLabel.setGeometry(QtCore.QRect(160, 20, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DistributeLabel.setFont(font)
        self.DistributeLabel.setObjectName("DistributeLabel")
        self.VolunteersTable = QtWidgets.QTableWidget(DistributeVolunteers)
        self.VolunteersTable.setGeometry(QtCore.QRect(20, 110, 301, 121))
        self.VolunteersTable.setObjectName("VolunteersTable")
        self.VolunteersTable.setColumnCount(0)
        self.VolunteersTable.setRowCount(0)
        self.CompetenceLabel = QtWidgets.QLabel(DistributeVolunteers)
        self.CompetenceLabel.setGeometry(QtCore.QRect(20, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CompetenceLabel.setFont(font)
        self.CompetenceLabel.setObjectName("CompetenceLabel")
        self.CompetenceComboBox = QtWidgets.QComboBox(DistributeVolunteers)
        self.CompetenceComboBox.setGeometry(QtCore.QRect(140, 50, 73, 22))
        self.CompetenceComboBox.setObjectName("CompetenceComboBox")
        self.SearchButton = QtWidgets.QPushButton(DistributeVolunteers)
        self.SearchButton.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.SearchButton.setObjectName("SearchButton")
        self.NewCompetenceLabel = QtWidgets.QLabel(DistributeVolunteers)
        self.NewCompetenceLabel.setGeometry(QtCore.QRect(330, 110, 181, 16))
        self.NewCompetenceLabel.setObjectName("NewCompetenceLabel")
        self.NewCompetenceComboBox = QtWidgets.QComboBox(DistributeVolunteers)
        self.NewCompetenceComboBox.setGeometry(QtCore.QRect(330, 140, 73, 22))
        self.NewCompetenceComboBox.setObjectName("NewCompetenceComboBox")
        self.DistributeButton = QtWidgets.QPushButton(DistributeVolunteers)
        self.DistributeButton.setGeometry(QtCore.QRect(330, 190, 93, 28))
        self.DistributeButton.setObjectName("DistributeButton")

        self.retranslateUi(DistributeVolunteers)
        QtCore.QMetaObject.connectSlotsByName(DistributeVolunteers)

    def retranslateUi(self, DistributeVolunteers):
        _translate = QtCore.QCoreApplication.translate
        DistributeVolunteers.setWindowTitle(_translate("DistributeVolunteers", "Dialog"))
        self.DistributeLabel.setText(_translate("DistributeVolunteers", "Распределение волонтеров"))
        self.CompetenceLabel.setText(_translate("DistributeVolunteers", "Компетенция"))
        self.SearchButton.setText(_translate("DistributeVolunteers", "Показать"))
        self.NewCompetenceLabel.setText(_translate("DistributeVolunteers", "Переместить в компетенцию:"))
        self.DistributeButton.setText(_translate("DistributeVolunteers", "Переместить"))

