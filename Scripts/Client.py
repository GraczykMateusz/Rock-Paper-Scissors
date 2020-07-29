import threading
import time
import socket
import sys

from ConnectingClientPage import ConnectingClientPage

class Client:
    
    socket_connection = None
    cs = None

    t1 = None
    t2 = None

    @classmethod
    def connecting(cls):

        try:
            cls.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cls.socket_connection.bind((socket.gethostname(), 45000))
            cls.socket_connection.listen(1)
        except Exception as err:
            print(err)
            cls.socket_connection.close()

        try:
            cls.t1 = threading.Thread(target=cls.try_connect, daemon=True)
            cls.t2 = threading.Thread(target=cls.receiv, daemon=True)
            cls.t1.start()
            cls.t2.start()
        except:
            print("Error: unable to start thread")
    
    @classmethod
    def try_connect(cls):
        is_connected = False
        connection_msg = "CONNECTION"
        
        while is_connected is False:
            try:
                cls.cs, address = cls.socket_connection.accept()
                cls.cs.send(bytes(connection_msg.encode("utf-8")))
                is_connected = True
            except:
                pass
    
    @classmethod
    def receiv(cls):
        is_connected = False
        
        while is_connected is False:
            try:
                receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                receiv_socket.connect((socket.gethostname(), 50000))
                
                msg = receiv_socket.recv(10)
                msg_decoded = msg.decode("utf-8")

                if msg_decoded == "CONNECTION":
                    ConnectingClientPage._connected()
                    is_connected = True
            except:
                pass

        while True:
            try:
                pass       
            except Exception as err:
                print(err)

    @classmethod
    def send(cls, msg):    
        try:
            cls.cs, address = cls.socket_connection.accept()
            cls.cs.send(bytes(msg.encode("utf-8")))
        except:
            pass

    @classmethod
    def send_rock(cls):
        cls.send("ROCK")

    @classmethod
    def send_paper(cls):
        cls.send("PAPER")
    
    @classmethod
    def send_scissors(cls):
        cls.send("SCISSORS")