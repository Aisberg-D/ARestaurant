#!/urs/bin/python3
# -*- coding: utf-8 -*-
import os.path

from PySide2 import QtWidgets, QtCore, QtGui


# ======================================================================================== Функции элементов интерфейса


def do_some_comboBox(some_list, some_comboBox=None):
    """Создание и заполнение QComboBox on_changed"""

    if some_comboBox == None:
        some_comboBox = QtWidgets.QComboBox()
    for elemen in some_list:
        some_comboBox.addItem(str(elemen))

    return some_comboBox


def do_some_button(text, some_button=None, do = None):
    """Создание, обзывание QButton и приклепление обработчика"""

    if some_button == None:
        some_button = QtWidgets.QPushButton()
        some_button.setText(text)
    if do == None:
        some_button.clicked.connect(lambda: do_nothing())
    else:
        some_button.clicked.connect(lambda: do())

    return some_button


def set_column_size_as_content(table):
    """Установление ширины стобцов по контенту"""

    table.horizontalHeader().setMinimumSectionSize(0)
    try:
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    except:
        table.horizontalHeader().setSectionResizeMode(3)


def set_row_size_as_content(table):
    """Установление высоты строк по контенту"""

    table.verticalHeader().setMinimumSectionSize(0)
    try:
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    except:
        table.verticalHeader().setSectionResizeMode(3)


def fulling_table(some_table, some_list, *some_functions, upr_str=False):
    """Заполнение таблиц"""

    if len(some_functions) == 0:
        show_msg("А как таблицу то заполнять?")
    else:

        table_item_change(some_list)  # Садит обработчик таблицы или пустой обработчик

        if len(some_functions) >= 2:
            some_functions[1]()

        if upr_str == True:  # Объявление колчиства строк, по длинне списка + доп строка при необходимости
            some_table.setRowCount(len(some_list) + 1)
        else:
            some_table.setRowCount(len(some_list))

        number_str = 0

        for element in some_list:

            for cell in range(0, some_table.columnCount()):
                some_table.setItem(number_str, cell, QtWidgets.QTableWidgetItem(str(element[cell])))

                some_functions[0]()

            number_str += 1

        if len(some_functions) >= 4:
            some_functions[3]()

        if len(some_functions) >= 3:
            table_item_change(some_table, some_functions[2]())


def save_tables(some_table, some_list, some_class, *some_functions):
    """Считывание таблиц"""

    if len(some_functions) == 0:
        show_msg("А как таблицу то считывать?")
    else:

        just_check_list(some_list)

        rowcount = some_table.rowCount()
        if type(some_table[-1][-1]).isinstanse(QtWidgets.QTableWidget.cellWidget):  # Проверяю строку управления
            rowcount -= 1

        for RowNum in range(0, rowcount):

            if len(some_functions) >= 2:
                some_functions[1]()

            for ColmnNum in range(0, some_table.columnCount()):
                some_class[ColmnNum] = str(
                    QtWidgets.QTableWidgetItem(some_table.ui.tableWidget_tables.item(RowNum, ColmnNum)).text())

                some_functions[0]()

            some_list.append(some_class)

def save_item(table, some_list):
    """Достаёт элементы из таблицы сохраняя их значение"""

    if table.currentRow() < len(some_list):
        if table.currentColumn() == 1:
            some_list[table.currentRow()][table.currentColumn()] = str(table.cellWidget(
                table.currentRow(), table.currentColumn()).currentIndex()
                                                                       )
        else:
            some_list[table.currentRow()][table.currentColumn()] = str(QtWidgets.QTableWidgetItem(
                table.item(table.currentRow(), table.currentColumn())).text())
    # print(str(QtWidgets.QTableWidgetItem(table.item(table.currentRow(), table.currentColumn())).text()))

def save_CB_item(table):
    """Достаёт элементы из таблицы сохраняя их значение если они QCombobox""" #todo Объеденить с обычной функцией

    if table.cellWidget(table.currentRow(), table.currentColumn()) != None:
        print(str(table.cellWidget(table.currentRow(), table.currentColumn()).currentText()))


def table_item_change(table, *some_function):
    """Функция для добавления обработчика к таблице"""

    if len(some_function) != 0:
        table.itemChanged.connect(lambda: some_function[0]())
    else:
        table.itemChanged.connect(lambda: do_nothing())


def just_check_list(some_list, *do_some_function):
    """Проверки листа, если длина равна нулю, то выполняется функция, если что то есть, очищается"""

    if len(some_list) == 0:
        do_some_function[0]()
    else:
        some_list.clear()

    # ============================================================================================ Шедевральные функции


def do_nothing():
    """Ничего не делает, просто ничего не делает. Шедевр, правда?"""
    pass


def get_key_from_dict(word, some_dict):
    """Возвращает ключ по значению из словаря"""
    for key in some_dict:
        if word == some_dict[key]:
            return key


def file_check(name_file):
    """Если файла нет создаёт"""

    if not os.path.isfile(name_file):
        createing_file = (f'{name_file}', 'tw')
        createing_file.close()

def upr_str_check(num_upr_str, select):
    """Проверяет является ли выделенная строка управляющей сравнивая с её текущим номером"""
    pass


def get_date(date):
    """Возвращает дату в текстовом формате, кроме года"""

    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    # print(date.toString()

    try:
        date_list = date.toString('dd.MM.yyyy').split('.')
    except:
        date_list = date.split('-')

    return (day_list[int(date_list[0]) - 1] + ' ' +
            month_list[int(date_list[1]) - 1] + ' ' +
            date_list[2] + ' года')




    # ================================================================================================= Форма сообщений


def show_msg(msg="Что то прям ваще пошло не так", title="Непредвиденная ошибка", style=None, *some_function):
    """Настраиваемое окно сообщения"""""

    msgBox = QtWidgets.QMessageBox()
    if style != None:
        msgBox.setStyle(style)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

    msgBox.setText(msg)
    msgBox.setWindowTitle(title)
    msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)

    msgBox.show()

    if len(some_function) != 0:
        msgBox.buttonClicked.connect(lambda: do_it())

    if msgBox.Ok:
        msgBox.exec_()

    def do_it(some_function):
        some_function[0]()
        msgBox.exec_()
