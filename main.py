from core.mainM import Main
from PySide2.QtWidgets import *


# 按间距中的绿色按钮以运行脚本。
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_ui = Main()
    main_ui.show()
    sys.exit(app.exec_())

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
