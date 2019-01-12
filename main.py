from PyQt5 import QtWidgets
import sys
from gui_files import gui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = gui.DefaultWindow()
    sys.exit(app.exec())