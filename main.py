import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Maps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Maps.ui', self)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Maps()
    window.show()
    sys.exit(application.exec())
