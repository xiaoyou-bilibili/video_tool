import sys
import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileDialog

from ui.main import Ui_MainWindow
from core.ffmpeg import FfmpegBase, execute_ffmpeg_cmd, get_ext
from core.util import remove_file
from threading import Thread, Lock


# 自定义信号，用于更新UI操作
class MySign(QtCore.QObject):
    # 当前进度
    current_progress = QtCore.Signal(int)
    # 总进度
    global_progress = QtCore.Signal(int)
    # 日志
    log = QtCore.Signal(str)
    # 状态栏
    status = QtCore.Signal(str)


class MainWindow(QtWidgets.QMainWindow):  # 继承QMainWindow
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._sign = MySign()
        self._action_bind()
        self._sign_bind()

    # 控件事件绑定
    def _action_bind(self):
        # 启动转码按钮
        self._ui.btn_start.clicked.connect(self.start)
        # 清空
        self._ui.action_clear.triggered.connect(self.clear_items)
        # 添加文件
        self._ui.action_add.triggered.connect(self.add_files)

    def _set_current_progress(self, progress: int):
        self._ui.progress_current.setValue(progress)

    def _set_global_progress(self, progress: int):
        self._ui.progress_global.setValue(progress)

    def _add_log_info(self, text: str):
        self._ui.text_edit_log.append("[{}]{}".format(time.strftime("%H:%M:%S", time.localtime()), text))

    def _set_status_info(self, text: str):
        self._ui.statusbar.showMessage(text)

    # 控件的信号绑定
    def _sign_bind(self):
        self._sign.current_progress.connect(self._set_current_progress)
        self._sign.global_progress.connect(self._set_global_progress)
        self._sign.log.connect(self._add_log_info)
        self._sign.status.connect(self._set_status_info)

    # 清空所有文件
    def clear_items(self):
        self._ui.list_files.clear()

    # 设置当前进度
    def set_process(self, process: int, frame: int, fps: float, speed: str):
        self._sign.current_progress.emit(process)
        self._sign.status.emit("frame={} fps={} speed={}".format(frame, fps, speed))

    # 设置底部提示信息
    def set_status(self, text: str):
        self._sign.status.emit(text)

    # 设置总进度
    def set_global_process(self, index: int, size: int):
        self._sign.global_progress.emit(int(float(index + 1) / float(size) * 100))

    # 添加日志
    def add_log(self, text: str):
        self._sign.log.emit(text)

    # 手动添加文件
    def add_files(self):
        file_dialog = QFileDialog()
        file_list = file_dialog.getOpenFileNames(self, "待操作的文件")  # 选择目录，返回选中的路径
        self._ui.list_files.add_path(file_list[0])

    # 获取ffmpeg的基本参数
    def get_base_option(self) -> FfmpegBase:
        hard = self._ui.combo_hard.currentText()
        if hard == "none":
            hard = ""
        return FfmpegBase(hard, self._ui.spin_thread_num.value())

    # 获取用户选择的操作
    def get_user_option(self):
        return self._ui.tab_option.currentIndex()

    # 视频转码
    def video_convert(self, path: str, name: str):
        base = self.get_base_option()
        # 获取视频编码和音频编码
        video_format = self._ui.combo_video.currentText()
        audio_format = self._ui.combo_auido.currentText()
        # 提取新的名称
        new_name = "new_{}".format(name)
        ext = name.split(".")[-1]
        # 判断字符串名称
        if get_ext(video_format) != "":
            new_name = new_name.replace(ext, get_ext(video_format))
        # 编码判断
        if video_format == "none":
            video_format = "-vn"
        else:
            video_format = "-c:v {}".format(video_format)
        if audio_format == "none":
            audio_format = "-cn"
        else:
            audio_format = "-c:a {}".format(audio_format)
        # 转换前把旧的文件删除
        new_path = path.replace(name, new_name)
        remove_file(new_path)
        self.add_log("开始转换 {}...".format(name))
        execute_ffmpeg_cmd(base.hard, base.thread, path, new_path,
                           "{} {}".format(video_format, audio_format), self.set_process)
        self.add_log("{} 转换完成!".format(name))

    # 批量操作
    def bath_option(self, option):
        self.add_log("开始任务")
        # 获取所有路径
        all_path = self._ui.list_files.get_all_path()
        # 按钮禁用
        self._ui.btn_start.setDisabled(True)
        size = len(all_path)
        for index, path in enumerate(all_path):
            print(index, path)
            # 提取出文件名
            name = path.split("/")[-1]
            if option == 1:
                self.video_convert(path, name)
            # 转换完毕后设置一下总体进度
            self.set_global_process(index, size)
        self._ui.btn_start.setDisabled(False)
        self.add_log("任务完成!")
        self.set_status("")

    def start(self):
        index = self.get_user_option()
        Thread(target=self.bath_option, args=(index,)).start()


# 显示主窗口
def show_main_window():
    app = QtWidgets.QApplication([])
    # 启动主窗口
    window = MainWindow()
    window.show()
    window.setWindowTitle("视频小工具 by:小游")
    sys.exit(app.exec_())
