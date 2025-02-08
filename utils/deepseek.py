from openai import OpenAI
import  re
from utils.db import DB
from pathlib import Path

class DSChat:
    def __init__(self):
        self.db = DB()
        self.client = None


    def link(self, api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    def clean_response(self, content):
        content = re.sub(r'\[.*?\]', '', content, flags=re.DOTALL)
        # 去除Markdown加粗和倾斜标记
        content = re.sub(r'\*\*\*', '', content)
        content = re.sub(r'\*\*', '', content)
        content = re.sub(r'\*', '', content)
        # 去除行首的#和-
        content = re.sub(r'^\t*[#-]+', '', content, flags=re.MULTILINE)

        content = re.sub(r'\n+', '\n', content)
        content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL)
        return content.strip()

    def getTip(self, user):
        tip = self.db.get_tip(user)
        if not tip:
            tip = self.db.get_tip("默认")
        return tip


    def chat(self, user, prompt):
        if self.client is None:
            return "deepseek未连接"
        try:
            self.db.add_history(user, "user", prompt)
            mes =[]
            mes += self.getTip(user)
            history = self.db.get_history(user)
            if len(history) > 20:
                self.db.delete_history(user)
                return "对话次数已达上限，请开始下一轮对话"
            mes += history
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages = mes,
            )
            content = response.choices[0].message.content
            content = self.clean_response(content)
            self.db.add_history(user, "assistant", content)
            return content
        except Exception as e:
            return f"Error: {e}\n抱歉，我遇到了一个错误，请稍后再试。"

