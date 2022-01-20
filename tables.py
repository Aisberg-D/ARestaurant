#!/urs/bin/python3
# -*- coding: utf-8 -*-

from xml.dom import minidom

try:
    import xml.etree.cElementTree as ET
except ImportError:  # Запретное заклятие для более быстрой работы XML
    import xml.etree.ElementTree as ET

# statuses = {
#    '-1' : 'Не обслуживается',
#    '0' : 'Свободен',
#    '1' : 'Занят',
# }


# Общие переменные

# Для столиков

headers_tables = ('Посадочные места', 'Статус стола', 'Текущий заказ', 'Ведущий офицант')
statuses = ('Не обслуживается', 'Свободен', 'Занят')

list_tables = []


class table:
    '''Описание единичного стола для клиентов'''

    def __init__(self, number, sit_p):
        self.number = number
        self.sit_p = sit_p
        self.status = statuses[0]
        self.order = None
        self.cur_waiter = None

    def __add__(self, other):
        return table(self.number + other, self.sit_p, self.status, self.order, self.cur_waiter)

    def __del__(self):  # todo С этим надо что то сделать
        return 'Стол удалён'

    def __getitem__(self, index):
        cur_table = [self.number, self.sit_p, self.status, self.order, self.cur_waiter]
        return cur_table[index]

    def __setitem__(self, key, value):
        cur_table = [self.number, self.sit_p, self.status, self.order, self.cur_waiter]
        cur_table[key] = value
        self(cur_table[0], cur_table[1], cur_table[2], cur_table[3], cur_table[4])

    def __str__(self):  # Может пригодиться, возвращает строчные значения по индексу
        return "{0} {1} {2} {3} {4}".format(self.number, self.sit_p, self.status, self.order, self.cur_waiter)

    def __call__(self, number, sit_p, status, order, cur_waiter):  # вместо edit
        self.number = number
        self.sit_p = sit_p
        self.status = status
        self.order = order
        self.cur_waiter = cur_waiter

    #    def test(self):
    #        print("Номер стола:" + str(self.number + 1), "Посадочных мест:" + str(self.sit_p), "Статус:" + str(self.status), "Офицант:" + self.cur_waiter)

    def cur_order(**kwargs):
        pass

    # Работа с XML


def read_tables(file_tables="XML_files/tables_test.xml"):
    '''Чтение XML файла таблиц'''

    list_tables.clear()
    cur_time_session = ET.parse(f"{file_tables}").getroot()

    for one_table in cur_time_session.findall("table"):
        list_tables.append(table(0, 0))
        list_tables[-1](one_table.attrib["number"], one_table.attrib["sit_p"],
                        str(one_table[0].text), str(one_table[1].text), str(one_table[2].text))


def save_tables_asXML(file_tables="XML_files/tables_test.xml"):
    '''Создание файла XML столов'''

    cur_time_session = ET.Element("tables")

    for element in list_tables:

        ET.SubElement(cur_time_session, "table", number=str(element.number), sit_p=str(element.sit_p))

        # создание дочерних суб-элементов.
        ET.SubElement(cur_time_session[-1], "status").text = str(element.status)
        if element.Order != None:
            ET.SubElement(cur_time_session[-1], "Order").text = str(element.Order)
        else:
            ET.SubElement(cur_time_session[-1], "Order").text = "None"
        if element.cur_waiter != None:
            ET.SubElement(cur_time_session[-1], "cur_waiter").text = str(element.cur_waiter)
        else:
            ET.SubElement(cur_time_session[-1], "cur_waiter").text = "None"

    with open(f"{file_tables}", "w") as tree:
        xml_strings = ET.tostring(cur_time_session).decode()
        xml_stringss = minidom.parseString(xml_strings).toprettyxml()
        # ET.ElementTree(cur_time_session).write(tree)
        tree.write(xml_stringss)
        tree.close()
    # cur_time_doc = ET.tostring(cur_time_session)
    # xml_tables = open("XML_files/tables_test.xml", "w")
    # xml_tables.write(cur_time_doc)