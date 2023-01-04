import sys
from main import ZoomButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5 import QtGui, QtWidgets


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход')
        self.setFixedSize(400, 290)
        self.setStyleSheet("background-color: rgb(27, 32, 39);")
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.label = QLabel('ВХОД', self)
        self.label.setFont(QtGui.QFont("Segou UI Black", 11, QtGui.QFont.Bold))
        self.label.setStyleSheet('color: rgb(210, 210, 210);')
        self.label.move(170, 40)

        self.line1 = QLineEdit(self)
        self.line1.resize(271, 40)
        self.line1.move(65, 80)
        self.line1.setStyleSheet('''
        border-radius: 4px;
        border-width: 3px;
        border-color: rgb(36, 42, 52);
        background-color: rgb(36, 42, 52);
        border-style: solid;
        color: rgb(210, 210, 210);''')
        self.line1.setFont(QtGui.QFont("Cascadia Mono Semibold", 11, QtGui.QFont.Bold))

        self.line2 = QLineEdit(self)
        self.line2.resize(271, 40)
        self.line2.move(65, 140)
        self.line2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line2.setStyleSheet('''
        border-radius: 4px;
        border-width: 3px;
        border-color: rgb(36, 42, 52);
        background-color: rgb(36, 42, 52);
        border-style: solid;
        color: rgb(210, 210, 210);''')
        self.line2.setFont(QtGui.QFont("Cascadia Mono Semibold", 11, QtGui.QFont.Bold))

        self.btn1 = ZoomButton('Вход', self)
        self.btn1.resize(115, 41)
        self.btn1.move(65, 200)
        self.btn1.setStyleSheet('''
        border-radius: 4px;
        color: rgb(210, 210, 210);
        background-color: rgb(52, 121, 214);
        border-style: solid;''')
        self.btn1.setFont(QtGui.QFont("Calibri Light", 10, QtGui.QFont.Bold))

        self.btn2 = ZoomButton('Регистрация', self)
        self.btn2.resize(115, 41)
        self.btn2.move(190, 200)
        self.btn2.setStyleSheet('''
        border-radius: 4px;
        color: rgb(210, 210, 210);
        background-color: rgb(52, 121, 214);
        border-style: solid;''')
        self.btn2.setFont(QtGui.QFont("Calibri Light", 10, QtGui.QFont.Bold))

        self.close_btn = ZoomButton(self)
        self.close_btn.resize(20, 41)
        self.close_btn.move(315, 200)
        self.close_btn.setStyleSheet('''
                                                border-radius: 4px;
                                                color: rgb(86, 92, 102);
                                                background-color: rgb(199, 84, 80);
                                                border-style: solid;''')

        def close_login():
            QApplication.quit()

        self.close_btn.clicked.connect(close_login)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
