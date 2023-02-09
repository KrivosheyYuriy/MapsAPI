import random
import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
from PyQt5.QtCore import Qt
import requests
from PIL import Image


def get_image(toponym_longitude, toponym_lattitude, spn):
    map_params = {
        "ll": ','.join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(spn),
        "l": random.choice(["map", "sat"]), 'pt': ",".join([toponym_longitude, toponym_lattitude])
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    img = Image.open(BytesIO(
        response.content))
    img.show()
    img.save('1.png')


def key_press_event(event):
    global spn
    if event.key() == Qt.Key_PageUp:
        spn += 0.0005
    elif event.key() == Qt.Key_PageDown:
        if spn > 0.0005:
            spn -= 0.0005


get_image('38.910410', '45.036155', ['0.005', '0.005'])
spn = 0