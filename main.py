import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from UI import Ui_MainWindow
from random import randint


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            pia = QPainter()
            pia.begin(self)
            pia.setBrush(QColor('yellow'))
            radius = randint(1, 300)
            pia.drawEllipse(randint(0, 900), randint(0, 700), radius, radius)
            pia.end()
        self.flag = False

    def run(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
