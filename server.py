import socket
import tqdm
import os


IP = '127.0.0.1'
PORT = 5001


def server():
    new_file = []
    with socket.socket() as s:
        s.bind((IP, PORT))
        s.listen()
        conn, addr = s.accept()
        print('connected by', addr)
        data = conn.recv(1024)
        new_file.append(data)
        print(new_file)
        conn.sendall(data)
    return new_file


def save_file(fil, f_name):
    f = open(f_name, "w")
    f.write(fil)


def run():
    f = server()
    f_name = server()
    save_file(f, f_name)


if __name__ == "__main__":
    run()


