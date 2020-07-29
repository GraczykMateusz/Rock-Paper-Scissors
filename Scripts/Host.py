import _thread
import time
import socket

from ConnectingHostPage import ConnectingHostPage

class Host:

    socket_connection = None
    cs = None
    
    @classmethod
    def connecting(cls):
        try:
            cls.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cls.socket_connection.bind((socket.gethostname(), 50000))
            cls.socket_connection.listen(1)
        except Exception as err:
            print(err)
            cls.socket_connection.close()

        try:
            _thread.start_new_thread(cls.try_connect, ("Thread-3", 4,))
            _thread.start_new_thread(cls.receiv, ("Thread-4", 4,))
        except:
            print("Error: unable to start thread")

    @classmethod       
    def try_connect(cls, threadName, delay):
        is_connected = "connected"
        
        while True:
            try:
                cls.cs, address = cls.socket_connection.accept()
                cls.cs.send(bytes(is_connected.encode("utf-8")))
            except:
                pass
    
    @classmethod
    def receiv(cls, threadName, delay):
        is_connected = False

        while is_connected is False:
            try:
                receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                receiv_socket.connect((socket.gethostname(), 45000))
                
                msg = receiv_socket.recv(10)
                msg_decoded = msg.decode("utf-8")

                if msg_decoded == "connected":
                    ConnectingHostPage._connected()
                    is_connected = True

            except Exception as err:
                print(err)

        while True:
            try:
                receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                receiv_socket.connect((socket.gethostname(), 45000))
                
                msg = receiv_socket.recv(10)
                msg_decoded = msg.decode("utf-8")
                print(msg_decoded)
                if msg_decoded == "ROCK":
                    pass
                elif msg_decoded == "PAPER":
                    pass
                elif msg_decoded == "SCISSORS":
                    pass
                    
            except Exception as err:
                print(err)

    @classmethod
    def lose_connection(cls):
        pass
