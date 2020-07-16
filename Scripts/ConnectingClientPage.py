import tkinter as tk

from ConnectingPage import ConnectingPage

class ConnectingClientPage(ConnectingPage):

    is_connected = None

    def __init__(self, parent, controller):
        self.controller = controller
        self._config(parent, controller)

        ConnectingClientPage.is_connected = tk.BooleanVar()

        ConnectingClientPage.is_connected.trace('w', lambda var, indx, mode: self.controller.show_frame("PlayerVsPlayerClient"))

    @classmethod
    def _connected(cls):
        ConnectingClientPage.is_connected.set(True)
