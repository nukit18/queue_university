import asyncio

from db_api.quick_cmd import get_ids_bakalavr, get_description, get_name_and_num_win
from pages import start_win, final_win
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(round(1440/1.8), round(1024/1.8))
        MainWindow.setMinimumSize(QtCore.QSize(round(1440/1.8), round(1024/1.8)))
        MainWindow.setMaximumSize(QtCore.QSize(round(1440/1.8), round(1024/1.8)))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(round(426/1.8), 0, round(588/1.8), round(186/1.8)))
        self.label.setStyleSheet("position: absolute;\n"
                                 "width: 588px;\n"
                                 "height: 186px;\n"
                                 "left: 426px;\n"
                                 "top: 0px;\n"
                                 "\n"
                                 "font-family: Roboto;\n"
                                 "font-style: normal;\n"
                                 "font-weight: normal;\n"
                                 "font-size: 53px;\n"
                                 "line-height: 112px;\n"
                                 "display: flex;\n"
                                 "align-items: center;\n"
                                 "\n"
                                 "color: #000000;\n"
                                 "")
        self.label.setObjectName("label")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(round(20/1.8), round(30/1.8), round(131/1.8), round(51/1.8)))
        self.back_btn.setStyleSheet("background: #ff0000;\n"
                                    "border-radius: 38px;\n"
                                    "position: absolute;\n"
                                    "width: 58px;\n"
                                    "height: 18px;\n"
                                    "left: 10px;\n"
                                    "top: 10px;\n"
                                    "\n"
                                    "font-family: Roboto;\n"
                                    "font-style: normal;\n"
                                    "font-weight: normal;\n"
                                    "font-size: 20px;\n"
                                    "line-height: 112px;\n"
                                    "display: flex;\n"
                                    "align-items: center;\n"
                                    "\n"
                                    "color: #FFFFFF;")
        self.back_btn.setObjectName("back_btn")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, round(150/1.8), round(1440/1.8), round(874/1.8)))
        self.scrollArea.setMinimumSize(QtCore.QSize(round(1440/1.8), round(874/1.8)))
        self.scrollArea.setMaximumSize(QtCore.QSize(round(1440/1.8), round(874/1.8)))
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
                                      "            border: 0px solid #c6c6c6;\n"
                                      "            background: transparent;\n"
                                      "            width: 25px;    \n"
                                      "            margin: 0px 0px 0px 0px;\n"
                                      "        }\n"
                                      "QScrollBar:horizontal {\n"
                                      "            border: 0px solid #c6c6c6;\n"
                                      "            background: transparent;\n"
                                      "            height: 13px;    \n"
                                      "            margin: 0px 0px 0px 0px;\n"
                                      "        }\n"
                                      "        QScrollBar::handle {\n"
                                      "            background: #c6c6c6;\n"
                                      "            border: 0px solid 1;\n"
                                      "            border-radius: 6px;\n"
                                      "        }\n"
                                      "        QScrollBar::add-line:vertical {\n"
                                      "            height: 0px;\n"
                                      "            subcontrol-position: bottom;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "        QScrollBar::sub-line:vertical {\n"
                                      "            height: 0 px;\n"
                                      "            subcontrol-position: top;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "        QScrollBar::add-line:horizontal {\n"
                                      "            width: 0px;\n"
                                      "            subcontrol-position: right;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "        QScrollBar::sub-line:horizontal {\n"
                                      "            width: 0 px;\n"
                                      "            subcontrol-position: left;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        loop = asyncio.get_event_loop()
        scroll_height = (len(loop.run_until_complete(get_ids_bakalavr())) - 0) * 400
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, round(1413/1.8), round(scroll_height/1.8)))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, round(scroll_height/1.8)))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.array_btns = []

        self.one = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.one)
        self.two = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.two)
        self.three = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.three)
        self.four = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.four)
        self.five = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.five)
        self.six = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.six)
        self.seven = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.seven)
        self.eight = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.eight)
        self.nine = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.nine)
        self.ten = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.ten)
        self.eleven = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.eleven)
        self.twelve = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.twelve)
        self.thirteen = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.thirteen)
        self.fourteen = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.fourteen)
        self.fifteen = QtWidgets.QPushButton(self.frame)
        self.array_btns.append(self.fifteen)

        count = 0
        for e in loop.run_until_complete(get_ids_bakalavr()):
            num = 50 + count * 350
            count += 1
            btn = self.array_btns[e - 1]
            btn.setGeometry(QtCore.QRect(round(150/1.8), round(num/1.8), round(1100/1.8), round(300/1.8)))
            font = QtGui.QFont()
            font.setFamily("Roboto")
            font.setPointSize(-1)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            btn.setFont(font)
            btn.setStyleSheet("background: #4052EF;\n"
                              "border-radius: 38px;\n"
                              "position: absolute;\n"
                              "\n"
                              "font-family: Roboto;\n"
                              "font-style: normal;\n"
                              "font-weight: normal;\n"
                              "font-size: 27px;\n"
                              "line-height: 84px;\n"
                              "display: flex;\n"
                              "align-items: center;\n"
                              "text-align: center;\n"
                              "\n"
                              "color: #FFFFFF;")
            btn.setIconSize(QtCore.QSize(round(676/1.8), round(186/1.8)))
            btn.setDefault(False)
            btn.setFlat(False)
            btn.setObjectName("btn_" + str(e))

        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions(MainWindow)

    def add_functions(self, MainWindow):
        self.back_btn.clicked.connect(lambda: self.back_click(MainWindow))

        loop = asyncio.get_event_loop()
        bakalavr_ids = loop.run_until_complete(get_ids_bakalavr())

        if 1 in bakalavr_ids:
            self.array_btns[0].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(1))[0]))
        if 2 in bakalavr_ids:
            self.array_btns[1].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(2))[0]))
        if 3 in bakalavr_ids:
            self.array_btns[2].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(3))[0]))
        if 4 in bakalavr_ids:
            self.array_btns[3].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(4))[0]))
        if 5 in bakalavr_ids:
            self.array_btns[4].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(5))[0]))
        if 6 in bakalavr_ids:
            self.array_btns[5].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(6))[0]))
        if 7 in bakalavr_ids:
            self.array_btns[6].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(7))[0]))
        if 8 in bakalavr_ids:
            self.array_btns[7].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(8))[0]))
        if 9 in bakalavr_ids:
            self.array_btns[8].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(9))[0]))
        if 10 in bakalavr_ids:
            self.array_btns[9].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(10))[0]))
        if 11 in bakalavr_ids:
            self.array_btns[10].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(11))[0]))
        if 12 in bakalavr_ids:
            self.array_btns[11].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(12))[0]))
        if 13 in bakalavr_ids:
            self.array_btns[12].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(13))[0]))
        if 14 in bakalavr_ids:
            self.array_btns[13].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(14))[0]))
        if 15 in bakalavr_ids:
            self.array_btns[14].clicked.connect(
                lambda: self.next_click(MainWindow, loop.run_until_complete(get_name_and_num_win(15))[0]))

    def back_click(self, MainWindow):
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def next_click(self, MainWindow, text_btn):
        ui = final_win.Ui_MainWindow()
        ui.setupUi(MainWindow, text_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.label.setText(_translate("MainWindow", "Бакалавриат"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))
        loop = asyncio.get_event_loop()
        bakalavr_ids = loop.run_until_complete(get_ids_bakalavr())

        for e in bakalavr_ids:
            name = loop.run_until_complete(get_name_and_num_win(e))[0]
            description = loop.run_until_complete(get_description(e))
            self.array_btns[e - 1].setText(_translate("MainWindow", name + '\n' + description))
