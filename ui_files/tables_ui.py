# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tables.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(286, 97)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 60, 141, 23))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 71, 16))
        self.label.setStyleSheet(u"lable2 {\n"
"font-size: 3\n"
"font-weight: bold\n"
"} ")
        self.label.setTextFormat(Qt.RichText)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 20, 151, 31))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043d\u044f\u043b, \u043f\u0440\u0438\u043d\u044f\u043b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435:", None))
        self.label_2.setText("")
    # retranslateUi

