# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(562, 588)
        Form.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(Form)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_num_of_cur_order = QLabel(Form)
        self.label_num_of_cur_order.setObjectName(u"label_num_of_cur_order")

        self.horizontalLayout.addWidget(self.label_num_of_cur_order)

        self.horizontalSpacer = QSpacerItem(395, 35, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_update = QPushButton(Form)
        self.pushButton_update.setObjectName(u"pushButton_update")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        self.pushButton_update.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton_update)

        self.label_ikon_2 = QLabel(Form)
        self.label_ikon_2.setObjectName(u"label_ikon_2")

        self.horizontalLayout.addWidget(self.label_ikon_2)

        self.label_cur_user = QLabel(Form)
        self.label_cur_user.setObjectName(u"label_cur_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_cur_user.sizePolicy().hasHeightForWidth())
        self.label_cur_user.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_cur_user)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setStyleSheet(u"")
        self.tab_menu = QWidget()
        self.tab_menu.setObjectName(u"tab_menu")
        self.gridLayout = QGridLayout(self.tab_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView_menu = QTableView(self.tab_menu)
        self.tableView_menu.setObjectName(u"tableView_menu")

        self.gridLayout.addWidget(self.tableView_menu, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_menu, "")
        self.tab_cur_order = QWidget()
        self.tab_cur_order.setObjectName(u"tab_cur_order")
        self.gridLayout_2 = QGridLayout(self.tab_cur_order)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView_cur_order = QTableView(self.tab_cur_order)
        self.tableView_cur_order.setObjectName(u"tableView_cur_order")

        self.gridLayout_2.addWidget(self.tableView_cur_order, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_cur_order, "")
        self.tab_today_orders = QWidget()
        self.tab_today_orders.setObjectName(u"tab_today_orders")
        self.gridLayout_3 = QGridLayout(self.tab_today_orders)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView_today_orders = QTableView(self.tab_today_orders)
        self.tableView_today_orders.setObjectName(u"tableView_today_orders")
        self.tableView_today_orders.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.tableView_today_orders, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_today_orders, "")

        self.gridLayout_6.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy3)
        self.pushButton_add.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton_add)

        self.pushButton_info = QPushButton(Form)
        self.pushButton_info.setObjectName(u"pushButton_info")
        sizePolicy3.setHeightForWidth(self.pushButton_info.sizePolicy().hasHeightForWidth())
        self.pushButton_info.setSizePolicy(sizePolicy3)
        self.pushButton_info.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton_info)

        self.pushButton_fin = QPushButton(Form)
        self.pushButton_fin.setObjectName(u"pushButton_fin")
        sizePolicy3.setHeightForWidth(self.pushButton_fin.sizePolicy().hasHeightForWidth())
        self.pushButton_fin.setSizePolicy(sizePolicy3)
        self.pushButton_fin.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton_fin)

        self.label_summ = QLabel(Form)
        self.label_summ.setObjectName(u"label_summ")
        sizePolicy3.setHeightForWidth(self.label_summ.sizePolicy().hasHeightForWidth())
        self.label_summ.setSizePolicy(sizePolicy3)
        self.label_summ.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.label_summ.setTextFormat(Qt.AutoText)
        self.label_summ.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_summ)


        self.gridLayout_6.addLayout(self.verticalLayout, 1, 1, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e\u043a\u043d\u043e \u043e\u0444\u0438\u0446\u0438\u0430\u043d\u0442\u0430", None))
        self.label_num_of_cur_order.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0437\u0430\u043a\u0430\u0437:", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c", None))
        self.label_ikon_2.setText(QCoreApplication.translate("Form", u"\u0422\u0443\u0442 \u0431\u044b\u043b\u0430 \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0430", None))
        self.label_cur_user.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0422\u0443\u0442 \u0432\u0430\u0449\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0424\u0418\u041e \u044e\u0437\u0435\u0440\u0430, </p><p>\u043d\u043e \u0440\u0430\u0437 \u043d\u0435\u0442, \u0447\u0442\u043e \u0442\u043e \u043f\u043e\u0448\u043b\u043e \u043d\u0435 \u0442\u0430\u043a</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_menu), QCoreApplication.translate("Form", u"\u041c\u0435\u043d\u044e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cur_order), QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0437\u0430\u043a\u0430\u0437", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_today_orders), QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0430\u0437\u044b \u043e\u0444\u0438\u0446\u0438\u0430\u043d\u0442\u0430", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u0412 \n"
" \u0417\u0410\u041a\u0410\u0417", None))
        self.pushButton_info.setText(QCoreApplication.translate("Form", u"\u041e\u041f\u0418\u0421\u0410\u041d\u0418\u0415", None))
        self.pushButton_fin.setText(QCoreApplication.translate("Form", u"\u0420\u0410\u0421\u0427\u0418\u0422\u0410\u0422\u042c", None))
        self.label_summ.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u0422\u0443\u0442 \u0434\u043e\u043b\u0436\u043d\u0430 </p><p align=\"center\">\u0431\u044b\u0442\u044c \u0438\u0442\u043e\u0433\u043e\u0432\u0430\u044f </p><p align=\"center\">\u0441\u0443\u043c\u043c\u0430</p></body></html>", None))
    # retranslateUi

