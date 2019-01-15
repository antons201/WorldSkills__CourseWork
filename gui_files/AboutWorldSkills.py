# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWorldSkills.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWorldSkills(object):
    def setupUi(self, AboutWorldSkills):
        AboutWorldSkills.setObjectName("AboutWorldSkills")
        AboutWorldSkills.resize(795, 599)
        self.centralwidget = QtWidgets.QWidget(AboutWorldSkills)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.WorldSkillsLabel = QtWidgets.QLabel(self.MainFrame)
        self.WorldSkillsLabel.setGeometry(QtCore.QRect(280, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WorldSkillsLabel.setFont(font)
        self.WorldSkillsLabel.setObjectName("WorldSkillsLabel")
        self.HistoryButton = QtWidgets.QPushButton(self.MainFrame)
        self.HistoryButton.setGeometry(QtCore.QRect(260, 80, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.HistoryButton.setFont(font)
        self.HistoryButton.setObjectName("HistoryButton")
        self.CompetitionButton = QtWidgets.QPushButton(self.MainFrame)
        self.CompetitionButton.setGeometry(QtCore.QRect(260, 190, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CompetitionButton.setFont(font)
        self.CompetitionButton.setObjectName("CompetitionButton")
        self.ChempionshipsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ChempionshipsButton.setGeometry(QtCore.QRect(260, 300, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ChempionshipsButton.setFont(font)
        self.ChempionshipsButton.setObjectName("ChempionshipsButton")
        self.AboutFrame = QtWidgets.QFrame(self.centralwidget)
        self.AboutFrame.setGeometry(QtCore.QRect(19, 9, 761, 531))
        self.AboutFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AboutFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AboutFrame.setObjectName("AboutFrame")
        self.AboutWSTextEdit = QtWidgets.QTextEdit(self.AboutFrame)
        self.AboutWSTextEdit.setGeometry(QtCore.QRect(10, 30, 741, 491))
        self.AboutWSTextEdit.setObjectName("AboutWSTextEdit")
        self.ABackButton = QtWidgets.QPushButton(self.AboutFrame)
        self.ABackButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.ABackButton.setObjectName("ABackButton")
        self.CompetitionFrame = QtWidgets.QFrame(self.centralwidget)
        self.CompetitionFrame.setGeometry(QtCore.QRect(19, 9, 761, 531))
        self.CompetitionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CompetitionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CompetitionFrame.setObjectName("CompetitionFrame")
        self.CompetitionList = QtWidgets.QListWidget(self.CompetitionFrame)
        self.CompetitionList.setGeometry(QtCore.QRect(0, 60, 256, 471))
        self.CompetitionList.setObjectName("CompetitionList")
        self.AboutTextEdit = QtWidgets.QTextEdit(self.CompetitionFrame)
        self.AboutTextEdit.setGeometry(QtCore.QRect(360, 60, 401, 471))
        self.AboutTextEdit.setObjectName("AboutTextEdit")
        self.CompetitionLabel = QtWidgets.QLabel(self.CompetitionFrame)
        self.CompetitionLabel.setGeometry(QtCore.QRect(0, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CompetitionLabel.setFont(font)
        self.CompetitionLabel.setObjectName("CompetitionLabel")
        self.AboutLabel = QtWidgets.QLabel(self.CompetitionFrame)
        self.AboutLabel.setGeometry(QtCore.QRect(360, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutLabel.setFont(font)
        self.AboutLabel.setObjectName("AboutLabel")
        self.SearchButton = QtWidgets.QPushButton(self.CompetitionFrame)
        self.SearchButton.setGeometry(QtCore.QRect(260, 240, 91, 51))
        self.SearchButton.setObjectName("SearchButton")
        self.CoBackButton = QtWidgets.QPushButton(self.CompetitionFrame)
        self.CoBackButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.CoBackButton.setObjectName("CoBackButton")
        self.ChempionshipsFrame = QtWidgets.QFrame(self.centralwidget)
        self.ChempionshipsFrame.setGeometry(QtCore.QRect(19, 9, 761, 531))
        self.ChempionshipsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ChempionshipsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ChempionshipsFrame.setObjectName("ChempionshipsFrame")
        self.ChampionshipsWSILabel = QtWidgets.QLabel(self.ChempionshipsFrame)
        self.ChampionshipsWSILabel.setGeometry(QtCore.QRect(220, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ChampionshipsWSILabel.setFont(font)
        self.ChampionshipsWSILabel.setObjectName("ChampionshipsWSILabel")
        self.ChampionshipsTable = QtWidgets.QTableWidget(self.ChempionshipsFrame)
        self.ChampionshipsTable.setGeometry(QtCore.QRect(0, 110, 761, 421))
        self.ChampionshipsTable.setObjectName("ChampionshipsTable")
        self.ChampionshipsTable.setColumnCount(0)
        self.ChampionshipsTable.setRowCount(0)
        self.ChBackButton = QtWidgets.QPushButton(self.ChempionshipsFrame)
        self.ChBackButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.ChBackButton.setObjectName("ChBackButton")
        self.ChempionshipsFrame.raise_()
        self.MainFrame.raise_()
        self.AboutFrame.raise_()
        self.CompetitionFrame.raise_()
        AboutWorldSkills.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutWorldSkills)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 26))
        self.menubar.setObjectName("menubar")
        AboutWorldSkills.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutWorldSkills)
        self.statusbar.setObjectName("statusbar")
        AboutWorldSkills.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWorldSkills)
        QtCore.QMetaObject.connectSlotsByName(AboutWorldSkills)

    def retranslateUi(self, AboutWorldSkills):
        _translate = QtCore.QCoreApplication.translate
        AboutWorldSkills.setWindowTitle(_translate("AboutWorldSkills", "MainWindow"))
        self.WorldSkillsLabel.setText(_translate("AboutWorldSkills", "O WorldSkills"))
        self.HistoryButton.setText(_translate("AboutWorldSkills", "История"))
        self.CompetitionButton.setText(_translate("AboutWorldSkills", "Компетенции"))
        self.ChempionshipsButton.setText(_translate("AboutWorldSkills", "Чемпионаты"))
        self.AboutWSTextEdit.setHtml(_translate("AboutWorldSkills", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Первый национальный чемпионат:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Весной 2013 года в Тольятти состоялся Первый всероссийский конкурс профессионального мастерства «Национальный чемпионат WorldSkills Russia — 2013». В чемпионате приняли участие более трёхсот участников в возрасте от 18 до 22 лет — студентов учреждений среднего профессионального образования, победителей региональных конкурсов.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">По результатам Национального чемпионата была сформирована сборная Российской Федерации, которая в июле 2013 года приняла участие в чемпионате мира WorldSkills International в Лейпциге (Германия).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Основатель:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Albert Vidal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;Fill youth with enthusiasm through special action! Convince young people\'s parents, trainers and company chiefs that a promising future is possible only through good vocational training&quot;.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Francisco Albert-Vidal, IVTO President 1984-1992</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It was his nephew, Juan Martinez Albert, and his friend, Jose Rubio, who asked for this nomination two years ago. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Francisco Albert-Vidal was born in Pinoso in 1917 and worked in the city hall of the village of Petrer. Later, he was the Vocational Training General Secretary until 1977 as well as the founder of the International VET Competitions, now WorldSkills.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">He died in Madrid, in 1993, and was buried in the village of Pinoso.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">On 31 March 2015, the plenary session of the city hall of Pinoso approved, unanimously, his appointment as honorary citizen of the village, as recognition of his work in the field of vocational training for young people through the creation of important events like WorldSkills Competitions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Words from Pepe Rubio (partner and friend): &quot;Thanks for this recognition. Francisco Albert Vidal worked for universal values, for people and their education&quot; </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Words from Juan Martinez (nephew): &quot;I\'m very excited, and I remember many family moments with him, especially together with my mother, the only sister of Francisco who is still alive. I want to transmit gratitude from my whole family.”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Президент:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Simon Bartley</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(United Kingdom)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simon was elected President of WorldSkills International at the organization’s General Assembly in October 2010 and took up his four-year post on 10th October 2011, the day after the Closing Ceremony at WorldSkills London 2011. Previously Simon had been Chief Executive of UK Skills and WorldSkills London 2011 as well as being the UK’s Official Delegate to both WorldSkills International and WorldSkills Europe (on both of which he was also a Board Member). Prior to his involvement in UK Skills Simon worked in the Building Services Sector as Chairman of his family business and he now works as an international skills consultant. Simon was educated at Durham University, from where he graduated with a BSc in Engineering Science and Management and an MSc in Management Science. He is a Chartered Engineer, a Member of the Institution of Civil Engineers and a Fellow of City and Guilds. A Member of the UK Governments Skills Commission he is also on the Council of City &amp; Guilds. Simon is a past Chair of the Confederation of British Industry’s Small and Medium Sized Enterprise Council.</p></body></html>"))
        self.ABackButton.setText(_translate("AboutWorldSkills", "Назад"))
        self.CompetitionLabel.setText(_translate("AboutWorldSkills", "Компетенции"))
        self.AboutLabel.setText(_translate("AboutWorldSkills", "Описание"))
        self.SearchButton.setText(_translate("AboutWorldSkills", "Показать\n"
" описание"))
        self.CoBackButton.setText(_translate("AboutWorldSkills", "Назад"))
        self.ChampionshipsWSILabel.setText(_translate("AboutWorldSkills", "Чемпионаты WSI"))
        self.ChBackButton.setText(_translate("AboutWorldSkills", "Назад"))

