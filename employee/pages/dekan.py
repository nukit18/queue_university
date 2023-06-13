import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 300)
        MainWindow.setMinimumSize(QtCore.QSize(580, 300))
        MainWindow.setMaximumSize(QtCore.QSize(580, 300))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 580, 61))
        self.label_3.setStyleSheet("font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 112px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #000000;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 538, 107))
        self.pushButton.setStyleSheet("background: #0C9700;\n"
"border-radius: 40px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 60px;\n"
"line-height: 112px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #FFFFFF;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 260, 61))
        self.label_2.setStyleSheet("font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 60px;\n"
"line-height: 112px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #000000;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_2.setBuddy(self.label_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.connection()


    def add_functions(self, sock):
        id_win = 1  # айди окна
        self.pushButton.clicked.connect(lambda: self.send_request(sock, id_win))

    def retranslateUi(self, MainWindow):
        id_win = 1  # айди окна
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.label_3.setText(_translate("MainWindow", "Номер талона: 0"))
        self.pushButton.setText(_translate("MainWindow", "Следующий"))
        self.label_2.setText(_translate("MainWindow", "Окно №" + str(id_win)))

    def next_queue(self, number):
        self.label_3.setText("Номер талона: " + str(number))

    def connection(self):
        import socket
        print("start_conn")
        sock = socket.socket()
        sock.connect(('192.168.31.46', 9090))  # ip хоста\терминала
        self.add_functions(sock)
        th_check = Thread(target=self.check_request, args=(sock, ))
        th_check.start()
        th_check_new_queue = Thread(target=self.send_skip_request, args=(sock, ))
        th_check_new_queue.start()


    def send_skip_request(self, sock):
        while True:
            time.sleep(5)
            sock.send("skip".encode())


    def check_request(self, sock):
        while True:
            data = sock.recv(1024)
            if not data:
                break
            self.next_queue(data.decode())
            # воспроизведение звука
            import pygame
            pygame.init()
            song = pygame.mixer.Sound('file.mp3')
            clock = pygame.time.Clock()
            song.play()
            clock.tick(2)
            pygame.quit()

    def send_request(self, sock, id_win):
        # номер окна
        sock.send(("win:" + str(id_win) + ":next").encode())