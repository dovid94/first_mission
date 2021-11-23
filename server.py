import socket
import tqdm
import os


IP = '127.0.0.1'
PORT = 5001


def server():
    name = get_name()
    with socket.socket() as s:
        s.bind((IP, 6000))
        s.listen()
        conn, addr = s.accept()
        print('connected by', addr)
        while True:
            data = conn.recv(1024)
            save_file(data, name)
            conn.sendall(data)
            if not data:
                break
        s.close()
    return data


def save_file(fil, name):
    print(type(fil), fil) 
    with open(name, "ab") as new_file:
        new_file.write(fil)


def get_name():
    s = socket.socket()
    s.bind((IP, PORT))
    s.listen()
    conn, addr = s.accept()
    name = conn.recv(1024)
    the_name = name
    conn.sendall(name)
    s.close()
    return the_name


def run():
    stuff = server()
    save_file(stuff)


if __name__ == "__main__":
    run()


