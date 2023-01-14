from PySide6.QtWidgets import QListWidget


# 可拖拽的列表
class QListDrag(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        paths = []
        for url in urls:
            # 这里只添加文件
            if url.scheme() == 'file':
                paths.append(str(url.path())[1:])
        self.add_path(paths)

    # 获取所有的路径
    def get_all_path(self):
        text_list = []
        # 获取所有文件
        for i in range(self.count()):
            text_list.append(self.item(i).text())
        return text_list

    # 添加路径，包括判重处理
    def add_path(self, file_paths: list):
        text_list = self.get_all_path()
        for path in file_paths:
            if path not in text_list:
                self.addItem(path)
