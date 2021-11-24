import socket
import threading
import time


IP = '127.0.0.1'
PORT1 = 5001
PORT2 = 5002


def get_s():
    s = socket.socket()
    s.connect((IP, PORT2))
    return s


def sender():
    unsent_msg = []
    while True:
        unsent_msg.append(input())
        try:
            while True:
                s = get_s()
                s.sendall(str.encode(unsent_msg.pop(0)))
                data = s.recv(1024)
                s.close
        except ConnectionRefusedError:
            time.sleep(1)
            continue
        except IndexError:
            s.close


def reciever():
    s = socket.socket()
    s.bind((IP, PORT1))
    s.listen()
    while True:
        conn = s.accept()[0]
        data = conn.recv(1024)
        conn.sendall(data)
        print(data.decode())


if __name__ == "__main__":
    sen = threading.Thread(target=sender)
    rec = threading.Thread(target=reciever)

    sen.start()
    rec.start()


