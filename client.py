import socket


IP = '127.0.0.1'
PORT = 5001


def get_s():
    s = socket.socket()
    s.connect((IP, PORT))
    return s


def get_user_data():
    f_name = input("enter the file name and location: ")
    try: 
        data = f_name.open(f_name, "r")
    except:
        print("you did not put the name and location correctly, or the file does not exist")
        return


def get_list(s):
    s.sendall(0)
    data = s.recv(4096)
    print(data)
    s.close()


def get_file(s):
    s.sendall(1)
    f = s.recv(4096)
    text_f = open("new_file.txt", "w")
    text_f.write(f)
    text_f.close
    s.close()


def update():
    data = get_user_data()
    if data is NONE:
        return
    s = get_s()
    s.sendall(data)
    s.close()


def runer():
    user_d = input(r"enter 'upload' to upload a file, 'download' to get a file, and 'see' to see the list of files")
    if user_d == "upload":
        update()
    elif user_d == "download":
        s = get_s()
        get_file(s)
    elif user_d == "see":
        s = get_s()
        get_list(s)
    else:
        print("wrong input")
    return


if __name__ == "__main__":
    runer()







