from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wxauto import *
from ui import mainPY
from core.tipM import TipM
from pathlib import Path
from utils.deepseek import DSChat
import time
from utils import threaded

class Main(QMainWindow, mainPY.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.eventConnect()
        self.names_path = ".//resources//names.txt"
        self.key_path = ".//resources//key.txt"
        self.wx = WeChat()
        self.friends = []
        self.load()
        self.ds = DSChat()
        self.end_chat = True




    def eventConnect(self):
        self.Add_friend_pb.clicked.connect(self.addFriend)
        self.Remove_friend_pb.clicked.connect(self.removeFriend)
        self.Start_pb.clicked.connect(self.start)
        self.Tip_mes_pb.clicked.connect(self.showTip)
        self.Clear_history_pb.clicked.connect(self.clearHistory)


    def getAllFrindes(self):
        friends = self.wx.GetAllFriends()
        friends_nn = []
        for f in friends:
            friends_nn.append((f["nickname"]))
        return friends_nn

    def addFriend(self):
        name, ok = QInputDialog.getText(self, "好友或者群聊名称", "name：", text="")
        items = [self.Friends_lw.item(i).text() for i in range(self.Friends_lw.count())]
        if name and ok:
            if name not in items:
                self.Friends_lw.addItem(name)
                self.friends .append(name)
                if not self.end_chat:
                    self.wx.AddListenChat(who=name, savepic=True)
            else:
                QMessageBox.information(self, "提示","昵称已存在")
        self.save()


    def removeFriend(self):
        item = self.Friends_lw.currentItem()
        self.friends.remove(item.text())
        if not self.end_chat:
            self.wx.RemoveListenChat(item.text())
        self.Friends_lw.takeItem(self.Friends_lw.currentRow())
        self.save()


    def start(self):
        try:
            self.save()
            if self.Start_pb.text() == "开始":
                self.Start_pb.setText("停止")
                self.ds.link(self.Api_key_le.text())
                self.startChat()
            else:
                self.Start_pb.setText("开始")
                self.endChat()
        except Exception as ex:
            QMessageBox.information(self, "提示", str(ex))

    @threaded
    def startChat(self):
        self.end_chat = False
        for i in self.friends:
            self.wx.AddListenChat(who=i, savepic=True)
        while True:
            if self.end_chat:
                return
            try:
                msgs = self.wx.GetListenMessage()
                for chat in msgs:
                    who = chat.who  # 获取聊天窗口名（人或群名)
                    if who in self.friends:
                        one_msgs = msgs[chat]  # 获取消息内容

                        for msg in one_msgs:
                            if msg.type == "friend":
                                content = msg.content  # 获取消息内容
                                chat.SendMsg(self.ds.chat(who, content))

                time.sleep(2)
            except Exception as es:
                pass


    def endChat(self):
        self.end_chat = True

    def showTip(self):
        item, ok = QInputDialog.getItem(self,"选择好友","好友：", ["默认"]+self.friends,0,False)
        if item and ok:
            tm =TipM(self,item,self.ds.db)
            tm.show()

    def clearHistory(self):
        if self.Select_all_cb.isChecked():
            for friend in self.friends:
                self.ds.db.delete_history(friend)
        else:
            friend = self.Friends_lw.currentItem().text()
            self.ds.db.delete_history(friend)

    def save(self):
        with open(self.names_path, "w") as f:
            f.write(str.join("\n",self.friends).rstrip())
        if self.Api_key_le.text():
            with open(self.key_path,"w") as f:
                f.write(self.Api_key_le.text())

    def load(self):
        if Path(self.names_path).exists():
            with open(self.names_path, "r") as f:
                names = f.readlines()
                names = [name.strip() for name in names]
            self.Friends_lw.clear()
            self.Friends_lw.addItems(names)
            self.friends = names
        if Path(self.key_path).exists():
            with open(self.key_path) as f:
                api_key = f.read()
            if api_key:
                self.Api_key_le.setText(api_key.strip())

    def closeEvent(self, event:QCloseEvent):
        self.ds.db.close()



