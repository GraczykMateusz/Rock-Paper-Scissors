import tkinter as tk

from Menu import Menu
from PlayerVsBot import PlayerVsBot
from PlayerVsPlayer import PlayerVsPlayer

class FramesController(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("1088x708")
        self.resizable(width=False, height=False)
        self.title("Rock-Paper-Scissors by Mateusz Graczyk")
        self.iconphoto(True, tk.PhotoImage(file = "../Graphics/icon.png"))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["Menu"] = Menu(parent=container, controller=self)
        self.frames["PlayerVsPlayer"] = PlayerVsPlayer(parent=container, controller=self)
        self.frames["PlayerVsBot"] = PlayerVsBot(parent=container, controller=self)

        self.frames["Menu"].grid(row=0, column=0, sticky="nsew")
        self.frames["PlayerVsPlayer"].grid(row=0, column=0, sticky="nsew")
        self.frames["PlayerVsBot"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()