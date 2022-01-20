#!/urs/bin/python3
#-*- coding: utf-8 -*-

#from PyQt6 import QtWidgets
#from PyQt6 import uic

import tables
import workers

import sys  # sys нужен для передачи argv в QApplication
import os

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.ui = uic.loadUi('tables.ui')  # Это нужно для инициализации нашего дизайна
        self.ui.show()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем (запускается если стартует с него)
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainForm()
    window.start()  # то запускаем функцию main()
    #app.exec_()   #sys.exit(MainForm.exec_())
