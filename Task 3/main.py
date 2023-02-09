import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests
from PIL import Image
from io import BytesIO
from PyQt5.QtCore import Qt


def get_image(toponym_lattitude, toponym_longitude, z, l):
    map_params = {
        "ll": ','.join([str(toponym_lattitude), str(toponym_longitude)]),
        "z": z,
        "l": l
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

    def keyPressEvent(self, event):
        global z, lantitude, longitude

        if event.key() == Qt.Key_PageUp:
            if z < 17:
                z += 1

        elif event.key() == Qt.Key_PageDown:
            if z > 0:
                z -= 1

        elif event.key() == Qt.Key_Left:
            longitude -= 0.001
            if longitude <= -180:
                longitude += 360

        elif event.key() == Qt.Key_Right:
            longitude += 0.001
            if longitude > 180:
                longitude -= 360

        elif event.key() == Qt.Key_Down:
            lantitude -= 0.001
            if lantitude < -90:
                lantitude += 180

        elif event.key() == Qt.Key_Up:
            lantitude += 0.001
            if lantitude > 90:
                lantitude -= 180
        self.add_map()

    def add_map(self):
        get_image(longitude, lantitude, z, 'map')
        pixmap = QPixmap('1.png')
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    lantitude, longitude = 45.036114, 38.910410
    z = 17
    application = QApplication(sys.argv)
    window = Maps()
    window.show()
    sys.exit(application.exec())