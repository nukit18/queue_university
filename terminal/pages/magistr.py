from PyQt5 import QtCore, QtGui, QtWidgets
from pages import start_win


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
        self.label.setGeometry(QtCore.QRect(round(426/1.8), 0, round(621/1.8), round(186/1.8)))
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
        self.back_btn.setGeometry(QtCore.QRect(round(470/1.8), round(750/1.8), round(500/1.8), round(140/1.8)))
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
"font-size: 42px;\n"
"line-height: 112px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #FFFFFF;")
        self.back_btn.setObjectName("back_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(round(245/1.8), round(400/1.8), round(950/1.8), round(186/1.8)))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("position: absolute;\n"
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
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # обработчик нажатий
        self.add_functions(MainWindow)

    def add_functions(self, MainWindow):
        self.back_btn.clicked.connect(lambda: self.back_click(MainWindow))

    def back_click(self, MainWindow):
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.label.setText(_translate("MainWindow", "Магистратура"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))
        self.label_2.setText(_translate("MainWindow", "Вам в кабинет №127"))
