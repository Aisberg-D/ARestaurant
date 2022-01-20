#!/urs/bin/python3
# -*- coding: utf-8 -*-

# Общие переменные

headers_workers = ("ID", "ФИО", "Возраст", "Обслуживаемые столы", "Смена", "Общая сумма заказов")

list_workers = []


class worker:
    '''Описание работника в организации'''

    def __init__(self, id, fio, age, phone_number, time):
        self.id = id
        self.fio = fio
        self.age = age
        self.phone_number = phone_number
        self.time = time

    def __add__(self, other):
        return worker(self.id + other, self.fio, self.age, self.phone_number, self.time)

    def __del__(self): # todo Доделать!!!
        return "Сотрудник удалён"

    def __call__(self, id, fio, age, phone_number, time):  # вместо edit
        self.id = id
        self.fio = fio
        self.age = age
        self.phone_number = phone_number
        self.time = time


class waiter(worker):
    '''Описание официанта зависит от worker'''

    def __init__(self, nums_tables, sum, id, fio, age, phone_number, time):
        super().__init__(id, fio, age, phone_number, time)
        self.nums_tables = nums_tables
        self.sum = sum

    def add_table(self, other):
        self.nums_tables += other

    def del_table(self, number_for_del):
        self.nums_tables.remove(int(number_for_del))
        return 'Стол удалён из списка отвественности официанта'
