import tkinter as tk

from Client import Client

class PlayerVsPlayerClient(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.ROCK = 0
        self.PAPER = 1
        self.SCISSORS = 2

        self.background_image = tk.PhotoImage(file = '../Backgrounds/playervsplayer2_background.png')
        self.background = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.background_image)
        self.background.place(x=0, y=0)

        self.back_button_image = tk.PhotoImage(file = '../Graphics/back_button.png')
        self.back_button = tk.Button(self, activebackground='black', image = self.back_button_image, command=lambda: controller.show_frame("HostClientPage"))
        self.back_button.place(x=1000, y=600)

        self.rock_image = tk.PhotoImage(file = '../Graphics/rock.png')
        self.rock_button = tk.Button(self, activebackground='black', image = self.rock_image, command=lambda: self.client_makes_move(self.ROCK))
        self.rock_button.place(x=149.5, y=180)

        self.paper_image = tk.PhotoImage(file = '../Graphics/paper.png')
        self.paper_button = tk.Button(self, activebackground='black', image = self.paper_image, command=lambda: self.client_makes_move(self.PAPER))
        self.paper_button.place(x=449.5, y=180)

        self.scissors_image = tk.PhotoImage(file = '../Graphics/scissors.png')
        self.scissors_button = tk.Button(self, activebackground='black', image = self.scissors_image, command=lambda: self.client_makes_move(self.SCISSORS))
        self.scissors_button.place(x=749.5, y=180)

        self.player1_score = 0
        self.player1_score_label = tk.Label(self, text=self.player1_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.player1_score_label.place(x=770, y=505)

        self.player2_score = 0
        self.player2_score_label = tk.Label(self, text=self.player2_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.player2_score_label.place(x=770, y=580)

    def client_makes_move(self, host_move): 
        if host_move == 0:
            Client.send_rock()
        elif host_move == 1:
            Client.send_paper()
        elif host_move == 2:
            Client.send_scissors()