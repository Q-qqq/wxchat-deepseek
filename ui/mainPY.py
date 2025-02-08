# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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
        MainWindow.resize(331, 578)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Remove_friend_pb = QPushButton(self.centralwidget)
        self.Remove_friend_pb.setObjectName(u"Remove_friend_pb")

        self.gridLayout.addWidget(self.Remove_friend_pb, 2, 4, 1, 1)

        self.Api_key_le = QLineEdit(self.centralwidget)
        self.Api_key_le.setObjectName(u"Api_key_le")

        self.gridLayout.addWidget(self.Api_key_le, 0, 1, 1, 4)

        self.Tip_mes_pb = QPushButton(self.centralwidget)
        self.Tip_mes_pb.setObjectName(u"Tip_mes_pb")

        self.gridLayout.addWidget(self.Tip_mes_pb, 4, 1, 1, 1)

        self.Clear_history_pb = QPushButton(self.centralwidget)
        self.Clear_history_pb.setObjectName(u"Clear_history_pb")

        self.gridLayout.addWidget(self.Clear_history_pb, 4, 4, 1, 1)

        self.Start_pb = QPushButton(self.centralwidget)
        self.Start_pb.setObjectName(u"Start_pb")

        self.gridLayout.addWidget(self.Start_pb, 4, 0, 1, 1)

        self.Friends_lw = QListWidget(self.centralwidget)
        self.Friends_lw.setObjectName(u"Friends_lw")

        self.gridLayout.addWidget(self.Friends_lw, 3, 0, 1, 5)

        self.Add_friend_pb = QPushButton(self.centralwidget)
        self.Add_friend_pb.setObjectName(u"Add_friend_pb")

        self.gridLayout.addWidget(self.Add_friend_pb, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Select_all_cb = QCheckBox(self.centralwidget)
        self.Select_all_cb.setObjectName(u"Select_all_cb")

        self.gridLayout.addWidget(self.Select_all_cb, 4, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 331, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LY_chat", None))
        self.Remove_friend_pb.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u9664", None))
        self.Tip_mes_pb.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a\u8bcd", None))
        self.Clear_history_pb.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5386\u53f2\u8bb0\u5f55", None))
        self.Start_pb.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.Add_friend_pb.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"API_KEY:", None))
        self.Select_all_cb.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
    # retranslateUi

