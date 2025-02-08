# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tipUI.ui'
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
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Tip_mes_te = QTextEdit(Form)
        self.Tip_mes_te.setObjectName(u"Tip_mes_te")

        self.gridLayout.addWidget(self.Tip_mes_te, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(145, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.OK_pb = QPushButton(Form)
        self.OK_pb.setObjectName(u"OK_pb")

        self.gridLayout.addWidget(self.OK_pb, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(144, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u63d0\u793a\u8bcd", None))
        self.OK_pb.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

