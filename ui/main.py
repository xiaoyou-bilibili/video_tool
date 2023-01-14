# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

from ui.components import QListDrag

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 539)
        self.action_add = QAction(MainWindow)
        self.action_add.setObjectName(u"action_add")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_files = QListDrag(self.centralwidget)
        self.list_files.setObjectName(u"list_files")
        self.list_files.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout.addWidget(self.list_files)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, -1, -1, -1)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.combo_hard = QComboBox(self.groupBox)
        self.combo_hard.addItem("")
        self.combo_hard.addItem("")
        self.combo_hard.addItem("")
        self.combo_hard.addItem("")
        self.combo_hard.addItem("")
        self.combo_hard.setObjectName(u"combo_hard")

        self.gridLayout_2.addWidget(self.combo_hard, 0, 1, 1, 1)

        self.spin_thread_num = QSpinBox(self.groupBox)
        self.spin_thread_num.setObjectName(u"spin_thread_num")
        self.spin_thread_num.setMaximum(20)
        self.spin_thread_num.setValue(4)

        self.gridLayout_2.addWidget(self.spin_thread_num, 0, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(80, 50))

        self.gridLayout.addWidget(self.btn_start, 1, 2, 1, 1)

        self.tab_option = QTabWidget(self.centralwidget)
        self.tab_option.setObjectName(u"tab_option")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.combo_sub = QComboBox(self.tab)
        self.combo_sub.addItem("")
        self.combo_sub.setObjectName(u"combo_sub")

        self.gridLayout_3.addWidget(self.combo_sub, 1, 2, 1, 1)

        self.check_sub_mp4 = QCheckBox(self.tab)
        self.check_sub_mp4.setObjectName(u"check_sub_mp4")

        self.gridLayout_3.addWidget(self.check_sub_mp4, 1, 3, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 4, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)

        self.tab_option.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.combo_video = QComboBox(self.tab_2)
        self.combo_video.addItem("")
        self.combo_video.addItem("")
        self.combo_video.addItem("")
        self.combo_video.addItem("")
        self.combo_video.addItem("")
        self.combo_video.addItem("")
        self.combo_video.addItem("")
        self.combo_video.setObjectName(u"combo_video")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.combo_video)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.combo_auido = QComboBox(self.tab_2)
        self.combo_auido.addItem("")
        self.combo_auido.addItem("")
        self.combo_auido.addItem("")
        self.combo_auido.setObjectName(u"combo_auido")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_auido)


        self.verticalLayout_6.addLayout(self.formLayout)

        self.tab_option.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.combo_extra_audio = QComboBox(self.tab_3)
        self.combo_extra_audio.addItem("")
        self.combo_extra_audio.setObjectName(u"combo_extra_audio")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.combo_extra_audio)


        self.verticalLayout_7.addLayout(self.formLayout_3)

        self.tab_option.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.edit_real_addr = QLineEdit(self.tab_4)
        self.edit_real_addr.setObjectName(u"edit_real_addr")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.edit_real_addr)

        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.radio_save_img = QRadioButton(self.tab_4)
        self.radio_save_img.setObjectName(u"radio_save_img")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.radio_save_img)


        self.verticalLayout_8.addLayout(self.formLayout_4)

        self.tab_option.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_9 = QVBoxLayout(self.tab_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_11 = QLabel(self.tab_5)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.edit_whisper = QLineEdit(self.tab_5)
        self.edit_whisper.setObjectName(u"edit_whisper")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.edit_whisper)


        self.verticalLayout_9.addLayout(self.formLayout_5)

        self.tab_option.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tab_option, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.group_status = QGridLayout()
        self.group_status.setObjectName(u"group_status")

        self.verticalLayout.addLayout(self.group_status)

        self.group_log = QGroupBox(self.centralwidget)
        self.group_log.setObjectName(u"group_log")
        self.group_log.setMinimumSize(QSize(0, 0))
        self.group_log.setMaximumSize(QSize(16777215, 150))
        self.group_log.setFlat(False)
        self.group_log.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.group_log)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.text_edit_log = QTextEdit(self.group_log)
        self.text_edit_log.setObjectName(u"text_edit_log")
        self.text_edit_log.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.text_edit_log)


        self.verticalLayout.addWidget(self.group_log)

        self.from_progress = QFormLayout()
        self.from_progress.setObjectName(u"from_progress")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.from_progress.setWidget(0, QFormLayout.LabelRole, self.label)

        self.progress_current = QProgressBar(self.centralwidget)
        self.progress_current.setObjectName(u"progress_current")
        self.progress_current.setValue(0)

        self.from_progress.setWidget(0, QFormLayout.FieldRole, self.progress_current)


        self.verticalLayout.addLayout(self.from_progress)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.progress_global = QProgressBar(self.centralwidget)
        self.progress_global.setObjectName(u"progress_global")
        self.progress_global.setValue(0)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.progress_global)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_add)
        self.menu.addAction(self.action_clear)
        self.menu_2.addAction(self.action_info)

        self.retranslateUi(MainWindow)

        self.tab_option.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u914d\u7f6e", None))
        self.combo_hard.setItemText(0, QCoreApplication.translate("MainWindow", u"none", None))
        self.combo_hard.setItemText(1, QCoreApplication.translate("MainWindow", u"cuda", None))
        self.combo_hard.setItemText(2, QCoreApplication.translate("MainWindow", u"dxva2", None))
        self.combo_hard.setItemText(3, QCoreApplication.translate("MainWindow", u"qsv", None))
        self.combo_hard.setItemText(4, QCoreApplication.translate("MainWindow", u"d3d11va", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u7801\u7ebf\u7a0b:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u52a0\u901f:", None))
        self.radioButton.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210\u540e\u5173\u673a:", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.combo_sub.setItemText(0, QCoreApplication.translate("MainWindow", u"ass", None))

        self.check_sub_mp4.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51famp4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u7c7b\u578b:", None))
        self.tab_option.setTabText(self.tab_option.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5185\u5d4c\u5b57\u5e55", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f16\u7801:", None))
        self.combo_video.setItemText(0, QCoreApplication.translate("MainWindow", u"libx264", None))
        self.combo_video.setItemText(1, QCoreApplication.translate("MainWindow", u"h264_nvenc", None))
        self.combo_video.setItemText(2, QCoreApplication.translate("MainWindow", u"libx265", None))
        self.combo_video.setItemText(3, QCoreApplication.translate("MainWindow", u"flv", None))
        self.combo_video.setItemText(4, QCoreApplication.translate("MainWindow", u"gif", None))
        self.combo_video.setItemText(5, QCoreApplication.translate("MainWindow", u"copy", None))
        self.combo_video.setItemText(6, QCoreApplication.translate("MainWindow", u"none", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u7f16\u7801:", None))
        self.combo_auido.setItemText(0, QCoreApplication.translate("MainWindow", u"aac", None))
        self.combo_auido.setItemText(1, QCoreApplication.translate("MainWindow", u"copy", None))
        self.combo_auido.setItemText(2, QCoreApplication.translate("MainWindow", u"none", None))

        self.tab_option.setTabText(self.tab_option.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u8f6c\u6362", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u683c\u5f0f:", None))
        self.combo_extra_audio.setItemText(0, QCoreApplication.translate("MainWindow", u"mp3", None))

        self.tab_option.setTabText(self.tab_option.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u63d0\u53d6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5730\u5740:", None))
        self.edit_real_addr.setText(QCoreApplication.translate("MainWindow", u"http://192.168.1.10:8209", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u7247:", None))
        self.radio_save_img.setText("")
        self.tab_option.setTabText(self.tab_option.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u8d85\u5206", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5730\u5740:", None))
        self.edit_whisper.setText(QCoreApplication.translate("MainWindow", u"http://192.168.1.10:8210", None))
        self.tab_option.setTabText(self.tab_option.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u751f\u6210", None))
        self.group_log.setTitle(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u65e5\u5fd7", None))
        self.text_edit_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8fdb\u5ea6:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\u8fdb\u5ea6:", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

