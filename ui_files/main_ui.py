# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(1, 0))
        MainWindow.setStyleSheet(u"QPushButton {\n"
"	font-weight: bold;\n"
"}\\")
        self.fulling = QAction(MainWindow)
        self.fulling.setObjectName(u"fulling")
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        self.view_items = QAction(MainWindow)
        self.view_items.setObjectName(u"view_items")
        self.view_current_menu = QAction(MainWindow)
        self.view_current_menu.setObjectName(u"view_current_menu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_last_day = QLabel(self.centralwidget)
        self.label_last_day.setObjectName(u"label_last_day")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_last_day.sizePolicy().hasHeightForWidth())
        self.label_last_day.setSizePolicy(sizePolicy2)
        self.label_last_day.setMinimumSize(QSize(0, 20))

        self.verticalLayout.addWidget(self.label_last_day)

        self.pushButton_test = QPushButton(self.centralwidget)
        self.pushButton_test.setObjectName(u"pushButton_test")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_test.sizePolicy().hasHeightForWidth())
        self.pushButton_test.setSizePolicy(sizePolicy3)
        self.pushButton_test.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.pushButton_test)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.comboBox_curtime = QComboBox(self.centralwidget)
        self.comboBox_curtime.setObjectName(u"comboBox_curtime")
        sizePolicy3.setHeightForWidth(self.comboBox_curtime.sizePolicy().hasHeightForWidth())
        self.comboBox_curtime.setSizePolicy(sizePolicy3)
        self.comboBox_curtime.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.comboBox_curtime)

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy4)
        self.calendarWidget.setMaximumSize(QSize(500, 500))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)

        self.verticalLayout.addWidget(self.calendarWidget)

        self.pushButton_curdate = QPushButton(self.centralwidget)
        self.pushButton_curdate.setObjectName(u"pushButton_curdate")
        sizePolicy3.setHeightForWidth(self.pushButton_curdate.sizePolicy().hasHeightForWidth())
        self.pushButton_curdate.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton_curdate)

        self.label_itog = QLabel(self.centralwidget)
        self.label_itog.setObjectName(u"label_itog")
        sizePolicy2.setHeightForWidth(self.label_itog.sizePolicy().hasHeightForWidth())
        self.label_itog.setSizePolicy(sizePolicy2)
        self.label_itog.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.label_itog)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(395, 35, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_ikon = QLabel(self.centralwidget)
        self.label_ikon.setObjectName(u"label_ikon")

        self.horizontalLayout.addWidget(self.label_ikon)

        self.label_cur_user = QLabel(self.centralwidget)
        self.label_cur_user.setObjectName(u"label_cur_user")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_cur_user.sizePolicy().hasHeightForWidth())
        self.label_cur_user.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.label_cur_user)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab_orders = QWidget()
        self.tab_orders.setObjectName(u"tab_orders")
        self.gridLayout_3 = QGridLayout(self.tab_orders)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_orders = QTableWidget(self.tab_orders)
        self.tableWidget_orders.setObjectName(u"tableWidget_orders")
        self.tableWidget_orders.setStyleSheet(u"QtableWidget{\n"
"height: 100%;\n"
"width: 100%\n"
"}")

        self.gridLayout_3.addWidget(self.tableWidget_orders, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_orders, "")
        self.tab_tables = QWidget()
        self.tab_tables.setObjectName(u"tab_tables")
        self.gridLayout = QGridLayout(self.tab_tables)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_tables = QTableWidget(self.tab_tables)
        self.tableWidget_tables.setObjectName(u"tableWidget_tables")
        self.tableWidget_tables.setStyleSheet(u"QtableWidget{\n"
"height: 100%;\n"
"width: 100%\n"
"}")

        self.gridLayout.addWidget(self.tableWidget_tables, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_tables, "")
        self.tab_waiters = QWidget()
        self.tab_waiters.setObjectName(u"tab_waiters")
        self.gridLayout_2 = QGridLayout(self.tab_waiters)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_waiters = QTableWidget(self.tab_waiters)
        self.tableWidget_waiters.setObjectName(u"tableWidget_waiters")

        self.gridLayout_2.addWidget(self.tableWidget_waiters, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_waiters, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 995, 21))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.edit = QMenu(self.menubar)
        self.edit.setObjectName(u"edit")
        self.info = QMenu(self.menubar)
        self.info.setObjectName(u"info")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.info.menuAction())
        self.file.addAction(self.fulling)
        self.file.addAction(self.save)
        self.file.addSeparator()
        self.file.addAction(self.view_items)
        self.file.addAction(self.view_current_menu)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fulling.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.view_items.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0431\u043b\u044e\u0434", None))
        self.view_current_menu.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u043c\u0435\u043d\u044e", None))
        self.label_last_day.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0445 \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.pushButton_test.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041a\u0415", None))
        self.pushButton_curdate.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0434\u0435\u043d\u044c", None))
        self.label_itog.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u043b \u0431\u044b\u0442\u044c \u0438\u0442\u043e\u0433 \u0434\u043d\u044f", None))
        self.label_ikon.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u0431\u044b\u043b\u0430 \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0430", None))
        self.label_cur_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0422\u0443\u0442 \u0432\u0430\u0449\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0424\u0418\u041e \u044e\u0437\u0435\u0440\u0430, </p><p>\u043d\u043e \u0440\u0430\u0437 \u043d\u0435\u0442, \u0447\u0442\u043e \u0442\u043e \u043f\u043e\u0448\u043b\u043e \u043d\u0435 \u0442\u0430\u043a</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_orders), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tables), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0438\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_waiters), QCoreApplication.translate("MainWindow", u"\u041e\u0444\u0438\u0446\u0438\u0430\u043d\u0442\u044b", None))
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.edit.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.info.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
    # retranslateUi

