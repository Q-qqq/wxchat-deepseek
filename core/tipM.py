from ui import tipPY

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pathlib import Path

class TipM(QWidget, tipPY.Ui_Form):
    def __init__(self,parent,user_id, db, f=Qt.Dialog):
        super().__init__(parent, f)
        self.setupUi(self)
        self.eventConnect()
        self.setWindowTitle(user_id)
        self.friend = user_id
        self.db = db
        self.load()

    def eventConnect(self):
        self.OK_pb.clicked.connect(self.okClicked)

    def load(self):
        tip = self.db.get_tip(self.friend)
        if tip:
            self.Tip_mes_te.setPlainText(tip[0]["content"])

    def okClicked(self):
        self.db.add_tip(self.friend, self.Tip_mes_te.toPlainText().strip())
        self.close()