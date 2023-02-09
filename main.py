import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests
from PIL import Image
from io import BytesIO
from PyQt5.QtCore import Qt


def get_image(toponym_lattitude, toponym_longitude, spn, l):
    map_params = {
        "ll": ','.join([toponym_lattitude, toponym_longitude]),
        "spn": ",".join([spn, spn]),
        "l": l, 'pt': ",".join([toponym_longitude, toponym_lattitude])
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    img = Image.open(BytesIO(
        response.content))
    img.show()
    img.save('1.png')


def key_press_event(event):
    global spn, lantitude, longitude
    if event.key() == Qt.Key_PageUp:
        spn += 0.0005
    elif event.key() == Qt.Key_PageDown:
        if spn > 0.0005:
            spn -= 0.0005
    elif event.key() == Qt.Key_Right:
        longitude += spn
    elif event.key() == Qt.Key_Left:
        longitude += spn
    elif event.key() == Qt.Key_Down:
        lantitude -= spn
    elif event.key() == Qt.Key_Up:
        lantitude += spn


class Maps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Maps.ui', self)


if __name__ == '__main__':
    lantitude, longitude = 45.036114, 38.910410
    spn = 0.0005
    application = QApplication(sys.argv)
    window = Maps()
    window.show()
    sys.exit(application.exec())