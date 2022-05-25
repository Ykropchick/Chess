import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connection()

    def my_color(self):
        return self.p

    def connection(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except Exception as e:
            print(str(e))

    def check_the_data(self):
        self.client.send(pickle.dumps("check"))
        return pickle.loads(self.client.recv(4096))

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except Exception as e:
            print(str(e))
