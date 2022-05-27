import socket
import pickle
from _thread import start_new_thread
from color import Color

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "localhost"
port = 5555
connections = 0
try:
    s.bind((server, port))
except Exception as e:
    print(str(e))
s.listen(3)

turn = Color()
board = []
game = ("on", None)

def client_thread(conn):
    global connections, turn, board, game
    if connections == 0:
        conn.send(pickle.dumps("w"))
    else:
        conn.send(pickle.dumps("b"))
    connections += 1
    while True:
        try:
            data = pickle.loads(conn.recv(10000))
            if not data:
                break
            elif data == "check":
                conn.send(pickle.dumps((board, turn, game)))
            elif data[0] == "new":
                board = data[1]
                turn.color = data[2]
                game = data[3]
                conn.send(pickle.dumps("Received"))
            else:
                conn.send(pickle.dumps((board, turn, game)))

        except Exception as e:
            print(str(e))
            exit(0)
            break


while True:
    conn, addr = s.accept()
    print(f"Connected: {addr}")
    start_new_thread(client_thread, (conn, ))