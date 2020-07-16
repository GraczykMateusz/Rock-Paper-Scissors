import tkinter as tk

from Menu import Menu
from PlayerVsBot import PlayerVsBot
from HostClientPage import HostClientPage
from ConnectingHostPage import ConnectingHostPage
from ConnectingClientPage import ConnectingClientPage
from PlayerVsPlayerClient import PlayerVsPlayerClient
from PlayerVsPlayerHost import PlayerVsPlayerHost

class FramesController(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("1088x708")
        self.resizable(width=False, height=False)
        self.title("Rock-Paper-Scissors by Mateusz Graczyk")
        self.iconphoto(True, tk.PhotoImage(file = "../Graphics/icon.png"))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["Menu"] = Menu(parent=container, controller=self)
        self.frames["PlayerVsBot"] = PlayerVsBot(parent=container, controller=self)
        self.frames["HostClientPage"] = HostClientPage(parent=container, controller=self)
        self.frames["ConnectingHostPage"] = ConnectingHostPage(parent=container, controller=self)
        self.frames["ConnectingClientPage"] = ConnectingClientPage(parent=container, controller=self)
        self.frames["PlayerVsPlayerClient"] = PlayerVsPlayerClient(parent=container, controller=self)
        self.frames["PlayerVsPlayerHost"] = PlayerVsPlayerHost(parent=container, controller=self)
        
        self.frames["Menu"].grid(row=0, column=0, sticky="nsew")
        self.frames["PlayerVsBot"].grid(row=0, column=0, sticky="nsew")
        self.frames["HostClientPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["ConnectingHostPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["ConnectingClientPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PlayerVsPlayerClient"].grid(row=0, column=0, sticky="nsew")
        self.frames["PlayerVsPlayerHost"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()