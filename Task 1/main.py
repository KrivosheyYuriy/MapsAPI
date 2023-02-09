import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

import requests
from PIL import Image
from io import BytesIO


def get_image(toponym_longitude, toponym_lattitude, spn, l):
    map_params = {
        "ll": ','.join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([spn, spn]),
        "l": l, 'pt': ",".join([toponym_longitude, toponym_lattitude])
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    img = Image.open(BytesIO(
        response.content))
    img.save('1.png')


class Maps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Maps.ui', self)
        self.add_map()

    def add_map(self):
        get_image('38.910410', '45.036114', '0.0005', 'map')
        pixmap = QPixmap('1.png')
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Maps()
    window.show()
    sys.exit(application.exec())
