#!/urs/bin/python3
# -*- coding: utf-8 -*-

from xml.dom import minidom

import my_lib_qt_1_0

try:
    import xml.etree.cElementTree as ET
except ImportError:  # Запретное заклятие для более быстрой работы XML
    import xml.etree.ElementTree as ET

import time

# Для заказов

headers_time_orders = ('№ заказа', '№ стола', 'Время заказа', 'Перечень заказа', 'Цена заказа')
headers_cur_order = ('Наименование', 'Масса', 'Количество', 'Цена за порцию', 'Общая цена')

list_orders = []

# Для меню

statuses = ('Не готовиться', 'Можем приготовть', 'Действует особое предложение')

item_types = {
    0: 'Дополнительное',
    1: 'Закуска',
    2: 'Салат',
    3: 'Горячее',
    4: 'Напиток'
}

# Для пунктов

list_items = []
# item = ()
actual_items_count = 0

headers_items = ('Наименование', 'Доступность', 'Масса', 'Время приготовления', 'Тип', 'Цена')


class Order(dict):
    """Описание еденичного заказа"""

    def __init__(self):
        self.id = 0
        self.date_time = time.strftime('%H.%M.%d.%m.%Y')
        self.do_order_waiter = None
        self.list_check = [[], []]
        self.price = self.get_price()
        dict.__init__(self,
                      id=self.id,
                      date_time=self.date_time,
                      do_order_waiter=self.do_order_waiter,
                      list_check=self.list_check,
                      price=self.get_price())
        # todo изменить
        # self.id = 0
        # self.date_time = time.strftime('%H.%M.%d.%m.%Y')
        # self.do_order_waiter = None
        # self.list_check = [[], []]
        # self.price = self.get_price()

    # def __del__(self):  # todo ДОДЕЛАТЬ!!!
    #     return f'Заказ удалён {self[0]}'

    # def __getitem__(self, index):
    #     cur_order = [self.id, self.date_time, self.do_order_waiter, self.list_check, self.price]
    #     return cur_order[index]
    #
    # def __setitem__(self, key, value):
    #     cur_order = [self.id, self.date_time, self.do_order_waiter, self.list_check]
    #     cur_order[key] = value
    #     self(cur_order[0], cur_order[1], cur_order[2], cur_order[3])
    #
    # def __call__(self, id, time_order, do_order_waiter, list_check):  # вместо edit
    #     self.id = id
    #     self.date_time = time_order
    #     self.do_order_waiter = do_order_waiter
    #     self.list_check = list_check
    #
    # def to_json(self):
    #     return self.__dict__

    def get_price(self):
        pass
        sum = 0
        for i in range(0, len(self.list_check[0])):
            sum = + self.list_check[0][i][6] * self.list_check[1][i]
        return sum


class Menu:
    """Представляет собой лист меню"""

    def __init__(self):
        self.dop = []
        self.piece = []
        self.salat = []
        self.hot = []
        self.drink = []
        self.menu = (self.dop, self.piece, self.salat, self.hot, self.drink)

    def __del__(self):  # todo ДОДЕЛАТЬ!!!
        return f'Меню удалено'

    def __add__(self, other):
        self.list.append(other)

    # def __call__(self, list_menu):  # вместо edit
    #    self.list = list_menu


# class item:
#     """Описание одного блюда или напитка"""
#
#     def __init__(self):
#         self.id = 0
#         self.status = 'actual'
#         self.name = None
#         self.mass = None
#         self.coocking_time = None
#         self.type = item_types[0]
#         self.price = 0
#         self.info = None
#         self.img_name = None
#
#     def __del__(self):  # todo ДОДЕЛАТЬ!!!
#         return f'{self.type}, а именно: "{self.name}" удалён'
#
#     def __getitem__(self, index):
#         cur_item = [self.id, self.status, self.name, self.mass, self.coocking_time,
#                     self.type, self.price, self.info, self.img_name]
#         return cur_item[index]
#
#     def __setitem__(self, key, value):
#         cur_item = [self.id, self.status, self.name, self.mass, self.coocking_time,
#                     self.type, self.price, self.info, self.img_name]
#         cur_item[key] = value
#         self(cur_item[0], cur_item[1], cur_item[2], cur_item[3], cur_item[4], cur_item[5],
#              cur_item[6], cur_item[7], cur_item[8])
#
#
#     def __call__(self, id, status, name, mass, coocking_time, type, info, img_name, price):  # вместо edit
#         self.id = id
#         self.status = status
#         self.name = name
#         self.mass = mass
#         self.coocking_time = coocking_time
#         self.type = type # my_lib_qt_1_0.get_key_from_dict(type, item_types)
#         self.price = price
#         self.info = info
#         self.img_name = img_name


def read_items(file_tables="XML_files/items/item.xml"):
    """Чтение XML файла пунктов/items"""

    list_items.clear()
    cur_time_session = ET.parse(f"{file_tables}").getroot()

    actual_items_count = 0

    for one_item in cur_time_session.findall("item"):
        # list_items.append(item())
        # list_items[-1](one_item.attrib["id"], one_item.attrib["status"], one_item.attrib["name"],
        #             str(one_item[0].text), str(one_item[1].text), str(one_item[2].text),
        #             str(one_item[3].text), str(one_item[4].text), str(one_item[5].text))

        item = (one_item.attrib["id"], one_item.attrib["name"], one_item.attrib["status"],
                str(one_item[0].text), str(one_item[1].text), str(one_item[2].text),
                str(one_item[3].text), str(one_item[4].text), str(one_item[5].text))
        list_items.append(item)
        if one_item.attrib["status"] == "actual":
            actual_items_count += 1
    if actual_items_count != int(cur_time_session.attrib["num"]):
        print('В данных жопа')


def save_items(file_tables="XML_files/items/item.xml"):
    """Запись XML файла items/пунктов"""

    cur_time_session = ET.Element("tables")

    for element in list_items:
        ET.SubElement(cur_time_session, "item", id=str(element.id), name=str(element.name), status=str(element.status))

        # создание дочерних суб-элементов.
        ET.SubElement(cur_time_session[-1], "mass").text = str(element.mass)
        ET.SubElement(cur_time_session[-1], "coocking_time").text = str(element.coocking_time)
        ET.SubElement(cur_time_session[-1], "type").text = str(element.type)
        ET.SubElement(cur_time_session[-1], "info").text = str(element.info)
        ET.SubElement(cur_time_session[-1], "img_name").text = str(element.img_name)
        ET.SubElement(cur_time_session[-1], "price").text = str(element.price)
        # if element.Order != None:
        #     ET.SubElement(cur_time_session[-1], "Order").text = str(element.Order)
        # else:
        #     ET.SubElement(cur_time_session[-1], "Order").text = "None"

    with open(f"{file_tables}", "w") as tree:
        xml_strings = ET.tostring(cur_time_session).decode()
        xml_stringss = minidom.parseString(xml_strings).toprettyxml()
        tree.write(xml_stringss)
        tree.close()
