from PyQt5 import QtCore, QtGui, QtWidgets

from gui_files import AdminWindowUi, CompetitorWindowUi, CoordinatorWindowUi, DefaultWindowUi, ExpertWindowUi
from gui_files import AuthDialogUi, CompetitorProfileDialogUi


class DefaultWindow(QtWidgets.QMainWindow, DefaultWindowUi.Ui_DefaultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


class AdminWindow(QtWidgets.QMainWindow, AdminWindowUi.Ui_AdminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CompetitorWindow(QtWidgets.QMainWindow, CompetitorWindowUi.Ui_CompetitorWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CoordinatorWindow(QtWidgets.QMainWindow, CoordinatorWindowUi.Ui_CoordinatorWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ExpertWindow(QtWidgets.QMainWindow, ExpertWindowUi.Ui_ExpertWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class AuthDialog(QtWidgets.QMainWindow, AuthDialogUi.Ui_AuthDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CompetitorProfileDialog(QtWidgets.QMainWindow, CompetitorProfileDialogUi.Ui_CompetitorProfileDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
