from PyQt5 import QtCore, QtGui, QtWidgets

from gui_files import AdminWindowUi, CompetitorWindowUi, CoordinatorWindowUi, DefaultWindowUi, ExpertWindowUi
from gui_files import AuthDialogUi, CompetitorProfileDialogUi
from gui_files import DistributeVolunteersUi, InsertVolunteersUi, InsertUsersUi
from gui_files import AboutRegion, AboutWorldSkills, AboutWSRussia

import db
import datetime

open_windows = {}
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

    def history_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.AboutFrame.setHidden(False)

    def competition_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.CompetitionFrame.setHidden(False)

    def championships_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.ChempionshipsFrame.setHidden(False)

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


    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
        self.ManagingChampionshipsButton.clicked.connect(self.managing_chempionships_click)
        self.ManagingCompetitorsButton.clicked.connect(self.managing_competitor_click)
        self.ExpertButton.clicked.connect(lambda: self.open_insert_window('expert'))
        self.CoordinatorButton.clicked.connect(lambda: self.open_insert_window('coordinate'))
        self.InsertButton.clicked.connect(lambda: self.open_insert_window('competitor'))
        self.CoBackButton.clicked.connect(self.back_click)
        self.ChBackButton.clicked.connect(self.back_click)

    def managing_chempionships_click(self):
        self.ManageChempionshipsFrame.setHidden(False)
        self.MainFrame.setHidden(True)

    def managing_competitor_click(self):
        self.CompetitorFrame.setHidden(False)
        self.MainFrame.setHidden(True)

    def open_insert_window(self, status):
        self.insert = InsertUsers(status)
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

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
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
        self.SaveButton.clicked.connect(self.save_password_click)

    def profile_click(self):
        self.MainFrame.setHidden(True)
        self.MyProfileFrame.setHidden(False)
        print(len(db.user_data))
        self.InfoNameLabel_2.setText(db.user_data[1])

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
            if len(newPassword) >= 6 and len(newPassword) <= 16 and num_bs != 0 and num_c != 0 and num_ls != 0 and isspace == 0:
                self.ErrorLabel.setText('Пароль изменён')
            else:
                self.ErrorLabel.setText('Ошибка')
        else:
            self.ErrorLabel.setText('Пароли не совпадают')

    def infrastructure_shedule_click(self):
        self.block_competition_frame()
        self.LinkFrame.setHidden(False)

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
        self.GreetLabel.setText(time() + db.user_data[1])
        self.GreetLabel.adjustSize()

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
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

    def init_buttons_actions(self):
        self.LogoutAction.triggered.connect(self.log_out)
        self.EnterRatingsButton.clicked.connect(self.enter_ratings_click)
        self.ResultsButton.clicked.connect(self.results_click)
        self.RBackButton.clicked.connect(self.back_click)
        self.MBackButton.clicked.connect(self.back_click)

    def enter_ratings_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.MarksFrame.setHidden(False)

    def results_click(self):
        self.block_frame()
        self.MainFrame.setHidden(True)
        self.ResultsFrame.setHidden(False)

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
        db.user_data = db.log_in(login, password)
        type = 0

        if len(db.user_data) != 0:
            type = int(db.user_data[len(db.user_data) - 1])

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

class InsertUsers(QtWidgets.QMainWindow, InsertUsersUi.Ui_InsertUsers):
    def __init__(self, status):
        super().__init__()
        self.setupUi(self)
        open_windows[self.objectName()] = self
        if status == 'coordinate':
            self.CompetitionLabel.setHidden(True)
            self.CompetenceComboBox.setHidden(True)

class CompetitorProfileDialog(QtWidgets.QMainWindow, CompetitorProfileDialogUi.Ui_CompetitorProfileDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# default_win = DefaultWindow()
