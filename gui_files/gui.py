from PyQt5 import QtCore, QtGui, QtWidgets

from gui_files import AdminWindowUi, CompetitorWindowUi, CoordinatorWindowUi, DefaultWindowUi, ExpertWindowUi
from gui_files import AuthDialogUi, CompetitorProfileDialogUi
from gui_files import DistributeVolunteersUi, InsertVolunteersUi

import db

open_windows = {}
user_data = []


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

    def show_AuthDialog(self):
        self.AuthDialog.show()


class AdminWindow(QtWidgets.QMainWindow, AdminWindowUi.Ui_AdminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)

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
        self.ProfileButton.clicked.connect(self.profile_click)
        self.CompetitionButton.clicked.connect(self.competition_click)
        self.ResultsButton.clicked.connect(self.results_click)
        self.RBackButton.clicked.connect(self.back_click)
        self.ExitButton.clicked.connect(self.back_click)
        self.CBackButton.clicked.connect(self.back_click)
        self.ParticipantButton.clicked.connect(self.participant_expert_click)
        self.ExpertButton.clicked.connect(self.participant_expert_click)
        self.PlanButton_4.clicked.connect(self.plan_click)
        self.InfrastructureButton.clicked.connect(self.infrastructure_shedule_click)
        self.SheduleButton.clicked.connect(self.infrastructure_shedule_click)

    def profile_click(self):
        self.MainFrame.setHidden(True)
        self.MyProfileFrame.setHidden(False)

    def competition_click(self):
        self.MainFrame.setHidden(True)
        self.CompetitionFrame.setHidden(False)
        self.block_competition_frame()

    def results_click(self):
        self.MainFrame.setHidden(True)
        self.ResultsFrame.setHidden(False)

    def participant_expert_click(self):
        self.block_competition_frame()
        self.PeopleFrame.setHidden(False)

    def plan_click(self):
        self.block_competition_frame()
        self.PlanFrame.setHidden(False)

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)

    def infrastructure_shedule_click(self):
        self.block_competition_frame()
        self.LinkFrame.setHidden(False)

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)

    def log_out(self):
        open_windows[self.objectName()].close()
        open_windows["DefaultWindow"].show()


class CoordinatorWindow(QtWidgets.QMainWindow, CoordinatorWindowUi.Ui_CoordinatorWindow):
    role =''
    def block_frame(self):
        self.VolunteersFrame.setHidden(True)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()
        self.block_frame()
        self.ManagingVolunteersButton.clicked.connect(lambda: self.managing_click('volunteers'))
        self.ManagingSponsorsButton.clicked.connect(lambda: self.managing_click('sponsors'))
        self.BackButton.clicked.connect(self.back_click)
        self.InsertButton.clicked.connect(lambda: self.open_insert_window(self.role))
        self.DistributeButton.clicked.connect(self.open_distribute_window)

    def managing_click(self, manage):
        self.role = manage
        self.MainFrame.setHidden(True)
        self.VolunteersFrame.setHidden(False)
        if manage == 'sponsors':
            self.ManagingVolunteersLabel.setText('Управление спонсорами')
            self.InsertButton.setText('Добавить спонсоров')
            self.DistributeButton.setHidden(True)
        if manage == 'volunteers':
            self.ManagingVolunteersLabel.setText('Управление волонтерами')
            self.InsertButton.setText('Добавить волонтеров')
            self.DistributeButton.setHidden(False)

    def open_insert_window(self, role):
        self.insert = InsertVolunteers(role)
        self.insert.show()

    def open_distribute_window(self):
        self.distribute = DistributeVolunteers()
        self.distribute.show()

    def back_click(self):
        self.block_frame()
        self.MainFrame.setHidden(False)

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)

    def log_out(self):
        open_windows[self.objectName()].close()
        open_windows["DefaultWindow"].show()


class ExpertWindow(QtWidgets.QMainWindow, ExpertWindowUi.Ui_ExpertWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        self.init_buttons_actions()

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)

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
        user_data = db.log_in(login, password)
        type = 0

        if len(user_data) != 0:
            type = int(user_data[len(user_data) - 1])

        if type == 1:
            open_windows[AdminWindow().objectName()].show()
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 2:
            open_windows[CompetitorWindow().objectName()].show()
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 3:
            open_windows[CoordinatorWindow().objectName()].show()
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 4:
            open_windows[ExpertWindow().objectName()].show()
            self.close()
            open_windows["DefaultWindow"].close()
        else:
            self.ErrorLabel.setText("Неправильные данные")

class InsertVolunteers(QtWidgets.QMainWindow, InsertVolunteersUi.Ui_InsertVolunteers):
    def __init__(self, role):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        if role == 'sponsors':
            self.InsertLabel.setText('Добавление спонсоров')

class DistributeVolunteers(QtWidgets.QMainWindow, DistributeVolunteersUi.Ui_DistributeVolunteers):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self

class CompetitorProfileDialog(QtWidgets.QMainWindow, CompetitorProfileDialogUi.Ui_CompetitorProfileDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# default_win = DefaultWindow()
