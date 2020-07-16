import tkinter as tk
from abc import ABC, abstractmethod

class ConnectingPage(tk.Frame, ABC):
    def _config(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.background_image = tk.PhotoImage(file = '../Backgrounds/connecting_background.png')
        self.background = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.background_image)
        self.background.place(x=0, y=0)

        self.back_button_image = tk.PhotoImage(file = '../Graphics/back_button.png')
        self.back_button = tk.Button(self, activebackground='black', image = self.back_button_image, command=lambda: controller.show_frame("HostClientPage"))
        self.back_button.place(x=1000, y=600)

    @abstractmethod
    def _connected(self):
        pass
        