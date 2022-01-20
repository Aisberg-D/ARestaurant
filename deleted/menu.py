
import sys  # s

statuses = ('Не готовиться', 'Можем приготовть', 'Действует особое предложение')

class punkt():

    '''Описание пункта меню'''

    def __init__(self):
        self.id = 0
        self.type = None
        self.name = None
        self.price = 0
        self.mass = 0
        self.cooking_time = 0
        self.status = [0]
        self.comment = None

    def __add__(self, other):
        return punkt(self.id + other, self.name, self.price, self.mass, self.cooking_time, self.comment)

    def __del__(self):
        return "Пункт меню ", self.name, " был удалён."

    def edit(self, id, type, name, price, mass, cooking_time, status, comment):
        self.id = id
        self.type = type
        self.name = name
        self.price = price
        self.mass = mass
        self.cooking_time = cooking_time
        self.status = status
        self.comment = comment