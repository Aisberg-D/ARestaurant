import numpy as np
from PyQt5.QtWidgets import QApplication, QTableView, QWidget, QGridLayout, QPushButton, \
    QTreeView, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

mass = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], float)

#import order_menu_item

class Table(QWidget):
    def __init__(self, data=None, parent=None):
        super().__init__()
        self.model = QStandardItemModel()
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(1)
        #self.model.setHorizontalHeaderLabels(order_menu_item.headers_items)
        self.btnLoad = QPushButton("Load")
        self.btnCalc = QPushButton("Calc")
        self.btnGet = QPushButton('Get')
        self.btnLoad.clicked.connect(self.load_data)
        self.btnCalc.clicked.connect(self.calc)
        self.btnGet.clicked.connect(self.get_data)
        grid = QGridLayout(self)
        grid.setContentsMargins(1, 1, 1, 1)
        grid.addWidget(self.table, 0, 0, 4, 4)
        grid.addWidget(self.btnLoad, 4, 0, 1, 1)
        grid.addWidget(self.btnCalc, 4, 1, 1, 1)
        grid.addWidget(self.btnGet, 4, 3, 1, 1)
        self.data = data

    def load_data(self):
        rows = len(self.data)
        cols = len(self.data[0])
        for row in range(rows):
            for col in range(cols):
                item = QStandardItem(str(self.data[row][col]))
                self.model.setItem(row, col, item)

    def calc(self):
        for i in range(len(self.data[0])):
            self.data[0][i] *= 100
            self.load_data()

    def get_data(self):
        rows = self.model.rowCount()
        cols = self.model.columnCount()
        out = [[self.model.item(i, j).text() for j in range(cols)] for i in range(rows)]
        print(out)


if __name__ == "__main__":
    app = QApplication([])
    w = Table(mass)
    w.show()
    app.exec_()