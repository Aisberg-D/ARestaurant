#!/urs/bin/python3
# -*- coding: utf-8 -*-

from PySide2 import QtWidgets, QtCore, QtGui

import sys  # sys нужна для передачи argv в QApplication
import os  # библиотека для доступа к системным параметрам
import time
import datetime  # библиотека для работы с датой
import socket
import requests
import http.server
import threading
import json

from ui_files import main_ui, tables_ui  # конвертированные файлы интерфейса

import my_lib_qt_1_0

import tables
import workers


class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_ui.py
        super().__init__()
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # ====================================== Обработчики событий

        # Обработчики главного меню

        self.ui.fulling.triggered.connect(lambda: self.fulling_tables())
        self.ui.save.triggered.connect(lambda: self.save_tables_inXML(self.save_tables()))

        # Обработчики календаря

        self.ui.calendarWidget.clicked['QDate'].connect(lambda: self.target_calendar_day())
        self.ui.pushButton_curdate.clicked.connect(lambda: self.cur_calendar_day())

        # Кнопки добавления\удалени строки

        self.ui.button_add_table = QtWidgets.QPushButton()
        self.ui.button_add_table.setText("Добавить стол")
        self.ui.button_add_table.clicked.connect(lambda: self.add_one_str_with_table())
        self.ui.button_del_table = QtWidgets.QPushButton()
        self.ui.button_del_table.setText("Удалить стол")
        self.ui.button_del_table.clicked.connect(lambda: self.del_one_str_with_table())

        # Для тестов

        # self.ui.pushButton.clicked.connect(lambda: table_show(app))
        # self.ui.pushButton.clicked.connect(lambda: show_msg(None, None))
        # self.ui.pushButton.clicked.connect()

        # tables.list_tables[2](5, 10, 0, None, None) #Пример правки при помощи __Call__

        # Таблица закзов

        # self.ui.tableWidget_orders.setColumnCount(len(tables.headers_orders))
        # self.ui.tableWidget_orders.setHorizontalHeaderLabels(tables.headers_tables)
        # my_lib_qt_1_0.set_column_size_as_conent(self.ui.tableWidget_orders)

        # Таблица столов

        self.ui.tableWidget_tables.setColumnCount(len(tables.headers_tables))
        self.ui.tableWidget_tables.setHorizontalHeaderLabels(tables.headers_tables)
        my_lib_qt_1_0.set_column_size_as_content(self.ui.tableWidget_tables)

        # Таблица официантов

        self.ui.tableWidget_waiters.setColumnCount(5)
        self.ui.tableWidget_waiters.setHorizontalHeaderLabels(workers.headers_workers)
        my_lib_qt_1_0.set_column_size_as_content(self.ui.tableWidget_waiters)

    # ====================================== Методы главной формы

    # ====================================== Работа с календарём

    def target_calendar_day(self):
        """Функция для проверки выбранной даты в календаре"""

        # print(self.ui.calendarWidget.selectedDate().toString("yyyy.MM.dd"))

        sel_dat = self.ui.calendarWidget.selectedDate()

        if sel_dat < datetime.datetime.now():
            if os.path.isfile(f'Worked Days/{sel_dat.toString("yyyy")}/{sel_dat.toString("MM")}/'
                              f'{sel_dat.toString("dd")}_orders.xml'):

                res = QtWidgets.QMessageBox.question(
                    self,
                    'Подтверждение',
                    f'За день {sel_dat.toString("MM.dd")} найдены записи. Загрузить для просмотра?',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

                if res == QtWidgets.QMessageBox.Yes:
                    my_lib_qt_1_0.do_nothing()  # todo Тут будет загружаться таблица с нужного дня
                    self.fulling_tables(f'Worked Days/{sel_dat.toString("yyyy")}/'
                                        f'{sel_dat.toString("MM")}/{sel_dat.toString("dd")}')
            else:
                QtWidgets.QMessageBox.information(
                    self,
                    "Оповещение",
                    f"В данный день записей не было",
                    QtWidgets.QMessageBox.Ok)

        elif sel_dat == datetime.datetime.now():

            # todo сделать проверку в следующей версии, на созданную сегодня запись
            QtWidgets.QMessageBox.information(
                self,
                "Оповещение",
                f"Сегодняшняя запись может быть создана",
                QtWidgets.QMessageBox.Ok)
            self.fulling_tables(f'Worked Days/{sel_dat.toString("yyyy")}/'
                                f'{sel_dat.toString("MM")}/{sel_dat.toString("dd")}')

    def cur_calendar_day(self):
        """Устанавливает в качестве выбранной даты текущую"""

        self.ui.calendarWidget.setSelectedDate(datetime.datetime.now())
        sel_date = self.ui.calendarWidget.selectedDate()

        if not os.path.isdir(f'Worked Days/{sel_date.toString("yyyy")}/{sel_date.toString("MM")}'):
            os.mkdir(f'Worked Days/{sel_date.toString("yyyy")}/{sel_date.toString("MM")}')
        do_files(self, sel_date)

    # ====================================== Функции для работы с таблицей

    # Функции для работы со строками

    def add_one_str_with_table(self):
        """Добавляет одну строку со столом в таблицу"""

        table_of_tables = self.ui.tableWidget_tables

        table_of_tables.insertRow(table_of_tables.rowCount() - 1)
        table_of_tables.setCellWidget(
            table_of_tables.rowCount() - 2,
            table_of_tables.columnCount() - 3,
            my_lib_qt_1_0.do_some_comboBox(tables.statuses)).currentIndexChanged.connect(
            lambda: self.save_item(table_of_tables))

    def del_one_str_with_table(self):
        """Удаляет строку со столом из таблицы"""

        table_of_tables = self.ui.tableWidget_tables
        target_str = QtWidgets.QTableWidgetItem(
            table_of_tables.item(table_of_tables.rowCount() - 1, 1)).text()

        if (int(target_str) < 0) or (int(target_str) > table_of_tables.rowCount() - 2):
            QtWidgets.QMessageBox.information(
                self,
                "Предупреждение",
                f"№ {target_str} Вне диапазона номеров столов",
                QtWidgets.QMessageBox.Ok)
        else:
            res = QtWidgets.QMessageBox.question(
                self,
                "Подтверждение",
                f"Вы хотите удалить стол № {target_str}",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                table_of_tables.removeRow(int(target_str) - 1)

    def add_buttons_upr(self):  # todo Переделать
        """Добавляет кнопки управления"""

        table_of_tables = self.ui.tableWidget_tables

        table_of_tables.setCellWidget(table_of_tables.rowCount() - 1,
                                      table_of_tables.columnCount() - 1,
                                      self.ui.button_add_table)
        table_of_tables.setCellWidget(table_of_tables.rowCount() - 1,
                                      table_of_tables.columnCount() - 2,
                                      self.ui.button_del_table)

    # ====================================== Функции заполнения

    def fulling_tables(self, path=f'Worked Days/{datetime.datetime.now().strftime("%Y")}/'
                                  f'{datetime.datetime.now().strftime("%m")}/'
                                  f'{datetime.datetime.now().strftime("%d")}/'):

        """Функция заполняющая таблицы"""  # todo Добавить возможность выбора откуда загружать

        self.fulling_table(f'{path}_table.xml')
        # self.fulling_orders(f'/{path}_orders.xml')
        # self.fulling_times(f'/{path}_times.xml')

    def fulling_table(self, file_name):
        """Заполнение таблицы с информацией о столах"""

        tables.read_tables(file_name)
        table_of_tables = self.ui.tableWidget_tables
        my_lib_qt_1_0.table_item_change(table_of_tables)

        table_of_tables.setRowCount(len(tables.list_tables) + 1)
        # Объявление колчиства строк, по длинне списка считанных столов + доп строка

        number_str = 0
        for one_table in tables.list_tables:

            for cell in range(0, table_of_tables.columnCount()):
                table_of_tables.setItem(number_str, cell, QtWidgets.QTableWidgetItem(str(one_table[cell + 1])))

                if cell == 1:
                    table_of_tables.setCellWidget(number_str, cell, my_lib_qt_1_0.do_some_comboBox(tables.statuses))
                    # Создаю выпадющие списки

                    table_of_tables.cellWidget(number_str, cell).currentIndexChanged.connect(
                        lambda: my_lib_qt_1_0.save_CB_item(table_of_tables))
                    # Сажу на них обработчики

            number_str += 1

        self.add_buttons_upr()

        my_lib_qt_1_0.table_item_change(
            table_of_tables, lambda: my_lib_qt_1_0.save_item(table_of_tables, tables.list_tables))

        table_of_tables.selectRow(table_of_tables.rowCount() - 1)  # выбор последней строки

    def fulling_orders(self, file_name):  # todo Ещё раз всё обдумать
        pass

    def fulling_waiters(self, file_name):
        pass

    # ======================================  Функции сохранения

    def save_tables(self):
        """Функция вызывающая сохранение всех таблиц"""  # todo разделить на части
        self.save_table()
        # save_orders(self)
        # save_times(self)

    def save_table(self):
        # tables.list_tables.clear() # Очищает список столов
        my_lib_qt_1_0.just_check_list(tables.list_tables)

        table_of_tables = self.ui.tableWidget_tables

        for RowNum in range(0, table_of_tables.rowCount() - 1):

            one_table = tables.table(0, 0)
            one_table[0] = RowNum

            for ColmnNum in range(0, table_of_tables.columnCount()):

                one_table[ColmnNum + 1] = str(QtWidgets.QTableWidgetItem(table_of_tables.item(RowNum, ColmnNum)).text())

                if ColmnNum == 1:
                    one_table[ColmnNum + 1] = str(table_of_tables.cellWidget(RowNum, ColmnNum).currentIndex())

            tables.list_tables.append(one_table)

    def save_tables_inXML(self, save):
        """Функция главного меню для сохранения всех таблиц в XML"""
        save()  # единственный параметр, сама функция
        tables.save_tables_asXML()
        # tables.save_orders_asXML()
        # workers.save_time_asXML()


def do_files(main_form, date):  # todo Добавить проверку пути и создание
    res = QtWidgets.QMessageBox.question(
        main_form,
        'Подтверждение',
        f'Сегодня: {my_lib_qt_1_0.get_date(date)}.\n Вы хотите начать делать записи?',
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if res == QtWidgets.QMessageBox.Yes:
        open(f'Worked Days/{date.toString("yyyy")}/{date.toString("MM")}/{date.toString("dd")}_orders.xml',
             'tw', encoding='utf-8').close()
        open(f'Worked Days/{date.toString("yyyy")}/{date.toString("MM")}/{date.toString("dd")}_table.xml',
             'tw', encoding='utf-8').close()
        open(f'Worked Days/{date.toString("yyyy")}/{date.toString("MM")}/{date.toString("dd")}_waiters.xml',
             'tw', encoding='utf-8').close()


# ====================================== Формы для редактирования:

class TablesForm(QtWidgets.QFormLayout):
    """Форма для просмотра и редоктирования информации для столов"""

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_ui.py
        super().__init__()
        self.ui = tables_ui.Ui_Dialog()
        self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна





class ServerArestarunt:
    """Описание сервера обрабатывающего запросы от официантов"""

    def __init__(self):

        self.host = socket.gethostbyname(socket.gethostname())    # Объявляю адрес сервра по текущему айпи компьютера
        self.port = 25505

        self.waiters = []   # список клиентов

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # todo Поправить сокет

        self.sock.bind((self.host, self.port))

        self.status = "Включен"
        self.working()


    def working(self):
        #print(self.status)
        while self.status == "Включен":
            try:
                data, addr = self.sock.recvfrom(1024)

                if addr not in self.waiters:
                    self.waiters.append(addr)
                    # todo Делать проверку авторизированного пользоватля надо тут

                timeconnect = datetime.datetime.now()

                print(data.decode('utf-8'))
            except:
                self.status = "Отключен"
        self.sock.close()



if __name__ == '__main__':  # Код ниже исполняется если программа стартует с этого файла

    def main_form_start():
        """Запуск главной формы для скармливания потоку"""
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        app.setStyle('Fusion')
        window = MainForm()
        window.show()  # запуск формы main()
        sys.exit(app.exec_())

    # def server_stert():
    #     """Запуск сервера для скрамливания потоку"""
    #     serv = ServerArestarunt()

    tform = threading.Thread(target=main_form_start)
    tserv = threading.Thread(target=ServerArestarunt)

    tserv.start()
    tform.start()
