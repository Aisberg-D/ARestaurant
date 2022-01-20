#!/urs/bin/python3
# -*- coding: utf-8 -*-
import requests
from PySide2 import QtWidgets, QtCore, QtGui

import sys  # sys нужна для передачи argv в QApplication
import os  # библиотека для доступа к системным параметрам
import datetime  # библиотека для работы с датой
import threading
import json

from ui_files import menu_ui  # конвертированные файлы интерфейса

import my_lib_qt_1_0

import order_menu_item


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = menu_ui.Ui_Form()
        self.ui.setupUi(self)
        self.number_of_upr_str = 0
        self.numeric_order = 1

        # ====================================== Таблица меню

        self.ui.tableView_menu.setModel(QtGui.QStandardItemModel())
        self.ui.tableView_menu.model().setHorizontalHeaderLabels(order_menu_item.headers_items)
        self.ui.tableView_menu.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # Выбор 1го элемента
        self.ui.tableView_menu.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Выбор строкой
        self.ui.tableView_menu.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Запрет на редактирование
        my_lib_qt_1_0.set_column_size_as_content(self.ui.tableView_menu)

        # ====================================== Таблица текущего заказа

        self.do_cur_order_table()

        # ====================================== Таблица списка заказов

        self.ui.tableView_today_orders.setModel(QtGui.QStandardItemModel())
        self.ui.tableView_today_orders.model().setHorizontalHeaderLabels(order_menu_item.headers_time_orders)
        self.ui.tableView_today_orders.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableView_today_orders.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_today_orders.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        my_lib_qt_1_0.set_column_size_as_content(self.ui.tableView_today_orders)
        my_lib_qt_1_0.set_row_size_as_content(self.ui.tableView_today_orders)

        self.list_orders = []
        self.add_order()
        self.ui.tableView_today_orders.selectRow(0)

        # Создание управляющей строки и обработчик строк

        self.ui.tableView_today_orders.selectionModel().selectionChanged.connect(lambda: self.update_cur_order())
        self.ui.tableView_today_orders.model().setRowCount(self.ui.tableView_today_orders.model().rowCount() + 1)
        self.ui.tableView_today_orders.setSpan(1, 0, 1, 5)
        self.ui.tableView_today_orders.setIndexWidget(self.ui.tableView_today_orders.model().index(
            self.ui.tableView_today_orders.model().rowCount() - 1, 0),
            EditListOrders(self))

        # self.ui.tableView_today_orders.selectionChanged(lambda: save_current_order(self))

        # Обработчики кнопок

        self.ui.pushButton_update.clicked.connect(lambda: self.update_tables())

        self.ui.pushButton_add.clicked.connect(lambda: self.add_item())
        self.ui.pushButton_info.clicked.connect(lambda: self.info_item_view())
        self.ui.pushButton_fin.clicked.connect(lambda: self.fin_order())

    def fulling_menu(self):
        """Заполняет таблицу с меню"""

        order_menu_item.read_items()  # todo тут буду разделять на подключение к хосту

        self.ui.tableView_menu.model().setRowCount(len(order_menu_item.list_items))
        # Объявление колчиства строк

        number_str = 0
        for one_item in order_menu_item.list_items:
            for cell in range(0, self.ui.tableView_menu.model().columnCount()):

                if one_item[cell + 1] == 'None':
                    self.ui.tableView_menu.model().setItem(number_str, cell, QtGui.QStandardItem('Отсуствует'))
                else:
                    if cell == self.ui.tableView_menu.model().columnCount() - 1:
                        self.ui.tableView_menu.model().setItem(number_str, cell, QtGui.QStandardItem(str(one_item[-1])))
                    else:
                        self.ui.tableView_menu.model().setItem(number_str, cell,
                                                               QtGui.QStandardItem(str(one_item[cell + 1])))
            number_str += 1

    def do_cur_order_table(self):
        """Прорисовка таблицы текущего заказа"""
        self.ui.tableView_cur_order.setModel(QtGui.QStandardItemModel())
        self.ui.tableView_cur_order.model().setHorizontalHeaderLabels(order_menu_item.headers_cur_order)
        self.ui.tableView_cur_order.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)  # Выбор отсуствует
        self.ui.tableView_cur_order.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        my_lib_qt_1_0.set_column_size_as_content(self.ui.tableView_cur_order)

    def update_cur_order(self):
        """Обновляет все данные текущего заказа"""
        self.ui.tableView_cur_order.model().clear()
        self.do_cur_order_table()
        self.view_list_cur_items()
        self.row_reprice()
        self.end_reprice()
        # if self.ui.tableView_cur_order.model().columnCount() != 0:
        #     self.end_reprice()

    def add_order(self):
        """Добавляет новую строку и пустой заказ в лист обрабатывающихся заказов"""

        table = self.ui.tableView_today_orders
        tablem = self.ui.tableView_today_orders.model()

        tablem.insertRow(0)
        tablem.setItem(0, 0, QtGui.QStandardItem(str(self.numeric_order)))
        table.setIndexWidget(tablem.index(
            0, 1),
            my_lib_qt_1_0.do_some_comboBox(list(range(1, 11))))
        table.setIndexWidget(tablem.index(
            0, 3),
            my_lib_qt_1_0.do_some_button("Просмотреть список", do=lambda: self.view_list_cur_items()))
        self.number_of_upr_str += 1
        self.numeric_order += 1
        self.list_orders.append(order_menu_item.Order())

    def del_order(self):
        """Удаляет выбранный обрабатывающийся заказ"""
        table = self.ui.tableView_today_orders
        tablem = self.ui.tableView_today_orders.model()
        selected = table.selectedIndexes()[0].row()

        if self.number_of_upr_str != table.selectedIndexes()[0].row():
            if selected != self.number_of_upr_str:
                tablem.removeRow(selected)
                self.list_orders.remove(self.list_orders[self.number_of_upr_str - 1 - selected])
                # todo Учесть обратный порядок
                if tablem.rowCount() == 1:
                    res = QtWidgets.QMessageBox.question(
                        self,
                        'Уведомление',
                        f'Это был последний обрабатывающийся заказ. Создать новый?',
                        QtWidgets.QMessageBox.Yes,
                        QtWidgets.QMessageBox.No)
                    if res == QtWidgets.QMessageBox.Yes:
                        self.add_order()
                self.number_of_upr_str -= 1

    def update_tables(self):
        """Обновляет все таблицы на форме"""
        self.fulling_menu()
        fulling_orders(self, self.list_orders)  # todo Подправить вызывваемую функцию
        self.update_cur_order()

    def view_list_cur_items(self):
        try:
            selected = self.ui.tableView_today_orders.selectedIndexes()[0].row()
            cur_order = self.list_orders[self.number_of_upr_str - 1 - selected]  # todo Учесть обратный порядок
            self.selected_order_view(cur_order)
            self.ui.tabWidget.setCurrentIndex(1)  # Переключение на вкладку текущего заказа
        except:
            my_lib_qt_1_0.do_nothing()

    def selected_order_view(self, cur_order):
        """Прорисовывает таблицу с выбранными в текущем заказе элементами"""

        table = self.ui.tableView_cur_order
        tablem = self.ui.tableView_cur_order.model()

        if len(cur_order.list_check[1]) != 0:
            for item in range(0, len(cur_order.list_check[1])):
                tablem.setRowCount(tablem.rowCount() + 1)
                tablem.setItem(tablem.rowCount() - 1, 0, QtGui.QStandardItem(str(cur_order.list_check[0][item][1])))  # Название

                tablem.setItem(tablem.rowCount() - 1, 1, QtGui.QStandardItem(str(cur_order.list_check[0][item][3])))  # Масса

                if (cur_order.do_order_waiter != '') or (cur_order.do_order_waiter is None):
                    table.setIndexWidget(tablem.index(tablem.rowCount() - 1, 2),
                                         EditCountItem(self, cur_order.list_check[1][item]))
                else:
                    table.setIndexWidget(tablem.index(tablem.rowCount() - 1, 2),
                                         QtWidgets.QLabel(cur_order.list_check[1][item]))

                tablem.setItem(tablem.rowCount() - 1, 3, QtGui.QStandardItem(str(cur_order.list_check[0][item][8])))
                # Цена

                tablem.setItem(tablem.rowCount() - 1, 4, QtGui.QStandardItem(str(cur_order.list_check[0][item][8])))
                # Повторение строки для первой цены по предмету

    def row_reprice(self):
        """Пересчёт построчно каждого предмета (item) в текущем заказе"""

        table = self.ui.tableView_cur_order
        tablem = self.ui.tableView_cur_order.model()

        if tablem.rowCount() != 0:
            for row in range(0, self.number_of_upr_str):
                selected = self.ui.tableView_today_orders.selectedIndexes()[0].row()
                try:
                    cur_count_item = int(table.indexWidget(tablem.index(row, 2)).count_label.text())
                    self.list_orders[self.number_of_upr_str - 1 - selected].list_check[1][row] = cur_count_item
                    sum_one_item = cur_count_item * int(tablem.item(row, 3).text())
                    tablem.setItem(row, 4, QtGui.QStandardItem(str(sum_one_item)))
                except:
                    my_lib_qt_1_0.do_nothing()



    def end_reprice(self):
        """Финальный пересчёт суммы текущего заказа"""

        sum_all_items = 0

        table = self.ui.tableView_cur_order
        tablem = self.ui.tableView_cur_order.model()

        for row in range(0, tablem.rowCount()):
            sum_all_items += int(tablem.item(row, 4).text())
        self.ui.label_summ.setText(f'Итого: {sum_all_items} р')

        # return cur_price = order_menu_item.Order.get_price()

    def info_item_view(self):
        """Выводит сообщение с описание итема из блюда или меню"""
        selected = order_menu_item.list_items[self.ui.tableView_menu.selectedIndexes()[0].row()]
        QtWidgets.QMessageBox.about(self, selected[1], selected[7])
        # my_lib_qt_1_0.show_msg(selected[7], selected[1], style=self.style()) #todoooo Разобраться со стилями

    def add_item(self):
        """Добавить элемент в таблицу текущего заказа и в сам соотвествующий заказ"""

        table = self.ui.tableView_cur_order
        tablem = self.ui.tableView_cur_order.model()

        selected = order_menu_item.list_items[self.ui.tableView_menu.selectedIndexes()[0].row()]
        tablem.setRowCount(tablem.rowCount() + 1)
        index_cur_order = self.ui.tableView_today_orders.selectedIndexes()[0].row()
        if index_cur_order < self.number_of_upr_str:
            cur_order = self.list_orders[self.number_of_upr_str - 1 - index_cur_order]
            # todo Учесть обратный порядок, добавить исключение

        if selected is None:
            res = QtWidgets.QMessageBox.question(
                self,
                'Уведомление',
                f'Отсуствует выделение',
                QtWidgets.QMessageBox.Ok)
            if res == QtWidgets.QMessageBox.Ok:
                my_lib_qt_1_0.do_nothing()
        else:
            tablem.setItem(tablem.rowCount() - 1, 0, QtGui.QStandardItem(str(selected[1])))  # Название

            tablem.setItem(tablem.rowCount() - 1, 1, QtGui.QStandardItem(str(selected[3])))  # Масса

            table.setIndexWidget(tablem.index(tablem.rowCount() - 1, 2), EditCountItem(self))

            tablem.setItem(tablem.rowCount() - 1, 3, QtGui.QStandardItem(str(selected[8])))  # Цена

            tablem.setItem(tablem.rowCount() - 1, 4, QtGui.QStandardItem(str(selected[8])))  # Костыль
            print(cur_order)
            cur_order.list_check[0].append(selected)
            cur_order.list_check[1].append(1)

        self.row_reprice()
        self.end_reprice()

        # table.indexWidget(tablem.index(tablem.rowCount() - 1, 2)).count_label.changeEvent(self.row_reprice())
        # my_lib_qt_1_0.table_item_change(tablem, self.end_reprice())  # Обработчик

    def del_item(self):
        """Удаляет элемент из таблицы и текущего заказа"""

        table = self.ui.tableView_cur_order
        tablem = self.ui.tableView_cur_order.model()
        index_cur_order = self.ui.tableView_today_orders.selectedIndexes()[0].row()
        if index_cur_order < self.number_of_upr_str:
            cur_order = self.list_orders[self.number_of_upr_str - 1 - index_cur_order]

        for row in range(0, self.number_of_upr_str):
            if tablem.rowCount() != 0:
                cur_count_item = int(table.indexWidget(tablem.index(row, 2)).count_label.text())
                if cur_count_item < 1:
                    tablem.removeRow(row)
                    cur_order.list_check[0].pop(row)
                    cur_order.list_check[1].pop(row)


class EditListOrders(QtWidgets.QWidget):
    """Группа кнопок для добавления или удаления заказа"""

    def __init__(self, form: Ui_Form):  # Мост в другой класс
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.form = form  # Переменная моста

        self.pushButton_add = QtWidgets.QPushButton('Добавить заказ')
        self.pushButton_add.clicked.connect(lambda: form.add_order())
        self.pushButton_del = QtWidgets.QPushButton('Удалить заказ')
        self.pushButton_del.clicked.connect(lambda: form.del_order())

        layout.addWidget(self.pushButton_add)
        layout.addWidget(self.pushButton_del)
        layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

        self.setLayout(layout)


class EditCountItem(QtWidgets.QWidget):
    """Группа кнопок для редактирования количества предмета (item) в текущем заказе"""

    def __init__(self, form: Ui_Form, init_count=1):  # Мост в другой класс
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.form = form  # Переменная моста

        self.pushButton_minus = QtWidgets.QPushButton('-')
        self.pushButton_minus.setFixedWidth(23)
        self.pushButton_minus.clicked.connect(lambda: self.minus_item())
        self.count_label = QtWidgets.QLabel(str(init_count))
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)  # Выравнивание по центру
        self.pushButton_plus = QtWidgets.QPushButton('+')
        self.pushButton_plus.setFixedWidth(23)
        self.pushButton_plus.clicked.connect(lambda: self.plus_item())

        layout.addWidget(self.pushButton_minus)
        layout.addWidget(self.count_label)
        layout.addWidget(self.pushButton_plus)

        self.setLayout(layout)

    def plus_item(self):
        cur = int(self.count_label.text())
        if cur + 1 > 99:
            my_lib_qt_1_0.do_nothing()
        else:
            self.count_label.setText(f'{cur + 1}')
            self.form.row_reprice()
            self.form.end_reprice()

    def minus_item(self):
        cur = int(self.count_label.text())
        if cur <= 1:
            res = QtWidgets.QMessageBox.warning(
                self,
                'Подтверждение',
                f'Вы действительно хотите удалить элемент из заказа?',
                QtWidgets.QMessageBox.Yes,
                QtWidgets.QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                self.count_label.setText(f'{cur - 1}')
                self.form.del_item()
        else:
            self.count_label.setText(f'{cur - 1}')
            self.form.row_reprice()
            self.form.end_reprice()


def fulling_orders(ui_form, orders):
    """Проверят существование папки, где хранятся обрабаотываемые данные"""
    cur_date = datetime.datetime.now().strftime('%d-%m-%Y')
    if not os.path.isdir(f'XML_files'):
        os.mkdir(f'XML_files')
    do_file(cur_date, ui_form, orders)


def do_file(cur_date, ui_form, orders):
    """Создаёт файл для записи текущих заказов или загружает данные из файла сделанные ранее сегодня"""
    if os.path.isfile(f'XML_files/{cur_date.split("-")[2]}-{cur_date.split("-")[1]}-cur_waiter_orders.json'):
        with open(f'XML_files/{cur_date.split("-")[2]}-{cur_date.split("-")[1]}-cur_waiter_orders.json', 'w') as file:
            json.dump(orders, file, indent=1)
            send(orders)# todo Добавить постоянную проверку на сервере
    else:
        # todo Сюда нужно вставить проверку списка заказов на сервере
        res = QtWidgets.QMessageBox.question(
            ui_form,
            'Подтверждение',
            f'Сегодня: {my_lib_qt_1_0.get_date(cur_date)}.\n Вы хотите начать делать записи?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            with open(f'XML_files/{cur_date.split("-")[2]}-{cur_date.split("-")[1]}-cur_waiter_orders.json',
                      'w') as file:
                json.dump(file, orders, indent=1)  # todo Добавить имя официанта в название файла


# def send(massage):
#     """Отправляет сообщения на сервер"""
#     response = requests.get('192.168.0.198:25564') # todo Вынести в настройки
#     if response:
#         print(response)
#     requests.post(massage)


if __name__ == '__main__':  # Код ниже исполняется если программа стартует с этого файла

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Fusion')
    window = Ui_Form()  # запуск функции main()
    window.show()
    sys.exit(app.exec_())
