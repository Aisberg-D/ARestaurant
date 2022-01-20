# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
        Dialog.resize(413, 401)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_id = QLabel(Dialog)
        self.label_id.setObjectName(u"label_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_id.sizePolicy().hasHeightForWidth())
        self.label_id.setSizePolicy(sizePolicy1)
        self.label_id.setLayoutDirection(Qt.LeftToRight)
        self.label_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_id)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(300, 164))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_view_info = QPushButton(Dialog)
        self.pushButton_view_info.setObjectName(u"pushButton_view_info")
        self.pushButton_view_info.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_view_info)

        self.horizontalSpacer = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_edit_pic = QPushButton(Dialog)
        self.pushButton_edit_pic.setObjectName(u"pushButton_edit_pic")
        self.pushButton_edit_pic.setEnabled(False)
        self.pushButton_edit_pic.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_edit_pic)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_name = QLabel(Dialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_name)

        self.label_mass = QLabel(Dialog)
        self.label_mass.setObjectName(u"label_mass")
        self.label_mass.setLayoutDirection(Qt.LeftToRight)
        self.label_mass.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_mass)

        self.label_coocking_time = QLabel(Dialog)
        self.label_coocking_time.setObjectName(u"label_coocking_time")
        self.label_coocking_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_coocking_time)

        self.label_type = QLabel(Dialog)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_type)

        self.label_coocking_price = QLabel(Dialog)
        self.label_coocking_price.setObjectName(u"label_coocking_price")
        self.label_coocking_price.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_coocking_price)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_name = QLineEdit(Dialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setEnabled(False)

        self.verticalLayout_2.addWidget(self.lineEdit_name)

        self.lineEdit_mass = QLineEdit(Dialog)
        self.lineEdit_mass.setObjectName(u"lineEdit_mass")
        self.lineEdit_mass.setEnabled(False)

        self.verticalLayout_2.addWidget(self.lineEdit_mass)

        self.lineEdit_coocking_time = QLineEdit(Dialog)
        self.lineEdit_coocking_time.setObjectName(u"lineEdit_coocking_time")
        self.lineEdit_coocking_time.setEnabled(False)

        self.verticalLayout_2.addWidget(self.lineEdit_coocking_time)

        self.comboBox_type = QComboBox(Dialog)
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setEnabled(False)

        self.verticalLayout_2.addWidget(self.comboBox_type)

        self.lineEdit_price = QLineEdit(Dialog)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setEnabled(False)

        self.verticalLayout_2.addWidget(self.lineEdit_price)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_unblock = QPushButton(Dialog)
        self.pushButton_unblock.setObjectName(u"pushButton_unblock")
        self.pushButton_unblock.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.pushButton_unblock)

        self.pushButton_save = QPushButton(Dialog)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_save)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.buttonBox)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.pushButton_unblock.clicked.connect(self.lineEdit_coocking_time.show)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_id.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0442 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c ID \u043f\u0440\u043e\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043e\u0442\u0441\u0443\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.pushButton_view_info.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_edit_pic.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c.", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_mass.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0441\u0441\u0430:", None))
        self.label_coocking_time.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_type.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f:", None))
        self.label_coocking_price.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430:", None))
        self.pushButton_unblock.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

