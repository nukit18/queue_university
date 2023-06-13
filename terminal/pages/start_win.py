import time

from pages import bakalavr_new, specialist_new, magistr
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(round(1440/1.8), round(1024/1.8))
        MainWindow.setMinimumSize(QtCore.QSize(round(1440/1.8), round(1024/1.8)))
        MainWindow.setMaximumSize(QtCore.QSize(round(1440/1.8), round(1024/1.8)))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-11, -22, round(1509/1.8), round(315/1.8)))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setPixmap(QtGui.QPixmap("pages/фон.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.bak_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bak_btn.setGeometry(QtCore.QRect(round(382/1.8), round(318/1.8), round(676/1.8), round(186/1.8)))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bak_btn.setFont(font)
        self.bak_btn.setStyleSheet("background: #4052EF;\n"
                                   "border-radius: 38px;\n"
                                   "position: absolute;\n"
                                   "width: 588px;\n"
                                   "height: 186px;\n"
                                   "left: 421px;\n"
                                   "top: 318px;\n"
                                   "\n"
                                   "font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 53px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.bak_btn.setIconSize(QtCore.QSize(round(676/1.8), round(186/1.8)))
        self.bak_btn.setDefault(False)
        self.bak_btn.setFlat(False)
        self.bak_btn.setObjectName("bak_btn")
        self.spec_btn = QtWidgets.QPushButton(self.centralwidget)
        self.spec_btn.setGeometry(QtCore.QRect(round(382/1.8), round(563/1.8), round(676/1.8), round(186/1.8)))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spec_btn.setFont(font)
        self.spec_btn.setStyleSheet("background: #4052EF;\n"
                                    "border-radius: 38px;\n"
                                    "position: absolute;\n"
                                    "width: 588px;\n"
                                    "height: 186px;\n"
                                    "left: 421px;\n"
                                    "top: 318px;\n"
                                    "\n"
                                    "font-family: Roboto;\n"
                                    "font-style: normal;\n"
                                    "font-weight: normal;\n"
                                    "font-size: 53px;\n"
                                    "line-height: 112px;\n"
                                    "display: flex;\n"
                                    "align-items: center;\n"
                                    "\n"
                                    "color: #FFFFFF;")
        self.spec_btn.setIconSize(QtCore.QSize(round(676/1.8), round(186/1.8)))
        self.spec_btn.setDefault(False)
        self.spec_btn.setFlat(False)
        self.spec_btn.setObjectName("spec_btn")
        self.mag_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mag_btn.setGeometry(QtCore.QRect(round(382/1.8), round(808/1.8), round(676/1.8), round(186/1.8)))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mag_btn.setFont(font)
        self.mag_btn.setStyleSheet("background: #4052EF;\n"
                                   "border-radius: 38px;\n"
                                   "position: absolute;\n"
                                   "width: 588px;\n"
                                   "height: 186px;\n"
                                   "left: 421px;\n"
                                   "top: 318px;\n"
                                   "\n"
                                   "font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 53px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.mag_btn.setIconSize(QtCore.QSize(round(676/1.8), round(186/1.8)))
        self.mag_btn.setDefault(False)
        self.mag_btn.setFlat(False)
        self.mag_btn.setObjectName("mag_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # обработчик нажатий
        self.add_functions(MainWindow)


    def add_functions(self, MainWindow):
        self.bak_btn.clicked.connect(lambda: self.bakalavr_click(MainWindow))
        self.spec_btn.clicked.connect(lambda: self.specialist_click(MainWindow))
        self.mag_btn.clicked.connect(lambda: self.magistr_click(MainWindow))

    def bakalavr_click(self, MainWindow):
        ui = bakalavr_new.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def specialist_click(self, MainWindow):
        ui = specialist_new.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def magistr_click(self, MainWindow):
        ui = magistr.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.bak_btn.setText(_translate("MainWindow", "Бакалавриат"))
        self.spec_btn.setText(_translate("MainWindow", "Специалитет"))
        self.mag_btn.setText(_translate("MainWindow", "Магистратура"))
