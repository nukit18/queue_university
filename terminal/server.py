import asyncio
from _thread import start_new_thread
from threading import Thread

from db_api.quick_cmd import get_last_queue, get_name_and_num_win, next_queue, read_new_queue, get_id_by_ip, \
    on_reception_get, on_reception_add


def server_start(loop):
    import socket

    sock = socket.socket()
    sock.bind(('', 9090))  # айпи сервера\хоста(текущей машины), оставить пустым
    sock.listen(15)
    while True:
        conn, addr = sock.accept()
        print('Connected to :', addr[0], ':', addr[1])
        th_action2 = Thread(target=threaded, args=(conn, loop, addr[0], ))
        th_action2.start()


def threaded(conn, loop, ip_address):
    while True:
        id_spec = loop.run_until_complete(get_id_by_ip(ip_address))
        new_queue_bool = loop.run_until_complete(read_new_queue(id_spec))
        if new_queue_bool == 1:
            send_response(loop, id_spec, conn)
            print("send")
        data = conn.recv(1024)
        if data.decode() == "skip":
            continue
        if not data:
            break
        arr_info = data.decode().split(":")
        if arr_info[2] == "next":
            try:
                talon = loop.run_until_complete(next_queue(int(arr_info[1])))
                conn.send((str(talon)).encode())
            except:
                print("Error in next_spec")
    conn.close()


def send_response(loop, id_spec, conn):
    talon = loop.run_until_complete(next_queue(id_spec))
    conn.send((str(talon)).encode())
