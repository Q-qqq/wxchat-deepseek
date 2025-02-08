import sqlite3
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class DB:
    def __init__(self):
        self.mes_path = './/resources//ds_msgs.db'
        self.conn = sqlite3.connect(self.mes_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.initHistory()
        self.initTip()

    def initHistory(self):
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS history (
                    user_id TEXT,
                    role TEXT,
                    content TEXT
                    )
                    ''')
        self.conn.commit()

    def initTip(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS tips (
                            user_id TEXT UNIQUE,
                            tip TEXT
                            )
                            ''')
        self.conn.commit()

    def add_history(self,user_id, role, content):
        self.cursor.execute('INSERT INTO history (user_id, role, content) VALUES (?, ?, ?)', (user_id, role, content))
        self.conn.commit()


    def get_history(self, user_id):
        # 查询数据库
        self.cursor.execute('SELECT role, content FROM history WHERE user_id=? ORDER BY rowid', (user_id,))
        history = self.cursor.fetchall()

        # 将结果转换为字典列表
        history_dict = [{'role': row[0], 'content': row[1]} for row in history]

        return history_dict

    def delete_history(self, user_id):
        self.cursor.execute("DELETE FROM history WHERE user_id=?", (user_id,))
        self.conn.commit()


    def add_tip(self, user_id, tip):
        try:
            self.cursor.execute('INSERT INTO tips (user_id, tip) VALUES (?, ?)', (user_id, tip))
        except:
            self.cursor.execute("UPDATE tips SET tip=? WHERE user_id=?", (tip, user_id))
        self.conn.commit()

    def get_tip(self, user_id):
        self.cursor.execute("SELECT * FROM tips WHERE user_id=?", (user_id,))
        row = self.cursor.fetchone()
        tip_dict = [{"role":"system", "content":row[1]}] if row else []
        return tip_dict

    def delete_tip(self, user_id):
        self.cursor.execute("DELETE FROM tips WHERE user_id=?", (user_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()