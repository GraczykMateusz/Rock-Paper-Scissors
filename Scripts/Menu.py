import tkinter as tk

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.background_image = tk.PhotoImage(file = '../Backgrounds/main_background.png')
        self.background = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.background_image)
        self.background.place(x=0, y=0)

        self.start_playervsbot_button_image = tk.PhotoImage(file = '../Graphics/start_button.png')
        self.start_playervsbot_button = tk.Button(self, activebackground='black', image = self.start_playervsbot_button_image, command=lambda: controller.show_frame("PlayerVsBot"))
        self.start_playervsbot_button.place(x=715, y=230)

        self.start_playervsplayer_button_image = tk.PhotoImage(file = '../Graphics/start_button.png')
        self.start_playervsplayer_button = tk.Button(self, activebackground='black', image = self.start_playervsplayer_button_image, command=lambda: controller.show_frame("HostClientPage"))
        self.start_playervsplayer_button.place(x=715, y=438)
