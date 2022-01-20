import numpy as np

from PyQt5.QtWidgets import (QApplication, QTableView, QTreeView,
                             QMainWindow, QWidget, QGridLayout, QPushButton, QMenu)
from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex)


class NpModel(QAbstractTableModel):
    def __init__(self, data=np.array([[]])):
        super().__init__()
        self.npdata = data

    def rowCount(self, index=QModelIndex()):
        return len(self.npdata)

    def columnCount(self, index=QModelIndex()):
        return len(self.npdata[0])

    def data(self, index, role):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        val = self.npdata[index.row()][index.column()]
        return str(round(val, 4))

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole: return None
        if orientation == Qt.Vertical:
            return 'Строка ' + str(section)
        else:
            return 'Столбец ' + str(section)

    def set(self, arr=np.array([[]])):
        self.beginResetModel()
        self.npdata = arr
        self.endResetModel()
        self.layoutChanged.emit()

    def get(self):
        return self.npdata


class NpTable(QMainWindow):
    def __init__(self, data=np.array([[]]), parent=None):
        super().__init__()
        self.model = NpModel()
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.horizontalHeader().setSectionResizeMode(1)
        self.btnLoad = QPushButton("Reload")
        self.btnCalc = QPushButton("Calc")
        self.btnGet = QPushButton('Get')
        self.btnLoad.clicked.connect(self.reload)
        self.btnCalc.clicked.connect(self.calc)
        self.btnGet.clicked.connect(self.get_data)
        wgt = QWidget()
        grid = QGridLayout(wgt)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.view, 0, 0, 4, 4)
        grid.addWidget(self.btnLoad, 4, 0, 1, 1)
        grid.addWidget(self.btnCalc, 4, 1, 1, 1)
        grid.addWidget(self.btnGet, 4, 3, 1, 1)
        self.setCentralWidget(wgt)
        self.load(data)

    def reload(self):
        self.model.set(self.data.copy())

    def load(self, data=np.array([[]])):
        self.data = data
        self.model.set(data.copy())

    def calc(self):
        rows = self.model.rowCount()
        cols = self.model.columnCount()
        for i in range(rows):
            for j in range(cols):
                self.model.npdata[i][j] /= (j + 2)
        self.model.layoutChanged.emit()

    def get_data(self):
        print(repr(self.model.get()))

    def contextMenuEvent(self, event):
        indexes = [(i.row(), i.column()) for i in self.view.selectionModel().selectedIndexes()]
        self.statusBar().showMessage(str(indexes))
        mnu = QMenu()
        mnu.addAction('x10').setObjectName('calc10')
        mnu.addAction('x100').setObjectName('calc100')
        pos = self.view.mapToGlobal(event.pos())
        ret = mnu.exec_(pos)
        if ret:
            num = 0
            obj = ret.objectName()
            if obj == 'calc10':
                num = 10
            elif obj == 'calc100':
                num = 100
            if num:
                for ind in indexes: self.model.npdata[ind] *= num
        index = self.model.index(-1, -1)
        self.view.setCurrentIndex(index)
        self.model.layoutChanged.emit()
        self.statusBar().showMessage('')


mass = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], float)

if __name__ == "__main__":
    app = QApplication([])
    w = NpTable()
    w.load(mass)
    w.resize(600, 400)
    w.move(0, 0)
    w.show()
    app.exec_()