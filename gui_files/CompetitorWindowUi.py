# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompetitorWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CompetitorWindow(object):
    def setupUi(self, CompetitorWindow):
        CompetitorWindow.setObjectName("CompetitorWindow")
        CompetitorWindow.resize(737, 514)
        self.centralwidget = QtWidgets.QWidget(CompetitorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.ProfileButton = QtWidgets.QPushButton(self.MainFrame)
        self.ProfileButton.setGeometry(QtCore.QRect(270, 100, 201, 71))
        self.ProfileButton.setObjectName("ProfileButton")
        self.CompetitionButton = QtWidgets.QPushButton(self.MainFrame)
        self.CompetitionButton.setGeometry(QtCore.QRect(270, 190, 201, 71))
        self.CompetitionButton.setObjectName("CompetitionButton")
        self.ResultsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ResultsButton.setGeometry(QtCore.QRect(270, 280, 201, 81))
        self.ResultsButton.setObjectName("ResultsButton")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(270, 0, 211, 41))
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
        self.ResultsFrame = QtWidgets.QFrame(self.centralwidget)
        self.ResultsFrame.setGeometry(QtCore.QRect(19, 9, 711, 481))
        self.ResultsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ResultsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ResultsFrame.setObjectName("ResultsFrame")
        self.InfoNameLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoNameLabel.setGeometry(QtCore.QRect(250, 160, 55, 16))
        self.InfoNameLabel.setText("")
        self.InfoNameLabel.setObjectName("InfoNameLabel")
        self.SexLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.SexLabel.setGeometry(QtCore.QRect(170, 190, 55, 16))
        self.SexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SexLabel.setObjectName("SexLabel")
        self.InfoCompetenceLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoCompetenceLabel.setGeometry(QtCore.QRect(490, 180, 71, 20))
        self.InfoCompetenceLabel.setText("")
        self.InfoCompetenceLabel.setObjectName("InfoCompetenceLabel")
        self.InfoSexLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoSexLabel.setGeometry(QtCore.QRect(250, 190, 55, 16))
        self.InfoSexLabel.setText("")
        self.InfoSexLabel.setObjectName("InfoSexLabel")
        self.RegionLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.RegionLabel.setGeometry(QtCore.QRect(170, 250, 55, 16))
        self.RegionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RegionLabel.setObjectName("RegionLabel")
        self.InfoRegionLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoRegionLabel.setGeometry(QtCore.QRect(250, 250, 55, 16))
        self.InfoRegionLabel.setText("")
        self.InfoRegionLabel.setObjectName("InfoRegionLabel")
        self.InfoChempionshipLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoChempionshipLabel.setGeometry(QtCore.QRect(490, 146, 71, 20))
        self.InfoChempionshipLabel.setText("")
        self.InfoChempionshipLabel.setObjectName("InfoChempionshipLabel")
        self.NameLabel_2 = QtWidgets.QLabel(self.ResultsFrame)
        self.NameLabel_2.setGeometry(QtCore.QRect(170, 160, 55, 16))
        self.NameLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NameLabel_2.setObjectName("NameLabel_2")
        self.NumUserLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.NumUserLabel.setGeometry(QtCore.QRect(380, 210, 101, 20))
        self.NumUserLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NumUserLabel.setObjectName("NumUserLabel")
        self.ModulsTable = QtWidgets.QTableWidget(self.ResultsFrame)
        self.ModulsTable.setGeometry(QtCore.QRect(390, 240, 191, 81))
        self.ModulsTable.setObjectName("ModulsTable")
        self.ModulsTable.setColumnCount(0)
        self.ModulsTable.setRowCount(0)
        self.ChempionshipLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.ChempionshipLabel.setGeometry(QtCore.QRect(410, 146, 71, 20))
        self.ChempionshipLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChempionshipLabel.setObjectName("ChempionshipLabel")
        self.CompetenceLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.CompetenceLabel.setGeometry(QtCore.QRect(400, 180, 81, 20))
        self.CompetenceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CompetenceLabel.setObjectName("CompetenceLabel")
        self.SumLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.SumLabel.setGeometry(QtCore.QRect(530, 330, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SumLabel.setFont(font)
        self.SumLabel.setText("")
        self.SumLabel.setObjectName("SumLabel")
        self.ResultsLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.ResultsLabel.setGeometry(QtCore.QRect(240, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ResultsLabel.setFont(font)
        self.ResultsLabel.setObjectName("ResultsLabel")
        self.IdLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.IdLabel.setGeometry(QtCore.QRect(170, 220, 55, 16))
        self.IdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IdLabel.setObjectName("IdLabel")
        self.InfoNumUserLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoNumUserLabel.setGeometry(QtCore.QRect(490, 210, 71, 20))
        self.InfoNumUserLabel.setText("")
        self.InfoNumUserLabel.setObjectName("InfoNumUserLabel")
        self.DistrictLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.DistrictLabel.setGeometry(QtCore.QRect(170, 280, 55, 16))
        self.DistrictLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DistrictLabel.setObjectName("DistrictLabel")
        self.InfoDistrictLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoDistrictLabel.setGeometry(QtCore.QRect(250, 280, 55, 16))
        self.InfoDistrictLabel.setText("")
        self.InfoDistrictLabel.setObjectName("InfoDistrictLabel")
        self.InfoIdLabel = QtWidgets.QLabel(self.ResultsFrame)
        self.InfoIdLabel.setGeometry(QtCore.QRect(250, 220, 55, 16))
        self.InfoIdLabel.setText("")
        self.InfoIdLabel.setObjectName("InfoIdLabel")
        self.MyProfileFrame = QtWidgets.QFrame(self.centralwidget)
        self.MyProfileFrame.setGeometry(QtCore.QRect(19, 9, 711, 481))
        self.MyProfileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MyProfileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MyProfileFrame.setObjectName("MyProfileFrame")
        self.InfoSexLabel_2 = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoSexLabel_2.setGeometry(QtCore.QRect(220, 170, 55, 16))
        self.InfoSexLabel_2.setText("")
        self.InfoSexLabel_2.setObjectName("InfoSexLabel_2")
        self.ErrorLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.ErrorLabel.setGeometry(QtCore.QRect(424, 300, 141, 20))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.SaveButton = QtWidgets.QPushButton(self.MyProfileFrame)
        self.SaveButton.setGeometry(QtCore.QRect(420, 330, 71, 28))
        self.SaveButton.setObjectName("SaveButton")
        self.EmailLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.EmailLabel.setGeometry(QtCore.QRect(150, 320, 55, 16))
        self.EmailLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.IdLabel_2 = QtWidgets.QLabel(self.MyProfileFrame)
        self.IdLabel_2.setGeometry(QtCore.QRect(150, 230, 55, 16))
        self.IdLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IdLabel_2.setObjectName("IdLabel_2")
        self.PhoneLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.PhoneLabel.setGeometry(QtCore.QRect(150, 290, 55, 16))
        self.PhoneLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.BirthLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.BirthLabel.setGeometry(QtCore.QRect(114, 200, 91, 20))
        self.BirthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BirthLabel.setObjectName("BirthLabel")
        self.PasswordCheckBox = QtWidgets.QCheckBox(self.MyProfileFrame)
        self.PasswordCheckBox.setGeometry(QtCore.QRect(420, 280, 121, 20))
        self.PasswordCheckBox.setObjectName("PasswordCheckBox")
        self.ExitButton = QtWidgets.QPushButton(self.MyProfileFrame)
        self.ExitButton.setGeometry(QtCore.QRect(500, 330, 71, 28))
        self.ExitButton.setObjectName("ExitButton")
        self.RepeatPasswordLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.RepeatPasswordLabel.setGeometry(QtCore.QRect(420, 220, 161, 20))
        self.RepeatPasswordLabel.setObjectName("RepeatPasswordLabel")
        self.InfoPhoneLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoPhoneLabel.setGeometry(QtCore.QRect(220, 290, 55, 16))
        self.InfoPhoneLabel.setText("")
        self.InfoPhoneLabel.setObjectName("InfoPhoneLabel")
        self.InfoCountryLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoCountryLabel.setGeometry(QtCore.QRect(220, 260, 55, 16))
        self.InfoCountryLabel.setText("")
        self.InfoCountryLabel.setObjectName("InfoCountryLabel")
        self.NewPasswordLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.NewPasswordLabel.setGeometry(QtCore.QRect(440, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewPasswordLabel.setFont(font)
        self.NewPasswordLabel.setObjectName("NewPasswordLabel")
        self.EnterPasswordLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.EnterPasswordLabel.setGeometry(QtCore.QRect(420, 160, 141, 20))
        self.EnterPasswordLabel.setObjectName("EnterPasswordLabel")
        self.NewPasswordEdit = QtWidgets.QLineEdit(self.MyProfileFrame)
        self.NewPasswordEdit.setGeometry(QtCore.QRect(420, 190, 141, 22))
        self.NewPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPasswordEdit.setObjectName("NewPasswordEdit")
        self.InfoBirthLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoBirthLabel.setGeometry(QtCore.QRect(220, 200, 55, 16))
        self.InfoBirthLabel.setText("")
        self.InfoBirthLabel.setObjectName("InfoBirthLabel")
        self.RepeatNewPasswordEdit = QtWidgets.QLineEdit(self.MyProfileFrame)
        self.RepeatNewPasswordEdit.setGeometry(QtCore.QRect(420, 250, 141, 22))
        self.RepeatNewPasswordEdit.setText("")
        self.RepeatNewPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RepeatNewPasswordEdit.setObjectName("RepeatNewPasswordEdit")
        self.NameLabel_3 = QtWidgets.QLabel(self.MyProfileFrame)
        self.NameLabel_3.setGeometry(QtCore.QRect(150, 140, 55, 16))
        self.NameLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NameLabel_3.setObjectName("NameLabel_3")
        self.CountryLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.CountryLabel.setGeometry(QtCore.QRect(150, 260, 55, 16))
        self.CountryLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CountryLabel.setObjectName("CountryLabel")
        self.ProfileLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.ProfileLabel.setGeometry(QtCore.QRect(270, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProfileLabel.setFont(font)
        self.ProfileLabel.setObjectName("ProfileLabel")
        self.InfoEmailLabel = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoEmailLabel.setGeometry(QtCore.QRect(220, 320, 55, 16))
        self.InfoEmailLabel.setText("")
        self.InfoEmailLabel.setObjectName("InfoEmailLabel")
        self.InfoIdLabel_2 = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoIdLabel_2.setGeometry(QtCore.QRect(220, 230, 55, 16))
        self.InfoIdLabel_2.setText("")
        self.InfoIdLabel_2.setObjectName("InfoIdLabel_2")
        self.InfoNameLabel_2 = QtWidgets.QLabel(self.MyProfileFrame)
        self.InfoNameLabel_2.setGeometry(QtCore.QRect(220, 140, 55, 16))
        self.InfoNameLabel_2.setText("")
        self.InfoNameLabel_2.setObjectName("InfoNameLabel_2")
        self.SexLabel_2 = QtWidgets.QLabel(self.MyProfileFrame)
        self.SexLabel_2.setGeometry(QtCore.QRect(150, 170, 55, 16))
        self.SexLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SexLabel_2.setObjectName("SexLabel_2")
        self.CompetitionFrame = QtWidgets.QFrame(self.centralwidget)
        self.CompetitionFrame.setGeometry(QtCore.QRect(19, 9, 711, 451))
        self.CompetitionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CompetitionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CompetitionFrame.setObjectName("CompetitionFrame")
        self.CompetenceLabel_2 = QtWidgets.QLabel(self.CompetitionFrame)
        self.CompetenceLabel_2.setGeometry(QtCore.QRect(240, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CompetenceLabel_2.setFont(font)
        self.CompetenceLabel_2.setObjectName("CompetenceLabel_2")
        self.NameCompetenceLabel = QtWidgets.QLabel(self.CompetitionFrame)
        self.NameCompetenceLabel.setGeometry(QtCore.QRect(340, 70, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NameCompetenceLabel.setFont(font)
        self.NameCompetenceLabel.setObjectName("NameCompetenceLabel")
        self.ExpertButton = QtWidgets.QPushButton(self.CompetitionFrame)
        self.ExpertButton.setGeometry(QtCore.QRect(200, 120, 101, 28))
        self.ExpertButton.setObjectName("ExpertButton")
        self.PlanButton_4 = QtWidgets.QPushButton(self.CompetitionFrame)
        self.PlanButton_4.setGeometry(QtCore.QRect(310, 120, 101, 28))
        self.PlanButton_4.setObjectName("PlanButton_4")
        self.PlanFrame = QtWidgets.QFrame(self.CompetitionFrame)
        self.PlanFrame.setGeometry(QtCore.QRect(100, 170, 531, 231))
        self.PlanFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlanFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlanFrame.setObjectName("PlanFrame")
        self.PictureLabel = QtWidgets.QLabel(self.PlanFrame)
        self.PictureLabel.setGeometry(QtCore.QRect(0, 0, 531, 231))
        self.PictureLabel.setText("")
        self.PictureLabel.setObjectName("PictureLabel")
        self.NumCompetenceLabel = QtWidgets.QLabel(self.CompetitionFrame)
        self.NumCompetenceLabel.setGeometry(QtCore.QRect(150, 70, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumCompetenceLabel.setFont(font)
        self.NumCompetenceLabel.setObjectName("NumCompetenceLabel")
        self.SheduleButton = QtWidgets.QPushButton(self.CompetitionFrame)
        self.SheduleButton.setGeometry(QtCore.QRect(540, 120, 101, 28))
        self.SheduleButton.setObjectName("SheduleButton")
        self.PeopleFrame = QtWidgets.QFrame(self.CompetitionFrame)
        self.PeopleFrame.setGeometry(QtCore.QRect(100, 170, 531, 231))
        self.PeopleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PeopleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PeopleFrame.setObjectName("PeopleFrame")
        self.InfoTable = QtWidgets.QTableWidget(self.PeopleFrame)
        self.InfoTable.setGeometry(QtCore.QRect(0, 0, 531, 231))
        self.InfoTable.setObjectName("InfoTable")
        self.InfoTable.setColumnCount(0)
        self.InfoTable.setRowCount(0)
        self.InfrastructureButton = QtWidgets.QPushButton(self.CompetitionFrame)
        self.InfrastructureButton.setGeometry(QtCore.QRect(420, 120, 111, 28))
        self.InfrastructureButton.setObjectName("InfrastructureButton")
        self.LinkFrame = QtWidgets.QFrame(self.CompetitionFrame)
        self.LinkFrame.setGeometry(QtCore.QRect(100, 170, 531, 221))
        self.LinkFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinkFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinkFrame.setObjectName("LinkFrame")
        self.LinkLabel = QtWidgets.QLabel(self.LinkFrame)
        self.LinkLabel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.LinkLabel.setObjectName("LinkLabel")
        self.InfoLinkLabel = QtWidgets.QLabel(self.LinkFrame)
        self.InfoLinkLabel.setGeometry(QtCore.QRect(120, 10, 55, 16))
        self.InfoLinkLabel.setText("")
        self.InfoLinkLabel.setObjectName("InfoLinkLabel")
        self.ParticipantButton = QtWidgets.QPushButton(self.CompetitionFrame)
        self.ParticipantButton.setGeometry(QtCore.QRect(90, 120, 101, 28))
        self.ParticipantButton.setObjectName("ParticipantButton")
        CompetitorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CompetitorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 26))
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
        self.SexLabel.setText(_translate("CompetitorWindow", "Пол"))
        self.RegionLabel.setText(_translate("CompetitorWindow", "Регион"))
        self.NameLabel_2.setText(_translate("CompetitorWindow", "Имя"))
        self.NumUserLabel.setText(_translate("CompetitorWindow", "Номер участника"))
        self.ChempionshipLabel.setText(_translate("CompetitorWindow", "Чемпионат"))
        self.CompetenceLabel.setText(_translate("CompetitorWindow", "Компетенция"))
        self.ResultsLabel.setText(_translate("CompetitorWindow", "Мои результаты"))
        self.IdLabel.setText(_translate("CompetitorWindow", "ID"))
        self.DistrictLabel.setText(_translate("CompetitorWindow", "Округ"))
        self.SaveButton.setText(_translate("CompetitorWindow", "Сохранить"))
        self.EmailLabel.setText(_translate("CompetitorWindow", "Email"))
        self.IdLabel_2.setText(_translate("CompetitorWindow", "ID"))
        self.PhoneLabel.setText(_translate("CompetitorWindow", "Телефон"))
        self.BirthLabel.setText(_translate("CompetitorWindow", "Дата рождения"))
        self.PasswordCheckBox.setText(_translate("CompetitorWindow", "Показать пароль"))
        self.ExitButton.setText(_translate("CompetitorWindow", "Выход"))
        self.RepeatPasswordLabel.setText(_translate("CompetitorWindow", "Повторите новый пароль:"))
        self.NewPasswordLabel.setText(_translate("CompetitorWindow", "Смена пароля"))
        self.EnterPasswordLabel.setText(_translate("CompetitorWindow", "Введите новый пароль:"))
        self.NameLabel_3.setText(_translate("CompetitorWindow", "Имя"))
        self.CountryLabel.setText(_translate("CompetitorWindow", "Страна"))
        self.ProfileLabel.setText(_translate("CompetitorWindow", "Мой профиль"))
        self.SexLabel_2.setText(_translate("CompetitorWindow", "Пол"))
        self.CompetenceLabel_2.setText(_translate("CompetitorWindow", "Моя компетенция"))
        self.NameCompetenceLabel.setText(_translate("CompetitorWindow", "- Название компетенции"))
        self.ExpertButton.setText(_translate("CompetitorWindow", "Эксперты"))
        self.PlanButton_4.setText(_translate("CompetitorWindow", "План застройки"))
        self.NumCompetenceLabel.setText(_translate("CompetitorWindow", "Номер компетенции"))
        self.SheduleButton.setText(_translate("CompetitorWindow", "Расписание"))
        self.InfrastructureButton.setText(_translate("CompetitorWindow", "Инфраструктура"))
        self.LinkLabel.setText(_translate("CompetitorWindow", "Ссылка на файл:"))
        self.ParticipantButton.setText(_translate("CompetitorWindow", "Участники"))
        self.menu.setTitle(_translate("CompetitorWindow", "Профиль"))
        self.LogoutAction.setText(_translate("CompetitorWindow", "Выйти"))

