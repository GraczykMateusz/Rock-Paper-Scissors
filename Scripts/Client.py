import _thread
import time
import socket

from ConnectingClientPage import ConnectingClientPage

class Client:

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
                    receiv_socket.connect((socket.gethostname(), 50000))
                    
                    msg = receiv_socket.recv(10)
                    msg_decoded = msg.decode("utf-8")

                    if msg_decoded == "connected":
                        ConnectingClientPage._connected()

                except Exception as err:
                    print(err)

        try:
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.bind((socket.gethostname(), 45000))
            socket_connection.listen(1)
        except Exception as err:
            print(err)
            socket_connection.close()

        try:
            _thread.start_new_thread(try_connect, ("Thread-1", 4,))
            _thread.start_new_thread(receiv, ("Thread-2", 4,))
        except:
            print("Error: unable to start thread")