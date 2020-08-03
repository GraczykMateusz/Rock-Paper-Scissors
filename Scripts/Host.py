import threading
import time
import socket

from ConnectingHostPage import ConnectingHostPage

class Host:

    socket_connection = None
    cs = None

    msg_decoded = None

    t1 = None
    t2 = None
    
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
                receiv_socket.connect((socket.gethostname(), 45000))
                
                msg = receiv_socket.recv(10)
                msg_decoded = msg.decode("utf-8")

                if msg_decoded == "CONNECTION":
                    ConnectingHostPage._connected()
                    is_connected = True
            except:
                pass

        while True:
            try:
                receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                receiv_socket.connect((socket.gethostname(), 45000))
                
                msg = receiv_socket.recv(10)
                cls.msg_decoded = msg.decode("utf-8")

                if cls.msg_decoded == "ROCK":
                    print(cls.msg_decoded)
                elif cls.msg_decoded == "PAPER":
                    print(cls.msg_decoded)
                elif cls.msg_decoded == "SCISSORS":
                    print(cls.msg_decoded)
            except Exception as err:
                print(err)



    @classmethod
    def lose_connection(cls):
        pass
