import asyncio
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from db_api.db_gino import db
from db_api import db_gino
from db_api.quick_cmd import create_db_specialist, get_last_queue, add_to_queue, next_queue, get_name_and_num_win, \
    get_ip_address, get_ids_bakalavr
from pages import start_win, queue
from server import server_start


def on_startup():
    print("Подключаем БД")
    db_gino.on_startup()
    print("Готово")

    print("Чистим БД")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.gino.drop_all())
    print("Готово")

    print("Создаем таблицу")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.gino.create_all())
    loop.run_until_complete(create_db_specialist())
    print("Готово")

    print("Запуск сервера")
    th_check = Thread(target=server_start, args=(loop, ))
    th_check.start()
    print("Готово")


def main():
    import sys
    on_startup()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = start_win.Ui_MainWindow()
    ui.setupUi(MainWindow)

    window = QtWidgets.QMainWindow()
    ui1 = queue.Ui_MainWindow()
    ui1.setupUi(window)
    window.show()
    window.setEnabled(True)

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()