import tkinter as tk

from ConnectingPage import ConnectingPage

class ConnectingHostPage(ConnectingPage):    
    is_connected = None
    
    def __init__(self, parent, controller):
        self.controller = controller
        self._config(parent, controller)

        ConnectingHostPage.is_connected = tk.BooleanVar()

        ConnectingHostPage.is_connected.trace('w', lambda var, indx, mode: self.controller.show_frame("PlayerVsPlayerHost"))

    @classmethod
    def _connected(cls):
        ConnectingHostPage.is_connected.set(True)