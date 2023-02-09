import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class Maps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Maps.ui', self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            pass  # увеличить масштаб на какое-то значение

        if event.key() == Qt.Key_PageDown:
            pass  # уменьшить масштаб на какое-то значение


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Maps()
    window.show()
    sys.exit(application.exec())
