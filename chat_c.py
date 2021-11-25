import socket
import threading
import time


IP = '127.0.0.1'
PORT1 = 5002
PORT2 = 5001


def get_s():
    """returns a connected socket"""
    s = socket.socket()
    s.connect((IP, PORT2))
    return s


def sender():
    """puts the messages in a list and sends them to the server"""
    unsent_msg = []
    while True:
        if connection_tester() == True:
            unsent_msg.append(input())
            while len(unsent_msg) > 0:
                try:
                    s = get_s()
                    s.sendall(str.encode(unsent_msg.pop(0)))
                    data = s.recv(1024)
                    s.close()
                except:
                    continue
        elif connection_tester == False:
            unsent_msg.append(input())


def connection_tester():
    """checks if the server is connected"""
    try:
        s = get_s()
        s.close()
        return True
    except ConnectionRefusedError:
        return False


def reciever():
    """establishes a server and prints the messages"""
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



