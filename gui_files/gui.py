from PyQt5 import QtCore, QtGui, QtWidgets

from gui_files import AdminWindowUi, CompetitorWindowUi, CoordinatorWindowUi, DefaultWindowUi, ExpertWindowUi
from gui_files import AuthDialogUi, CompetitorProfileDialogUi

import db

open_windows = {}
user_data = []


class DefaultWindow(QtWidgets.QMainWindow, DefaultWindowUi.Ui_DefaultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        open_windows["DefaultWindow"] = self
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


class CoordinatorWindow(QtWidgets.QMainWindow, CoordinatorWindowUi.Ui_CoordinatorWindow):
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
        self.window = ""

    def log_in(self):
        login = self.LoginEdit.text()
        password = self.PasswordEdit.text()
        user_data = db.log_in(login, password)
        type = 0

        if len(user_data) != 0:
            type = int(user_data[len(user_data) - 1])
        if type == 1:
            self.window = AdminWindow()
            self.window.show()
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 2:
            self.window = CompetitorWindow()
            self.window.show()
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 3:
            self.window = CoordinatorWindow()
            self.window.show()
            self.close()
            open_windows["DefaultWindow"].close()
        elif type == 4:
            self.window = ExpertWindow()
            self.window.show()
            self.close()
            open_windows["DefaultWindow"].close()
        else:
            self.ErrorLabel.setText("Неправильные данные")


class CompetitorProfileDialog(QtWidgets.QMainWindow, CompetitorProfileDialogUi.Ui_CompetitorProfileDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# default_win = DefaultWindow()
