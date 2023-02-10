import requests
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
import sys
from map_generator import Ui_MapGenerator


class MainWindow(QMainWindow, Ui_MapGenerator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Big_Task_1')
        self.show_map.clicked.connect(self.generate)

    def generate(self):
        x_coord = self.x_line.text()
        y_coord = self.y_line.text()
        size = self.size_line.text()
        check = self.check(x_coord, y_coord, size)
        if check:
            self.doing_request(check[0], check[1], check[2])
        else:
            self.map_widget.setText('Некорректные данные')

    def check(self, x, y, z):
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            if z > 4.0:
                z = 4.0
            elif z < 1.0:
                z = 1.0
            return x, y, z
        except ValueError:
            return False

    def doing_request(self, x, y, z):
        self.map_widget.setText('')
        # apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
        response = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={y},{x}&size=450,450&scale={z}&l=map")
        with open('file.png', 'wb') as f:
            f.write(response.content)
        response = QPixmap('file.png')
        self.map_widget.setPixmap(response)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
