from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from gui_files import AdminWindowUi, CompetitorWindowUi, CoordinatorWindowUi, DefaultWindowUi, ExpertWindowUi, \
    PlanWindowUi
from gui_files import AuthDialogUi, CompetitorProfileDialogUi
from gui_files import DistributeVolunteersUi, InsertVolunteersUi, InsertUsersUi
from gui_files import AboutRegion, AboutWorldSkills, AboutWSRussia

import os
import db
import datetime

t = '1.png'

open_windows = {}
head_comp_exp = ['ID', 'Имя', 'Пол', 'Дата рождения', 'Регион']
head_module = ['Модуль', 'Балл']
head_comp = ['ID', 'Имя', 'Пол', 'Логин', 'Пароль', 'Дата рождения', 'Регион', 'Email', 'Компетенция']
head_vol = ['ID', 'Имя', 'Регион', 'Пол']
head_chemp = ['ID', 'Название', 'Регион', 'Участники', 'Время проведения']


def time():
    a = datetime.datetime.time(datetime.datetime.now())
    if a.hour >= 6 and a.hour <= 11:
        return 'Доброе утро, '
    elif a.hour >= 12 and a.hour <= 17:
        return 'Добрый день, '
    else:
        return 'Добрый вечер, '


class DefaultWindow(QtWidgets.QMainWindow, DefaultWindowUi.Ui_DefaultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        open_windows[self.objectName()] = self
        self.AuthDialog = AuthDialog()
        self.init_buttons_actions()

    def init_buttons_actions(self):
        self.LoginAction.triggered.connect(self.show_AuthDialog)
        self.WorldSkillsButton.clicked.connect(self.open_worldskills_window)
        self.WorldSkillsRussiaButton.clicked.connect(self.open_worldskills_russia_window)
        self.TerritoryButton.clicked.connect(self.open_territory_window)

    def open_worldskills_window(self):
        self.ws = AboutWorldSkillsWindow()
        self.ws.show()

    def open_worldskills_russia_window(self):
        self.wsr = AboutWorldSkillsRussiaWindow()
        self.wsr.show()

    def open_territory_window(self):
        self.ter = AboutRegionWindow()
        self.ter.show()

    def show_AuthDialog(self):
        self.AuthDialog.show()


class AboutWorldSkillsWindow(QtWidgets.QMainWindow, AboutWorldSkills.Ui_AboutWorldSkills):
    def block_frame(self):
        self.AboutFrame.setHidden(True)
        self.CompetitionFrame.setHidden(True)
        self.ChempionshipsFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()

    def init_buttons_actions(self):
        self.HistoryButton.clicked.connect(self.history_click)
        self.CompetitionButton.clicked.connect(self.competition_click)
        self.ChempionshipsButton.clicked.connect(self.championships_click)
        self.ChBackButton.clicked.connect(self.back_click)
        self.CoBackButton.clicked.connect(self.back_click)
        self.ABackButton.clicked.connect(self.back_click)
        self.SearchButton.clicked.connect(self.search)

    def history_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.AboutFrame.setHidden(False)

    def competition_click(self):
        self.CompetitionList.clear()
        self.AboutTextEdit.clear()
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.CompetitionFrame.setHidden(False)
        all_competence = db.get_all_competences()
        for i in range(len(all_competence)):
            competence = all_competence[i]
            self.CompetitionList.addItem(competence)

    def championships_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.ChempionshipsFrame.setHidden(False)
        chempionships = db.get_all_championship()
        num_column = 0
        if (chempionships[0] != 0):
            num_column = len(chempionships[0])
        self.ChampionshipsTable.setRowCount(len(chempionships))
        self.ChampionshipsTable.setColumnCount(num_column)
        self.ChampionshipsTable.setHorizontalHeaderLabels(head_chemp)
        for i in range(len(chempionships)):
            for j in range(num_column):
                info = QTableWidgetItem(str(chempionships[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ChampionshipsTable.setItem(i, j, info)
        header = self.ChampionshipsTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(self.ChampionshipsTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def search(self):
        try:
            id = self.CompetitionList.selectionModel().selectedRows()
            for index in sorted(id):
                str_id = self.CompetitionList.item(index.row()).text()
            id_comp = str_id.split('. ')
            info = db.get_competence_info(id_comp[0])
            self.AboutTextEdit.setText(info[2])
        except BaseException as e:
            print(e)

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)


class AboutWorldSkillsRussiaWindow(QtWidgets.QMainWindow, AboutWSRussia.Ui_AboutWSRussia):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.label_2.setOpenExternalLinks(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_6.setOpenExternalLinks(True)


class AboutRegionWindow(QtWidgets.QMainWindow, AboutRegion.Ui_AboutRegion):
    def block_frame(self):
        self.HistoryFrame.setHidden(True)
        self.EventsFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()

    def init_buttons_actions(self):
        self.HistoryButton.clicked.connect(self.history_click)
        self.EventshButton.clicked.connect(self.events_click)

    def history_click(self):
        self.HistoryFrame.setHidden(False)
        self.EventsFrame.setHidden(True)

    def events_click(self):
        self.HistoryFrame.setHidden(True)
        self.EventsFrame.setHidden(False)
        header = self.EventsTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(self.EventsTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)


class AdminWindow(QtWidgets.QMainWindow, AdminWindowUi.Ui_AdminWindow):
    def block_frame(self):
        self.CompetitorFrame.setHidden(True)
        self.ManageChempionshipsFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()
        self.GreetLabel.setText(time() + db.user_data[1])
        self.GreetLabel.adjustSize()
        chempionship = db.get_current_championship().split('. ')
        self.NameChempionshipsLabel.setText(chempionship[1])
        self.NameChempionshipsLabel.adjustSize()

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
        self.ManagingChampionshipsButton.clicked.connect(self.managing_chempionships_click)
        self.ManagingCompetitorsButton.clicked.connect(self.managing_competitor_click)
        self.ExpertButton.clicked.connect(lambda: self.open_insert_window('expert'))
        self.CoordinatorButton.clicked.connect(lambda: self.open_insert_window('coordinate'))
        self.InsertButton.clicked.connect(lambda: self.open_insert_window('competitor'))
        self.CoBackButton.clicked.connect(self.back_click)
        self.ChBackButton.clicked.connect(self.back_click)
        self.SearchButton.clicked.connect(self.search_click)

    def managing_chempionships_click(self):
        self.ManageChempionshipsFrame.setHidden(False)
        self.MainFrame.setHidden(True)
        chempionships = db.get_all_championship()
        num_column = 0
        if (chempionships[0] != 0):
            num_column = len(chempionships[0])
        self.ChempionshipsTable.setRowCount(len(chempionships))
        self.ChempionshipsTable.setColumnCount(num_column)
        self.ChempionshipsTable.setHorizontalHeaderLabels(head_chemp)
        for i in range(len(chempionships)):
            for j in range(num_column):
                info = QTableWidgetItem(str(chempionships[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ChempionshipsTable.setItem(i, j, info)
        header = self.ChempionshipsTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.ChempionshipsTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def managing_competitor_click(self):
        self.CompetitorFrame.setHidden(False)
        self.MainFrame.setHidden(True)
        all_competence = db.get_all_competences()
        self.CompetitionComboBox.clear()
        for i in range(len(all_competence)):
            self.CompetitionComboBox.addItem(all_competence[i])
        self.CompetitionComboBox.adjustSize()
        data = db.get_all_competitors_experts(0, 0, 2)
        size_str = 0
        if len(data) != 0:
            size_str = len(data[0])
        self.CompetitorTable.setRowCount(len(data))
        self.CompetitorTable.setColumnCount(size_str)
        self.CompetitorTable.setHorizontalHeaderLabels(head_comp)
        for i in range(len(data)):
            for j in range(size_str):
                info = QTableWidgetItem(str(data[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.CompetitorTable.setItem(i, j, info)
        header = self.CompetitorTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.CompetitorTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def search_click(self):
        all_competence = db.get_all_competences()
        competence = all_competence[self.CompetitionComboBox.currentIndex()].split('. ')
        data = db.get_all_competitors_experts(competence[0], 0, 2)
        size_str = 0
        if len(data) != 0:
            size_str = len(data[0])
        self.CompetitorTable.setRowCount(len(data))
        self.CompetitorTable.setColumnCount(size_str)
        self.CompetitorTable.setHorizontalHeaderLabels(head_comp)
        for i in range(len(data)):
            for j in range(size_str):
                info = QTableWidgetItem(str(data[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.CompetitorTable.setItem(i, j, info)
        header = self.CompetitorTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.CompetitorTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def open_insert_window(self, status):
        self.insert = InsertUsers(status, self)
        self.insert.show()

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)

    def log_out(self):
        open_windows[self.objectName()].close()
        open_windows["DefaultWindow"].show()


class CompetitorWindow(QtWidgets.QMainWindow, CompetitorWindowUi.Ui_CompetitorWindow):
    def block_frame(self):
        self.MyProfileFrame.setHidden(True)
        self.CompetitionFrame.setHidden(True)
        self.ResultsFrame.setHidden(True)

    def block_competition_frame(self):
        self.LinkFrame.setHidden(True)
        self.PeopleFrame.setHidden(True)
        self.PlanFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()
        self.GreetLabel.setText(time() + db.user_data[1])
        self.GreetLabel.adjustSize()
        chempionship = db.get_current_championship().split('. ')
        self.NameChempionshipsLabel.setText(chempionship[1])
        self.NameChempionshipsLabel.adjustSize()
        self.InfoLinkLabel.setOpenExternalLinks(True)

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
        self.ProfileButton.clicked.connect(self.profile_click)
        self.CompetitionButton.clicked.connect(self.competition_click)
        self.ResultsButton.clicked.connect(self.results_click)
        self.RBackButton.clicked.connect(self.back_click)
        self.ExitButton.clicked.connect(self.back_click)
        self.CBackButton.clicked.connect(self.back_click)
        self.ParticipantButton.clicked.connect(lambda: self.participant_expert_click('participant'))
        self.ExpertButton.clicked.connect(lambda: self.participant_expert_click('expert'))
        self.PlanButton_4.clicked.connect(self.plan_click)
        self.InfrastructureButton.clicked.connect(lambda: self.infrastructure_shedule_click('inf'))
        self.SheduleButton.clicked.connect(lambda: self.infrastructure_shedule_click('she'))
        self.SaveButton.clicked.connect(self.save_password_click)

    def profile_click(self):
        self.MainFrame.setHidden(True)
        self.MyProfileFrame.setHidden(False)
        print(len(db.user_data))
        self.InfoNameLabel_2.setText(db.user_data[1])
        self.InfoSexLabel_2.setText(db.user_data[2])
        self.InfoIdLabel_2.setText(db.user_data[3])
        self.InfoBirthLabel.setText(
            str(db.user_data[5].year) + '-' + str(db.user_data[5].month) + '-' + str(db.user_data[5].day))
        self.InfoCountryLabel.setText(db.user_data[6])
        self.InfoEmailLabel.setText(db.user_data[7])
        self.InfoNameLabel_2.adjustSize()
        self.InfoSexLabel_2.adjustSize()
        self.InfoIdLabel_2.adjustSize()
        self.InfoBirthLabel.adjustSize()
        self.InfoCountryLabel.adjustSize()
        self.InfoEmailLabel.adjustSize()

    def competition_click(self):
        self.MainFrame.setHidden(True)
        self.CompetitionFrame.setHidden(False)
        self.block_competition_frame()
        self.NumCompetenceLabel.setText(str(db.user_data[9]))
        competence = db.get_competence_info(db.user_data[9])
        self.NameCompetenceLabel.setText(' - ' + competence[1])

    def results_click(self):
        self.MainFrame.setHidden(True)
        self.ResultsFrame.setHidden(False)
        self.InfoNameLabel.setText(db.user_data[1])
        self.InfoSexLabel.setText(db.user_data[2])
        self.InfoIdLabel.setText(db.user_data[3])
        self.InfoRegionLabel.setText(db.user_data[6])
        self.InfoChempionshipLabel.setText(str(db.user_data[10]))
        competence = db.get_competence_info(db.user_data[9])
        self.InfoCompetenceLabel.setText(competence[1])
        self.InfoNameLabel.adjustSize()
        self.InfoSexLabel.adjustSize()
        self.InfoIdLabel.adjustSize()
        self.InfoRegionLabel.adjustSize()
        self.InfoChempionshipLabel.adjustSize()
        self.InfoCompetenceLabel.adjustSize()
        marks = db.show_marks(db.user_data[0])
        self.ModulsTable.setRowCount(len(marks))
        self.ModulsTable.setColumnCount(2)
        self.ModulsTable.setHorizontalHeaderLabels(head_module)
        sum = 0
        for i in range(len(marks)):
            for j in range(2):
                if j == 0:
                    info = QTableWidgetItem('Модуль ' + str(marks[i][j]))
                else:
                    info = QTableWidgetItem(str(marks[i][j]))
                    sum += marks[i][j]
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ModulsTable.setItem(i, j, info)
        header = self.ModulsTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(self.ModulsTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)
        self.SumLabel.setText("Результат: "+str(sum))

    def participant_expert_click(self, role):
        self.block_competition_frame()
        self.PeopleFrame.setHidden(False)
        if role == 'participant':
            data = db.get_all_competitors_experts(db.user_data[9], db.user_data[0], db.user_data[8])
        else:
            data = db.get_all_competitors_experts(db.user_data[9], db.user_data[0], 4)
        size_str = 0
        for i in range(len(data)):
            data[i].pop(3)
            data[i].pop(3)
        if len(data) != 0:
            size_str = len(data[0])
        self.InfoTable.setRowCount(len(data))
        self.InfoTable.setColumnCount(size_str - 2)
        self.InfoTable.setHorizontalHeaderLabels(head_comp_exp)
        for i in range(len(data)):
            for j in range(size_str - 2):
                info = QTableWidgetItem(str(data[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.InfoTable.setItem(i, j, info)
        self.InfoTable.resizeColumnsToContents()
        header = self.InfoTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.InfoTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def plan_click(self):
        self.block_competition_frame()
        self.PlanFrame.setHidden(False)

        open_windows["Plan"] = PlanWindow(db.user_data[len(db.user_data) - 2])

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)

    def save_password_click(self):
        if self.NewPasswordEdit.text() == self.RepeatNewPasswordEdit.text():
            num_bs = 0
            num_ls = 0
            num_c = 0
            isspace = 0
            newPassword = self.NewPasswordEdit.text()
            for i in newPassword:
                if i.isupper():
                    num_bs += 1
                if i.isdigit():
                    num_c += 1
                if i.islower():
                    num_ls += 1
                if i == ' ':
                    isspace += 1
            if len(newPassword) >= 6 and len(
                    newPassword) <= 16 and num_bs != 0 and num_c != 0 and num_ls != 0 and isspace == 0:
                self.ErrorLabel.setText('Пароль изменён')
                db.change_password(newPassword)
            else:
                self.ErrorLabel.setText('Ошибка')
        else:
            self.ErrorLabel.setText('Пароли не совпадают')

    def infrastructure_shedule_click(self, but):
        self.block_competition_frame()
        self.LinkFrame.setHidden(False)
        competence = db.get_competence_info(str(db.user_data[9]))
        if but == 'inf':
            self.InfoLinkLabel.setText(competence[5])
        else:
            self.InfoLinkLabel.setText(competence[4])

        self.InfoLinkLabel.adjustSize()

    def log_out(self):
        open_windows[self.objectName()].close()
        open_windows["DefaultWindow"].show()


class CoordinatorWindow(QtWidgets.QMainWindow, CoordinatorWindowUi.Ui_CoordinatorWindow):
    role = ''

    def block_frame(self):
        self.VolunteersFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()
        self.GreetLabel.setText(time() + db.user_data[1])
        self.GreetLabel.adjustSize()
        chempionship = db.get_current_championship().split('. ')
        self.NameChempionshipsLabel_2.setText(chempionship[1])
        self.NameChempionshipsLabel_2.adjustSize()

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
        self.ManagingVolunteersButton.clicked.connect(lambda: self.managing_click('volunteers'))
        self.ManagingSponsorsButton.clicked.connect(lambda: self.managing_click('sponsors'))
        self.BackButton.clicked.connect(self.back_click)
        self.InsertButton.clicked.connect(lambda: self.open_insert_window(self.role))
        self.DistributeButton.clicked.connect(self.open_distribute_window)
        self.SearchButton.clicked.connect(self.search_click)

    def managing_click(self, manage):
        self.role = manage
        self.MainFrame.setHidden(True)
        self.VolunteersFrame.setHidden(False)
        if manage == 'sponsors':
            self.ManagingVolunteersLabel.setText('Управление спонсорами')
            self.InsertButton.setText('Добавить спонсоров')
            self.NumVolunteersLabel.setText('Всего спонсоров')
            self.DistributeButton.setHidden(True)
            data = db.get_all_sponsors()
        if manage == 'volunteers':
            self.ManagingVolunteersLabel.setText('Управление волонтерами')
            self.InsertButton.setText('Добавить волонтеров')
            self.NumVolunteersLabel.setText('Всего волонтеров')
            self.DistributeButton.setHidden(False)
            data = db.get_all_volunteers()
        size_str = 0
        if len(data) != 0:
            size_str = len(data[0])
        self.VolunteersTable.setRowCount(len(data))
        self.VolunteersTable.setColumnCount(size_str)
        self.VolunteersTable.setHorizontalHeaderLabels(head_vol)
        for i in range(len(data)):
            for j in range(size_str):
                info = QTableWidgetItem(str(data[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.VolunteersTable.setItem(i, j, info)
        header = self.VolunteersTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.VolunteersTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)
        self.InfoNumVolunteersLabel.setText(str(len(data)))
        all_competence = db.get_all_competences()
        self.CompetenceComboBox.clear()
        for i in range(len(all_competence)):
            self.CompetenceComboBox.addItem(all_competence[i])
        self.CompetenceComboBox.adjustSize()

    def open_insert_window(self, role):
        self.insert = InsertVolunteers(role, self)
        self.insert.show()

    def open_distribute_window(self):
        self.distribute = DistributeVolunteers(self)
        self.distribute.show()

    def search_click(self):
        all_competence = db.get_all_competences()
        competence = all_competence[self.CompetenceComboBox.currentIndex()].split('. ')
        if self.role == 'sponsors':
            data = db.get_sponsors(competence[0])
        else:
            data = db.get_volunteers(competence[0])
        size_str = 0
        if len(data) != 0:
            size_str = len(data[0])
        self.VolunteersTable.setRowCount(len(data))
        self.VolunteersTable.setColumnCount(size_str)
        self.VolunteersTable.setHorizontalHeaderLabels(head_vol)
        for i in range(len(data)):
            for j in range(size_str):
                info = QTableWidgetItem(str(data[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.VolunteersTable.setItem(i, j, info)
        header = self.VolunteersTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.VolunteersTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)

    def log_out(self):
        open_windows[self.objectName()].close()
        open_windows["DefaultWindow"].show()


class ExpertWindow(QtWidgets.QMainWindow, ExpertWindowUi.Ui_ExpertWindow):
    def block_frame(self):
        self.MarksFrame.setHidden(True)
        self.ResultsFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()
        self.GreetLabel.setText(time() + db.user_data[1])
        self.GreetLabel.adjustSize()
        chempionship = db.get_current_championship().split('. ')
        self.NameChempionshipsLabel.setText(chempionship[1])
        self.NameChempionshipsLabel.adjustSize()

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
        self.EnterRatingsButton.clicked.connect(self.enter_ratings_click)
        self.ResultsButton.clicked.connect(self.results_click)
        self.RBackButton.clicked.connect(self.back_click)
        self.MBackButton.clicked.connect(self.back_click)
        self.PushButton.clicked.connect(self.insert)
        self.SearchButton.clicked.connect(self.search)

    def enter_ratings_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.MarksFrame.setHidden(False)
        all_competitors = db.get_all_competitors_experts(db.user_data[9], 0, 2)
        self.MCompetitorComboBox.clear()
        self.ModulComboBox.clear()
        self.MarkComboBox.clear()
        for i in range(len(all_competitors)):
            self.MCompetitorComboBox.addItem(str(all_competitors[i][0]) + '. ' + str(all_competitors[i][1]))
        for i in range(5):
            self.ModulComboBox.addItem('Модуль' + str(i + 1))
        for i in range(10):
            self.MarkComboBox.addItem(str(i + 1))
        self.MCompetitorComboBox.adjustSize()
        self.MarkComboBox.adjustSize()
        self.ModulComboBox.adjustSize()

    def results_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.ResultsFrame.setHidden(False)
        all_competitors = db.get_all_competitors_experts(db.user_data[9], 0, 2)
        self.CompetitorComboBox.clear()
        for i in range(len(all_competitors)):
            self.CompetitorComboBox.addItem(str(all_competitors[i][0]) + '. ' + str(all_competitors[i][1]))
        self.CompetitorComboBox.adjustSize()

    def insert(self):
        all_competitors = db.get_all_competitors_experts(db.user_data[9], 0, 2)
        competitor = all_competitors[self.MCompetitorComboBox.currentIndex()][0]
        module = self.ModulComboBox.currentIndex() + 1
        mark = self.MarkComboBox.currentIndex() + 1
        data_mark = [competitor, module, mark]
        db.add_marks(data_mark)

    def search(self):
        all_competitors = db.get_all_competitors_experts(db.user_data[9], 0, 2)
        competitor = all_competitors[self.CompetitorComboBox.currentIndex()][0]
        marks = db.show_marks(competitor)
        self.ResultsWidget.setRowCount(len(marks))
        self.ResultsWidget.setColumnCount(2)
        self.ResultsWidget.setHorizontalHeaderLabels(head_module)
        for i in range(len(marks)):
            for j in range(2):
                if j == 0:
                    info = QTableWidgetItem('Модуль ' + str(marks[i][j]))
                else:
                    info = QTableWidgetItem(str(marks[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ResultsWidget.setItem(i, j, info)
        header = self.ResultsWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.ResultsWidget.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)

    def log_out(self):
        open_windows[self.objectName()].close()
        open_windows["DefaultWindow"].show()


class AuthDialog(QtWidgets.QMainWindow, AuthDialogUi.Ui_AuthDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.log_in)

    def log_in(self):
        login = self.LoginEdit.text()
        password = self.PasswordEdit.text()
        db.log_in(login, password)
        type = 0

        if len(db.user_data) != 0:
            type = int(db.user_data[len(db.user_data) - 3])

        if type == 1:
            open_windows[AdminWindow().objectName()].show()
            self.ErrorLabel.setText('')
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 2:
            open_windows[CompetitorWindow().objectName()].show()
            self.ErrorLabel.setText('')
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 3:
            open_windows[CoordinatorWindow().objectName()].show()
            self.ErrorLabel.setText('')
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 4:
            open_windows[ExpertWindow().objectName()].show()
            self.ErrorLabel.setText('')
            self.close()
            open_windows["DefaultWindow"].close()
        else:
            self.ErrorLabel.setText("Неправильные данные")
            pass


class InsertVolunteers(QtWidgets.QMainWindow, InsertVolunteersUi.Ui_InsertVolunteers):
    def __init__(self, role, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        open_windows[self.objectName()] = self
        all_competence = db.get_all_competences()
        for i in range(len(all_competence)):
            self.CompetitionComboBox.addItem(all_competence[i])
        self.CompetitionComboBox.adjustSize()
        self.MaleRadioButton.click()
        if role == 'sponsors':
            self.InsertLabel.setText('Добавление спонсоров')
        self.InsertButton.clicked.connect(lambda: self.insert(role, parent))
        reg = QRegExp("[а-яА-Яa-zA-Z- 0-9]{40}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.NameEdit.setValidator(pValidator)
        self.RegionEdit.setValidator(pValidator)


    def insert(self, role, parent):
        all_competence = db.get_all_competences()
        name = self.NameEdit.text()
        if self.MaleRadioButton.isChecked():
            value_gender = 'М'
        else:
            value_gender = 'Ж'
        region = self.RegionEdit.text()
        competence = all_competence[self.CompetitionComboBox.currentIndex()].split('. ')
        data = (name, value_gender, region, competence[0])
        if region != '' and name != '':
            if role == 'volunteers':
                db.add_volunteer(data)
            else:
                db.add_sponsor(data)
        CoordinatorWindow.managing_click(parent, role)
        self.close()


class DistributeVolunteers(QtWidgets.QMainWindow, DistributeVolunteersUi.Ui_DistributeVolunteers):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        open_windows[self.objectName()] = self
        all_competence = db.get_all_competences()
        for i in range(len(all_competence)):
            self.CompetenceComboBox.addItem(all_competence[i])
        self.CompetenceComboBox.adjustSize()
        for i in range(len(all_competence)):
            self.NewCompetenceComboBox.addItem(all_competence[i])
        self.NewCompetenceComboBox.adjustSize()
        self.SearchButton.clicked.connect(self.search_click)
        self.DistributeButton.clicked.connect(lambda: self.distribute_click(parent))

    def search_click(self):
        all_competence = db.get_all_competences()
        competence = all_competence[self.CompetenceComboBox.currentIndex()].split('. ')
        data = db.get_volunteers(competence[0])
        size_str = 0
        if len(data) != 0:
            size_str = len(data[0])
        self.VolunteersTable.setRowCount(len(data))
        self.VolunteersTable.setColumnCount(size_str)
        self.VolunteersTable.setHorizontalHeaderLabels(head_vol)
        for i in range(len(data)):
            for j in range(size_str):
                info = QTableWidgetItem(str(data[i][j]))
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.VolunteersTable.setItem(i, j, info)
        header = self.VolunteersTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(self.VolunteersTable.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

    def distribute_click(self, parent):
        try:
            all_competence = db.get_all_competences()
            id = self.VolunteersTable.selectionModel().selectedRows()
            for index in sorted(id):
                str_id = self.VolunteersTable.item(index.row(), 0).text()
            competence = all_competence[self.NewCompetenceComboBox.currentIndex()].split('. ')
            data = (str_id, competence[0])
            db.change_vol_competence(data)
            self.close()
            CoordinatorWindow.search_click(parent)
        except BaseException as e:
            print(e)

class InsertUsers(QtWidgets.QMainWindow, InsertUsersUi.Ui_InsertUsers):
    def __init__(self, status, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.MaleRadioButton.click()
        self.InsertButton.clicked.connect(lambda: self.insert_user(status, parent))
        all_competence = db.get_all_competences()
        for i in range(len(all_competence)):
            self.CompetenceComboBox.addItem(all_competence[i])
        if status == 'coordinate':
            self.CompetitionLabel.setHidden(True)
            self.CompetenceComboBox.setHidden(True)
        reg = QRegExp("[а-яА-Яa-zA-Z- 0-9]{40}")
        reg_mail = QRegExp("[а-яА-Яa-zA-Z- @.0-9]{40}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        mValidator = QRegExpValidator(self)
        mValidator.setRegExp(reg_mail)
        self.NameEdit.setValidator(pValidator)
        self.RegionEdit.setValidator(pValidator)
        self.PasswordEdit.setValidator(mValidator)
        self.EmailEdit.setValidator(mValidator)
        self.ErrorLabel.setText('')
        self.CompetenceComboBox.adjustSize()

    def insert_user(self, status, parent):
        all_competence = db.get_all_competences()
        name = self.NameEdit.text()
        if self.MaleRadioButton.isChecked():
            value_gender = 'М'
        else:
            value_gender = 'Ж'
        region = self.RegionEdit.text()
        email = self.EmailEdit.text()
        password = self.PasswordEdit.text()
        value_birth = self.BirthEdit.date()
        birth = str(value_birth.year()) + '-' + str(value_birth.month()) + '-' + str(value_birth.day())
        competence = all_competence[self.CompetenceComboBox.currentIndex()].split('. ')
        if name != '' and region != '' and email != '' and password != '':
            if status == 'coordinate':
                insert_data = (name, value_gender, region, email, password, birth, str('999'))
                db.add_coordinator(insert_data)
            elif status == 'expert':
                insert_data = (name, value_gender, region, email, password, birth, competence[0])
                db.add_expert(insert_data)
            else:
                insert_data = (name, value_gender, region, email, password, birth, competence[0])
                db.add_competitor(insert_data)
                AdminWindow.managing_competitor_click(parent)
            self.close()
        else:
            self.ErrorLabel.setText('Поля не должны быть пустыми')
            self.ErrorLabel.adjustSize()


class CompetitorProfileDialog(QtWidgets.QMainWindow, CompetitorProfileDialogUi.Ui_CompetitorProfileDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class PlanWindow(QtWidgets.QMainWindow, PlanWindowUi.Ui_PlanWindow):
    def __init__(self, comp):
        pixmap = QPixmap(str(os.getcwd()) + '/gui_files/%s.png' % comp)

        super().__init__()
        self.setupUi(self)
        self.resize(pixmap.width(), pixmap.height())
        self.PicLabel.resize(pixmap.width(), pixmap.height())
        self.PicLabel.setPixmap(
            pixmap.scaled(self.PicLabel.width(), self.PicLabel.height(), QtCore.Qt.KeepAspectRatio))
        self.show()
# default_win = DefaultWindow()
