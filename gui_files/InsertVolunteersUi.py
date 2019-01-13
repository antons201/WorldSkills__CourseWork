# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertVolunteersUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InsertVolunteers(object):
    def setupUi(self, InsertVolunteers):
        InsertVolunteers.setObjectName("InsertVolunteers")
        InsertVolunteers.resize(413, 250)
        self.NameLabel = QtWidgets.QLabel(InsertVolunteers)
        self.NameLabel.setGeometry(QtCore.QRect(90, 70, 55, 16))
        self.NameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NameLabel.setObjectName("NameLabel")
        self.SexLabel = QtWidgets.QLabel(InsertVolunteers)
        self.SexLabel.setGeometry(QtCore.QRect(90, 100, 55, 16))
        self.SexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SexLabel.setObjectName("SexLabel")
        self.RegionLabel = QtWidgets.QLabel(InsertVolunteers)
        self.RegionLabel.setGeometry(QtCore.QRect(90, 130, 55, 16))
        self.RegionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RegionLabel.setObjectName("RegionLabel")
        self.CompetitionLabel = QtWidgets.QLabel(InsertVolunteers)
        self.CompetitionLabel.setGeometry(QtCore.QRect(64, 160, 81, 16))
        self.CompetitionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CompetitionLabel.setObjectName("CompetitionLabel")
        self.NameEdit = QtWidgets.QLineEdit(InsertVolunteers)
        self.NameEdit.setGeometry(QtCore.QRect(160, 60, 113, 22))
        self.NameEdit.setObjectName("NameEdit")
        self.MaleRadioButton = QtWidgets.QRadioButton(InsertVolunteers)
        self.MaleRadioButton.setGeometry(QtCore.QRect(160, 100, 95, 20))
        self.MaleRadioButton.setObjectName("MaleRadioButton")
        self.FemaleRadioButton = QtWidgets.QRadioButton(InsertVolunteers)
        self.FemaleRadioButton.setGeometry(QtCore.QRect(250, 100, 95, 20))
        self.FemaleRadioButton.setObjectName("FemaleRadioButton")
        self.RegionEdit = QtWidgets.QLineEdit(InsertVolunteers)
        self.RegionEdit.setGeometry(QtCore.QRect(160, 130, 113, 22))
        self.RegionEdit.setObjectName("RegionEdit")
        self.CompetitionComboBox = QtWidgets.QComboBox(InsertVolunteers)
        self.CompetitionComboBox.setGeometry(QtCore.QRect(160, 160, 73, 22))
        self.CompetitionComboBox.setObjectName("CompetitionComboBox")
        self.InsertLabel = QtWidgets.QLabel(InsertVolunteers)
        self.InsertLabel.setGeometry(QtCore.QRect(110, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InsertLabel.setFont(font)
        self.InsertLabel.setObjectName("InsertLabel")
        self.InsertButton = QtWidgets.QPushButton(InsertVolunteers)
        self.InsertButton.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.InsertButton.setObjectName("InsertButton")

        self.retranslateUi(InsertVolunteers)
        QtCore.QMetaObject.connectSlotsByName(InsertVolunteers)

    def retranslateUi(self, InsertVolunteers):
        _translate = QtCore.QCoreApplication.translate
        InsertVolunteers.setWindowTitle(_translate("InsertVolunteers", "Dialog"))
        self.NameLabel.setText(_translate("InsertVolunteers", "Имя"))
        self.SexLabel.setText(_translate("InsertVolunteers", "Пол"))
        self.RegionLabel.setText(_translate("InsertVolunteers", "Регион"))
        self.CompetitionLabel.setText(_translate("InsertVolunteers", "Компетенция"))
        self.MaleRadioButton.setText(_translate("InsertVolunteers", "Мужской"))
        self.FemaleRadioButton.setText(_translate("InsertVolunteers", "Женский"))
        self.InsertLabel.setText(_translate("InsertVolunteers", "Добавление волонтеров"))
        self.InsertButton.setText(_translate("InsertVolunteers", "Добавить"))

