import _thread
import time
import socket

from ConnectingHostPage import ConnectingHostPage

class Host:

    @classmethod
    def connecting(cls):
    
        def try_connect(threadName, delay):
            is_connected = "connected"
            
            while True:
                try:
                    cs, address = socket_connection.accept()
                    cs.send(bytes(is_connected.encode("utf-8")))
                except:
                    pass

        def receiv(threadName, delay):
            while True:
                try:
                    receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    receiv_socket.connect((socket.gethostname(), 45000))
                    
                    msg = receiv_socket.recv(10)
                    msg_decoded = msg.decode("utf-8")

                    if msg_decoded == "connected":
                        ConnectingHostPage._connected()
                        #send feedback to client
                        
                except Exception as err:
                    print(err)

            while True:
                try:
                    receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    receiv_socket.connect((socket.gethostname(), 45000))
                    
                    msg = receiv_socket.recv(10)
                    msg_decoded = msg.decode("utf-8")

                    if msg_decoded == "ROCK":
                        pass
                    elif msg_decoded == "PAPER":
                        pass
                    elif msg_decoded == "SCISSORS":
                        pass
                        
                except Exception as err:
                    print(err)

        try:
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.bind((socket.gethostname(), 50000))
            socket_connection.listen(1)
        except Exception as err:
            print(err)
            socket_connection.close()

        try:
            _thread.start_new_thread(try_connect, ("Thread-3", 4,))
            _thread.start_new_thread(receiv, ("Thread-4", 4,))
        except:
            print("Error: unable to start thread")

    @classmethod
    def send_rock(cls):
        pass

    @classmethod
    def send_paper(cls):
        pass
    
    @classmethod
    def send_scissors(cls):
        pass

    @classmethod
    def lose_connection(cls):
        pass
