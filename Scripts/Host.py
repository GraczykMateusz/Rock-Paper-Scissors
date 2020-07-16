import _thread
import time
import socket

from ConnectingHostPage import ConnectingHostPage

class Host:
    @classmethod
    def connecting(cls):

        # Connection
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((socket.gethostname(), 50000))
            s.listen(1)
        except:
            print("!Connection")
            s.close()

        # Sender
        def send(threadName, delay):
            while True:
                x = input()

                cs, address = s.accept()
                try:
                    cs.send(bytes(x.encode("utf-8")))
                except:
                    pass

        def receiv(threadName, delay):
            while True:
                try:
                    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    send_socket.connect((socket.gethostname(), 45000))
                    
                    msg = send_socket.recv(10)
                    msg_decoded = msg.decode("utf-8")
                    if msg_decoded != "wait":
                        print(msg_decoded)
                        ConnectingHostPage._connected()
                except Exception as e:
                    print(e)

        try:
            _thread.start_new_thread(send, ("Thread-3", 4,))
            _thread.start_new_thread(receiv, ("Thread-4", 4,))
        except:
            print("Error: unable to start thread")

            