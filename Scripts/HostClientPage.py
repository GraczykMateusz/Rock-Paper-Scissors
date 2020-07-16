import tkinter as tk

from Client import Client
from Host import Host

class HostClientPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.background_image = tk.PhotoImage(file = '../Backgrounds/hostclient_background.png')
        self.background = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.background_image)
        self.background.place(x=0, y=0)

        self.back_button_image = tk.PhotoImage(file = '../Graphics/back_button.png')
        self.back_button = tk.Button(self, activebackground='black', image = self.back_button_image, command=lambda: controller.show_frame("Menu"))
        self.back_button.place(x=1000, y=600)

        self.host_image = tk.PhotoImage(file = '../Graphics/host.png')
        self.host = tk.Button(self, activebackground='black', image = self.host_image, command=lambda: [controller.show_frame("ConnectingHostPage"), Client.connecting()])
        self.host.place(x=268, y=180)

        self.client_image = tk.PhotoImage(file = '../Graphics/client.png')
        self.client = tk.Button(self, activebackground='black', image = self.client_image, command=lambda: [controller.show_frame("ConnectingClientPage"), Host.connecting()])
        self.client.place(x=630, y=180)